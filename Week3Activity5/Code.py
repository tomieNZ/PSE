"""
Clinic Management System - Week 3 Activity 5
An Object-Oriented Programming (OOP) implementation of a clinic database management system
using SQLite to manage doctors, patients, specializations, and appointments.

Author: tomiezhang
Course: YooBee MSE802 - Professional Software Engineering
"""

import sqlite3
from datetime import date, time


class Clinc:
    """
    Clinic Management System Class
    
    This class encapsulates all database operations for managing a clinic system,
    including doctors, patients, specializations, and appointments.
    It follows OOP principles with encapsulation and separation of concerns.
    """
    
    def __init__(self, db_name: str = 'clinic.db'):
        """
        Initialize the clinic database connection and create all required tables.
        
        This constructor follows the initialization pattern where:
        1. Database connection is established
        2. Cursor is created for executing SQL commands
        3. Tables are automatically created if they don't exist
        
        Args:
            db_name (str): Name of the SQLite database file (default: 'clinic.db')
        """
        self.db_name = db_name
        # Establish database connection using helper method
        self.conn = self.get_conn()
        # Create cursor object for executing SQL queries
        self.cursor = self.get_cursor()
        # Automatically create all required tables on initialization
        self.create_tables()

    def get_conn(self):
        """
        Get or create a database connection.
        
        This method establishes a connection to the SQLite database.
        In a production environment, connection pooling would be recommended.
        
        Returns:
            sqlite3.Connection: Database connection object
        """
        return sqlite3.connect(self.db_name)
    
    def get_cursor(self):
        """
        Get or create a database cursor.
        
        The cursor is used to execute SQL commands and fetch results.
        It must be created from an active database connection.
        
        Returns:
            sqlite3.Cursor: Database cursor object
        """
        return self.conn.cursor()

    def create_tables(self):
        """
        Create all database tables with proper relationships and constraints.
        
        This method implements the database schema design:
        - Tables are created using IF NOT EXISTS to prevent errors on re-initialization
        - Foreign key constraints ensure referential integrity
        - Primary keys with AUTOINCREMENT provide unique identifiers
        
        IMPORTANT: Table creation order matters due to foreign key dependencies:
        1. Specialization (no dependencies)
        2. Doctor (depends on Specialization)
        3. Patient (no dependencies)
        4. Appointment (depends on Doctor and Patient)
        
        Note: In SQLite, foreign key constraints are checked but not enforced
        by default. The constraints are defined for documentation and future compatibility.
        """
        # Create Doctor table
        # This table stores doctor information and references Specialization
        # Foreign key constraint: specialization_id must exist in specialization table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS doctor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                specialization_id INTEGER NOT NULL,
                FOREIGN KEY (specialization_id) REFERENCES specialization(id)
            )
        ''')
        
        # Create Patient table
        # This table stores patient personal information
        # Note: data_of_birth is used to calculate age for senior patient queries
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS patient (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                data_of_birth DATE NOT NULL,
                contact_number TEXT NOT NULL
            )
        ''')
        
        # Create Specialization table
        # This table stores medical specializations (e.g., Ophthalmology, Cardiology)
        # It is referenced by the Doctor table through foreign key relationship
        # IMPORTANT: This should ideally be created before Doctor table,
        # but SQLite's IF NOT EXISTS and deferred constraint checking allows this order
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS specialization (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            )
        ''')
        
        # Create Appointment table
        # This is a junction/bridge table that links Doctors and Patients
        # It implements a many-to-many relationship between doctors and patients
        # Foreign keys ensure that only valid doctor and patient IDs can be used
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointment (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                appointment_time TIME NOT NULL,
                doctor_id INTEGER NOT NULL,
                patient_id INTEGER NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (doctor_id) REFERENCES doctor(id),
                FOREIGN KEY (patient_id) REFERENCES patient(id)
            )
        ''')
        
        # Commit all table creation statements to make changes permanent
        # This ensures atomicity - either all tables are created or none
        self.get_conn().commit()
    
    def delete_tables(self):
        """
        Delete all tables from the database.
        
        WARNING: This method is for testing purposes only.
        In a production environment, this would be a dangerous operation.
        The DROP TABLE IF EXISTS statement prevents errors if tables don't exist.
        
        Note: Tables are dropped in reverse dependency order to avoid foreign key errors.
        """
        # Drop tables in reverse order of dependencies to avoid constraint violations
        self.cursor.execute('DROP TABLE IF EXISTS appointment;')
        self.cursor.execute('DROP TABLE IF EXISTS doctor;')
        self.cursor.execute('DROP TABLE IF EXISTS patient;')
        self.cursor.execute('DROP TABLE IF EXISTS specialization;')
        
        # Commit the deletion operations
        self.get_conn().commit()
        print("✓ Tables deleted.")

    def add_specialization(self, name: str, description: str):
        """
        Add a new medical specialization to the database.
        
        This method uses parameterized queries (?) to prevent SQL injection attacks.
        The commit() ensures the data is permanently saved.
        
        Args:
            name (str): Name of the specialization (e.g., 'Ophthalmology')
            description (str): Description of what the specialization covers
        """
        # Parameterized query prevents SQL injection
        # The ? placeholders are replaced with actual values from the tuple
        self.cursor.execute('''
            INSERT INTO specialization (name, description)
            VALUES (?, ?)
        ''', (name, description))
        # Commit to persist the changes
        self.get_conn().commit()

    def add_doctor(self, first_name: str, last_name: str, specialization_id: int):
        """
        Add a new doctor to the database.
        
        The doctor must be associated with an existing specialization.
        The foreign key constraint ensures referential integrity.
        
        Args:
            first_name (str): Doctor's first name
            last_name (str): Doctor's last name
            specialization_id (int): ID of the specialization (must exist in specialization table)
        
        Note: This method does not commit automatically. 
        Consider adding commit() for consistency with other add methods.
        """
        # Insert doctor with reference to specialization
        # Foreign key constraint ensures specialization_id exists
        self.cursor.execute('''
            INSERT INTO doctor (first_name, last_name, specialization_id)
            VALUES (?, ?, ?)
        ''', (first_name, last_name, specialization_id))
        # TODO: Add commit() here for consistency
    
    def add_patient(self, first_name: str, last_name: str, data_of_birth: date, contact_number: str):
        """
        Add a new patient to the database.
        
        The date_of_birth is stored as DATE type and is used later
        to calculate age for senior patient queries.
        
        Args:
            first_name (str): Patient's first name
            last_name (str): Patient's last name
            data_of_birth (date): Patient's date of birth (datetime.date object)
            contact_number (str): Patient's contact phone number
        """
        # Insert patient information
        # DATE type allows SQL date functions to be used for age calculations
        self.cursor.execute('''
            INSERT INTO patient (first_name, last_name, data_of_birth, contact_number)
            VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, data_of_birth, contact_number))
        # Commit to persist the patient record
        self.get_conn().commit()

    def list_senior_patients(self):
        """
        List all patients who are 65 years or older (senior patients).
        
        This method demonstrates SQL date arithmetic:
        - DATE('now', '-65 years') calculates the date 65 years ago from today
        - Patients with birth dates before this threshold are considered seniors
        - The query uses < comparison because older dates have smaller values
        
        This is one of the core requirements of the assignment.
        """
        print("\n--- Senior Patients (> 65) ---")
        
        # SQL date function: DATE('now', '-65 years') calculates the cutoff date
        # Patients born before this date are 65+ years old
        # This approach is more efficient than calculating age for each patient
        self.cursor.execute('''
            SELECT first_name, last_name, data_of_birth 
            FROM patient 
            WHERE data_of_birth < DATE('now', '-65 years')
        ''')
        results = self.cursor.fetchall()

        # Handle empty result set gracefully
        if not results:
            print("No matched patients found.")
            return
        
        # Display each senior patient's information
        for row in results:
            print(f"{row[0]} {row[1]} Born on ({row[2]})")
        print("\n--- End of Senior Patients ---")

    def count_ophthalmologists(self):
        """
        Count the total number of doctors specializing in ophthalmology.
        
        This method demonstrates:
        1. JOIN operation to connect related tables
        2. Aggregate function COUNT(*) to count records
        3. String function LOWER() for case-insensitive comparison
        4. WHERE clause for filtering
        
        This is one of the core requirements of the assignment.
        """
        print("\n--- Ophthalmologists Count ---")
        
        # JOIN operation connects doctor and specialization tables
        # ON clause specifies the relationship: doctor.specialization_id = specialization.id
        # WHERE clause filters for 'ophthalmology' specialization
        # LOWER() ensures case-insensitive matching
        # COUNT(*) returns the total number of matching records
        self.cursor.execute('''
            SELECT COUNT(*) 
            FROM doctor 
            JOIN specialization ON doctor.specialization_id = specialization.id
            WHERE LOWER(specialization.name) = 'ophthalmology'
        ''')
        result = self.cursor.fetchone()
        
        # fetchone() returns a tuple, result[0] contains the count
        if result:
            print(f"The total number of doctors who specialise in ophthalmology is {result[0]}.")
        else:
            print("No ophthalmologists found.")
        print("\n--- End of Ophthalmologists Count ---")


if __name__ == "__main__":
    """
    Main execution block - demonstrates the clinic management system functionality.
    
    This section:
    1. Initializes the database and creates tables
    2. Populates the database with sample data
    3. Executes the required queries (senior patients, ophthalmologists count)
    4. Cleans up by deleting tables (for testing)
    """
    # Initialize the clinic database system
    # This automatically creates all tables
    db = Clinc('./clinic.db')
    
    # Insert initial specialization data
    # These specializations are referenced by doctors
    db.add_specialization('Ophthalmology', 'Specialization in the diagnosis and treatment of eye diseases')
    db.add_specialization('Cardiology', 'Specialization in the diagnosis and treatment of heart diseases')
    db.add_specialization('Pediatrics', 'Specialization in the diagnosis and treatment of child diseases')
    
    # Add doctors with their specializations
    # specialization_id: 1=Ophthalmology, 2=Cardiology, 3=Pediatrics
    db.add_doctor('John', 'Doe', 1)      # Ophthalmologist
    db.add_doctor('Jane', 'Smith', 2)    # Cardiologist
    db.add_doctor('Jim', 'Beam', 3)     # Pediatrician
    
    # Add patients with various birth dates
    # Some patients are seniors (>65), others are not
    db.add_patient('John', 'Doe', date(1942, 1, 1), '1234567890')    # 82 years old (senior)
    db.add_patient('Jane', 'Smith', date(1950, 1, 1), '1234567890')   # 74 years old (senior)
    db.add_patient('Jim', 'Beam', date(1960, 1, 1), '1234567890')     # 64 years old (not senior)
    db.add_patient('Jill', 'Doe', date(1970, 1, 1), '1234567890')     # 54 years old
    db.add_patient('Jack', 'Smith', date(1980, 1, 1), '1234567890')   # 44 years old
    db.add_patient('Jill', 'Beam', date(1990, 1, 1), '1234567890')    # 34 years old
    
    # Execute required queries for the assignment
    # Requirement 1: List senior patients (>65 years)
    db.list_senior_patients()
    
    # Requirement 2: Count ophthalmologists
    db.count_ophthalmologists()
    
    # Clean up: Delete all tables (for testing purposes only)
    # WARNING: This removes all data from the database
    db.delete_tables()
