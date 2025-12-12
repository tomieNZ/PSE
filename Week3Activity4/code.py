import sqlite3

class YooBee:
    """A class to manage a simple university database (Students, Teachers, Courses) using SQLite."""

    def __init__(self, database_name: str) -> None:
        """Initializes the database connection and cursor."""
        self.database_name = database_name
        self._conn = None  # Private attribute for database connection
        self._cursor = None  # Private attribute for database cursor
        try:
            # Establish a connection to the SQLite database
            self._conn = sqlite3.connect(database_name)
            # Set the row_factory to sqlite3.Row for dictionary-like access to rows
            self._conn.row_factory = sqlite3.Row
            # Create a cursor object to execute SQL commands
            self._cursor = self._conn.cursor()
            print(f"✓ Connected to database: {self.database_name}")
            # Automatically create tables when an instance is initialized
            self._create_tables()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            # Ensure connection is closed if an error occurs during init
            if self._conn:
                self._conn.close()
                self._conn = None
                self._cursor = None
    # Attention: __enter__ will runing when 'with' block start
    def __enter__(self):
        """Enables the use of 'with' statement for resource management."""
        return self
    # Attention: __exit__ will runing when 'with' block done
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensures the database connection is closed when exiting the 'with' block."""
        self.close()

    # A wrap function to query everything
    def _execute_query(self, query: str, params=None, commit=False):
        """A helper method to execute SQL queries with error handling."""
        if not self._conn or not self._cursor:
            print("Error: Database connection is not active.")
            return None
        try:
            if params:
                self._cursor.execute(query, params)
            else:
                self._cursor.execute(query)
            if commit:
                #- COMMIT = Save your changes permanently to the database
                # Like clicking the "Save" button in Microsoft Word
                self._conn.commit()
            return self._cursor # Return the cursor itself on success
        # handle error when duplicate entries
        except sqlite3.IntegrityError as e:
            print(f"Integrity error: {e}. Check for duplicate entries or foreign key constraints.")
            return None # Return None on error
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None # Return None on error

    def _create_tables(self):
        """Creates Students, Teachers, and Courses tables if they do not exist."""
        # Create Students table
        # id is the primary key
        # Primary Key is a unique identifier for each row in a table
        # It helps the database find and identify each record quickly
        # we can set it AUTOINCREMENT means everytime increase a record id will generate automatically
        # use SQL like IF NOT EXISTS means only working when the table is not exist
        self._execute_query('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL,
            email VARCHAR UNIQUE NOT NULL
        )
        ''')
        # Create Teachers table
        #Attention: email will be set as UNIQUE, since every teacher only submit one unique email
        self._execute_query('''
        CREATE TABLE IF NOT EXISTS Teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL,
            email VARCHAR UNIQUE NOT NULL
        )
        ''')
        # Create Courses table with foreign keys
        # Attention: we will set two FOREIGN KEY in this table
        # A FOREIGN KEY will connect different tables, for instance, every teacher_id must point to a id in teachers table
        # It also means you cant delete data if the data connect to another table
        self._execute_query('''
        CREATE TABLE IF NOT EXISTS Courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code VARCHAR NOT NULL,
            name VARCHAR NOT NULL,
            teacher_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES Teachers(id),
            FOREIGN KEY (student_id) REFERENCES Students(id)
        )
        ''')
        print("✓ Tables created (if not already existing).")

    def insert_initial_data(self):
        """Inserts predefined initial data into the tables."""
        # Sample student data
        students_data = [
            ('Zhang Wei', 'zhang@example.com'),
            ('Alice Smith', 'alice@example.com'),
            ('Bob Johnson', 'bob@example.com'),
            ('Carol Lee', 'carol@example.com'),
            ('David Brown', 'david@example.com')
        ]
        # Insert students data
        cursor_students_count = self._execute_query('SELECT COUNT(*) FROM Students')
        if cursor_students_count and cursor_students_count.fetchone()[0] == 0:
            self._cursor.executemany('''
            INSERT INTO Students (name, email)
            VALUES (?, ?)
            ''', students_data)
            self._conn.commit()
            print(f"✓ Inserted {len(students_data)} initial students.")
        else:
            print("Students table already has data, skipping initial student insert.")

        # Sample teacher data
        teachers_data = [
            ('Teacher Wei', 'Teacherzhang@example.com'),
            ('Teacher Smith', 'Teacheralice@example.com'),
            ('Teacher Johnson', 'Teacherbob@example.com'),
            ('Teacher Lee', 'Teachercarol@example.com'),
            ('Teacher Brown', 'Teacherdavid@example.com')
        ]
        # Insert teachers data
        cursor_teachers_count = self._execute_query('SELECT COUNT(*) FROM Teachers')
        if cursor_teachers_count and cursor_teachers_count.fetchone()[0] == 0:
            self._cursor.executemany('''
            INSERT INTO Teachers (name, email)
            VALUES (?, ?)
            ''', teachers_data)
            self._conn.commit()
            print(f"✓ Inserted {len(teachers_data)} initial teachers.")
        else:
            print("Teachers table already has data, skipping initial teacher insert.")

        # Sample course data (linking student and teacher IDs)
        courses_data = [
            ('MSE802', 'Quantum computing', 1, 1), # Student 1, Teacher 1
            ('MSE800', 'Professional software engineering', 2, 2),
            ('MSE802', 'Quantum computing', 2, 2),
            ('MSE802', 'Quantum computing', 3, 3),
            ('MSE802', 'Quantum computing', 4, 1),
            ('MSE800', 'Professional software engineering', 4, 1),
        ]
        # Insert courses data
        cursor_courses_count = self._execute_query('SELECT COUNT(*) FROM Courses')
        if cursor_courses_count and cursor_courses_count.fetchone()[0] == 0:
            self._cursor.executemany('''
            INSERT INTO Courses (code, name, teacher_id, student_id)
            VALUES (?, ?, ?, ?)
            ''', courses_data)
            self._conn.commit()
            print(f"✓ Inserted {len(courses_data)} initial courses.")
        else:
            print("Courses table already has data, skipping initial course insert.")

    def add_student(self, name: str, email: str) -> bool:
        """Adds a new student to the Students table."""
        query = "INSERT INTO Students (name, email) VALUES (?, ?)"
        result = self._execute_query(query, (name, email), commit=True)
        return True if result else False # Return boolean based on whether cursor was returned

    def add_teacher(self, name: str, email: str) -> bool:
        """Adds a new teacher to the Teachers table."""
        query = "INSERT INTO Teachers (name, email) VALUES (?, ?)"
        result = self._execute_query(query, (name, email), commit=True)
        return True if result else False # Return boolean based on whether cursor was returned

    def add_course(self, code: str, name: str, teacher_id: int, student_id: int) -> bool:
        """Adds a new course enrollment to the Courses table."""
        query = "INSERT INTO Courses (code, name, teacher_id, student_id) VALUES (?, ?, ?, ?)"
        result = self._execute_query(query, (code, name, teacher_id, student_id), commit=True)
        return True if result else False # Return boolean based on whether cursor was returned

    def get_students_count_for_course(self, course_code: str) -> int:
        """Returns the number of students enrolled in a specific course."""
        query = "SELECT COUNT(DISTINCT student_id) FROM Courses WHERE code=?"
        # Fetch one result, which is the count
        cursor_result = self._execute_query(query, (course_code,))
        if cursor_result:
            return cursor_result.fetchone()[0]
        return 0

    def get_teachers_for_course(self, course_code: str) -> list:
        #- SELECT T.name: "I want to see the names from the Teachers table."
        #- FROM Teachers AS T: "Look in the Teachers table (let's call it T for short)."
        #- JOIN Courses AS C ON T.id = C.teacher_id: "And also look in the Courses table (let's call it C), connecting them where the Teacher's ID in the Teachers table matches the teacher_id in the Courses table."
        #- WHERE C.code = 'MSE802': "But only show me the teachers whose courses have the code 'MSE802'."
        """Returns a list of teacher names teaching a specific course."""
        query = """
        SELECT DISTINCT T.name
        FROM Teachers AS T
        JOIN Courses AS C ON T.id = C.teacher_id
        WHERE C.code = ?
        """
        cursor_result = self._execute_query(query, (course_code,))
        if cursor_result:
            # Fetch all matching teacher names and return as a list of strings
            return [row['name'] for row in cursor_result.fetchall()]
        return []

    def close(self):
        """Closes the database connection."""
        #only work when conn is not close
        if self._conn:
            self._conn.close()
            # reset conn and cursor
            self._conn = None
            self._cursor = None
            print("✓ Database connection closed.")

if __name__ == "__main__":
    # Using the YooBee class as a context manager to ensure proper connection handling
    with YooBee('database.db') as db_manager:
        # Insert initial data (this will only run if tables are empty)
        db_manager.insert_initial_data()

        # Get and print the number of students for 'MSE800' course
        mse800_students_count = db_manager.get_students_count_for_course('MSE800')
        print('-'*30)
        print(f'There are {mse800_students_count} students taking MSE800.')
        print('-'*30)
        # Get and print the names of teachers teaching 'MSE802'
        mse802_teacher_names = db_manager.get_teachers_for_course('MSE802')
        print('-'*30)
        print(f"Teachers for MSE802 are: {', '.join(mse802_teacher_names)}.")
        print('-'*30)
        # Example of adding new data
        # db_manager.add_student('New Student', 'new@example.com')
        # db_manager.add_teacher('New Teacher', 'newteacher@example.com')
        # db_manager.add_course('MSE803', 'Database Systems', 2, 4)