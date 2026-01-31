# Currency Exchange CLI

A simple NZD to USD currency exchange command-line tool with XE API integration.

## Introduction

A command-line currency exchange program that supports NZD to USD conversion using live exchange rates from XE API, and saves each transaction to a database.

## Features

- Live exchange rate from XE API
- Fallback to default rate if API unavailable
- Persistent transaction storage (SQLite)
- Transaction history query
- Rate refresh on demand
- Comprehensive error handling and logging

## Tech Stack

- Python 3.x
- SQLite3 (Data persistence)
- XE Currency Data API (Live rates)
- OOP Design Pattern

## Project Structure

```
Week6Activity8/
├── main.py           # Main program (contains all classes and logic)
├── requirements.txt  # Dependencies
├── README.md         # Project documentation
├── .env.example      # Environment variables template
├── .env              # Your API credentials (create from .env.example)
├── exchange.db       # SQLite database (auto-generated)
└── app.log           # Log file (auto-generated)
```

## OOP Design

### Class Structure

| Class | Responsibility |
|-------|----------------|
| `ExchangeError` | Custom base exception class |
| `InvalidAmountError` | Invalid amount exception |
| `APIError` | API request failure exception |
| `ExchangeService` | Business logic: API calls, rate calculation, database operations |
| `ExchangeApp` | Presentation layer: CLI user interaction |

## Database Design

### transactions Table

| Field | Type | Description |
|-------|------|-------------|
| id | INTEGER | Primary key, auto-increment |
| nzd_amount | REAL | NZD amount |
| usd_amount | REAL | USD amount |
| rate | REAL | Exchange rate used |
| created_at | TEXT | Creation timestamp |

## Setup

### 1. Install Dependencies

```bash
cd Week6Activity8
pip install -r requirements.txt
```

### 2. Configure API Credentials

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your XE API credentials
# Get credentials at: https://xecdapi.xe.com/
```

### 3. Run the Application

```bash
python main.py
```

## Usage Example

```
====== Currency Exchange System ======
Current Rate: 1 NZD = 0.6215 USD

1. Convert NZD -> USD
2. View History
3. Refresh Rate
4. Exit

Select option: 1
Enter NZD amount: 100
Success: 100.00 NZD -> 62.15 USD (Rate: 0.6215)

Select option: 3
Rate refreshed: 1 NZD = 0.6218 USD
```

## API Integration

### XE Currency Data API

- **Endpoint**: `https://xecdapi.xe.com/v1/convert_from`
- **Authentication**: HTTP Basic Auth
- **Documentation**: https://xecdapi.xe.com/docs/v1

### Fallback Behavior

If API credentials are not configured or API request fails:
- Uses default rate: 0.62
- Logs warning message
- Continues to function normally

## Error Handling

| Exception | Description |
|-----------|-------------|
| `InvalidAmountError` | Amount must be greater than 0 |
| `APIError` | API request failed (auth, timeout, etc.) |
| `ValueError` | Input must be a valid number |

All exceptions are logged to `app.log`.

## Logging System

Logs are output to:
- Console (real-time viewing)
- `app.log` file (persistent storage)

Log format:
```
2026-01-25 14:30:00 - INFO - Live rate fetched: 1 NZD = 0.6215 USD
2026-01-25 14:30:05 - INFO - Conversion successful: 100 NZD -> 62.15 USD @ 0.6215
2026-01-25 14:30:15 - ERROR - API request failed: Connection timeout
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `XE_ACCOUNT_ID` | Your XE API account ID |
| `XE_API_KEY` | Your XE API key |

## Author

Yaohui Zhang - 2026-01-25
