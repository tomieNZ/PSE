"""
Currency Exchange CLI - NZD to USD
A simple command-line currency exchange tool with OOP design and XE API integration.
@author: Yaohui Zhang
@date: 2026-01-25
"""
import os
import sqlite3
import logging
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, FloatPrompt
from rich.text import Text
from rich import box

# Load environment variables from .env file
load_dotenv(".env")

# Initialize Rich console
console = Console()


# ==================== Logging Configuration ====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# ==================== Custom Exceptions ====================
class ExchangeError(Exception):
    """Base exception for exchange system"""
    pass


class InvalidAmountError(ExchangeError):
    """Exception for invalid amount input"""
    pass


class APIError(ExchangeError):
    """Exception for API request failures"""
    pass


# ==================== Business Service Class ====================
class ExchangeService:
    """Currency exchange service class - handles business logic, API calls and database operations"""

    XE_API_URL = "https://xecdapi.xe.com/v1/convert_from"
    DEFAULT_RATE = 0.62  # Fallback rate if API fails

    def __init__(self, db_path="exchange.db"):
        """Initialize database connection and API credentials"""
        self.account_id = os.getenv("XE_ACCOUNT_ID")
        self.api_key = os.getenv("XE_API_KEY")
        self.rate = None  # Will be fetched from API
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()
        
        # Check API credentials
        if not self.account_id or not self.api_key:
            logger.warning("XE API credentials not found, using default rate")
            self.rate = self.DEFAULT_RATE
        else:
            logger.info("ExchangeService initialized with XE API")

    def _create_table(self):
        """Create transactions table if not exists"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nzd_amount REAL NOT NULL,
                usd_amount REAL NOT NULL,
                rate REAL NOT NULL,
                created_at TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def get_live_rate(self, from_currency="NZD", to_currency="USD"):
        """
        Fetch live exchange rate from XE API
        :param from_currency: Source currency code
        :param to_currency: Target currency code
        :return: Current exchange rate
        :raises APIError: When API request fails
        """
        if not self.account_id or not self.api_key:
            logger.info(f"Using default rate: {self.DEFAULT_RATE}")
            return self.DEFAULT_RATE

        try:
            response = requests.get(
                self.XE_API_URL,
                auth=HTTPBasicAuth(self.account_id, self.api_key),
                params={
                    "from": from_currency,
                    "to": to_currency,
                    "amount": 1
                },
                timeout=10
            )
            
            # Handle HTTP errors
            if response.status_code == 401:
                raise APIError("Invalid API credentials")
            elif response.status_code == 429:
                raise APIError("API rate limit exceeded")
            
            response.raise_for_status()
            
            data = response.json()
            rate = data["to"][0]["mid"]
            logger.info(f"Live rate fetched: 1 {from_currency} = {rate} {to_currency}")
            return rate

        except requests.Timeout:
            logger.error("API request timeout, using default rate")
            return self.DEFAULT_RATE
        except requests.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise APIError(f"Failed to fetch live rate: {e}")

    def get_current_rate(self):
        """Get current rate (from cache or API)"""
        if self.rate is None:
            self.rate = self.get_live_rate()
        return self.rate

    def refresh_rate(self):
        """Force refresh rate from API"""
        self.rate = self.get_live_rate()
        return self.rate

    def convert(self, nzd_amount):
        """
        Execute currency conversion with live rate
        :param nzd_amount: Amount in NZD
        :return: Tuple of (USD amount, rate used)
        :raises InvalidAmountError: When amount is invalid
        """
        if nzd_amount <= 0:
            raise InvalidAmountError("Amount must be greater than 0")
        
        rate = self.get_current_rate()
        usd_amount = round(nzd_amount * rate, 2)
        self._save_transaction(nzd_amount, usd_amount, rate)
        logger.info(f"Conversion successful: {nzd_amount} NZD -> {usd_amount} USD @ {rate}")
        return usd_amount, rate

    def _save_transaction(self, nzd, usd, rate):
        """Save transaction record to database"""
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            'INSERT INTO transactions (nzd_amount, usd_amount, rate, created_at) VALUES (?, ?, ?, ?)',
            (nzd, usd, rate, created_at)
        )
        self.conn.commit()

    def get_history(self):
        """Get all transaction history records"""
        self.cursor.execute('SELECT * FROM transactions ORDER BY id DESC')
        records = self.cursor.fetchall()
        logger.info(f"Query history: {len(records)} records found")
        return records

    def close(self):
        """Close database connection"""
        self.conn.close()


# ==================== CLI Application Class ====================
class ExchangeApp:
    """Command-line interface application class with Rich UI"""

    def __init__(self):
        """Initialize application"""
        self.service = ExchangeService()

    def show_menu(self):
        """Display styled menu options"""
        rate = self.service.get_current_rate()
        
        # Create header panel
        header = Text()
        header.append("Currency Exchange System\n", style="bold cyan")
        header.append(f"Current Rate: 1 NZD = {rate} USD", style="green")
        console.print(Panel(header, box=box.DOUBLE, border_style="cyan"))
        
        # Create menu table
        menu = Table(show_header=False, box=box.SIMPLE, padding=(0, 2))
        menu.add_column("Option", style="bold yellow")
        menu.add_column("Description", style="white")
        menu.add_row("[1]", "Convert NZD -> USD")
        menu.add_row("[2]", "View History")
        menu.add_row("[3]", "Refresh Rate")
        menu.add_row("[4]", "Exit")
        console.print(menu)

    def run(self):
        """Run main application loop"""
        console.print("\n[bold green]Welcome to Currency Exchange CLI![/bold green]\n")
        
        while True:
            self.show_menu()
            choice = Prompt.ask("\n[bold]Select option[/bold]", choices=["1", "2", "3", "4"])

            if choice == "1":
                self._handle_convert()
            elif choice == "2":
                self._handle_history()
            elif choice == "3":
                self._handle_refresh()
            elif choice == "4":
                console.print("\n[bold cyan]Goodbye![/bold cyan]\n")
                self.service.close()
                break

    def _handle_convert(self):
        """Handle conversion operation with styled output"""
        try:
            amount = FloatPrompt.ask("[bold]Enter NZD amount[/bold]")
            usd_amount, rate = self.service.convert(amount)
            
            # Create result panel
            result = Text()
            result.append(f"{amount:.2f} NZD", style="bold yellow")
            result.append(" -> ", style="white")
            result.append(f"{usd_amount:.2f} USD", style="bold green")
            result.append(f"\n(Rate: {rate})", style="dim")
            
            console.print(Panel(result, title="[green]Conversion Success[/green]", 
                               border_style="green", box=box.ROUNDED))
            
        except ValueError:
            logger.error("Input error: Please enter a valid number")
            console.print("[bold red]Error:[/bold red] Please enter a valid number")
        except InvalidAmountError as e:
            logger.error(f"Amount error: {e}")
            console.print(f"[bold red]Error:[/bold red] {e}")
        except APIError as e:
            logger.error(f"API error: {e}")
            console.print(f"[bold red]Error:[/bold red] {e}")

    def _handle_history(self):
        """Handle view history operation with styled table"""
        records = self.service.get_history()
        
        if not records:
            console.print("[yellow]No transaction records found[/yellow]")
            return
        
        # Create styled table
        table = Table(title="Transaction History", box=box.ROUNDED, 
                     header_style="bold cyan", border_style="blue")
        table.add_column("ID", style="dim", justify="right")
        table.add_column("NZD", style="yellow", justify="right")
        table.add_column("USD", style="green", justify="right")
        table.add_column("Rate", style="magenta", justify="right")
        table.add_column("Time", style="dim")
        
        for r in records:
            table.add_row(
                str(r[0]),
                f"{r[1]:.2f}",
                f"{r[2]:.2f}",
                f"{r[3]:.4f}",
                r[4]
            )
        
        console.print(table)

    def _handle_refresh(self):
        """Handle rate refresh operation with styled output"""
        try:
            with console.status("[bold green]Refreshing rate...", spinner="dots"):
                rate = self.service.refresh_rate()
            console.print(f"[bold green]Rate refreshed:[/bold green] 1 NZD = {rate} USD")
        except APIError as e:
            logger.error(f"Refresh failed: {e}")
            console.print(f"[bold red]Error:[/bold red] {e}")


# ==================== Program Entry ====================
if __name__ == "__main__":
    app = ExchangeApp()
    app.run()
