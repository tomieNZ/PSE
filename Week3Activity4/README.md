# YooBee MSE802 Week3 - Activity4

## 📋 Project Overview

This project is an Object-Oriented Programming (OOP) based database management system that uses SQLite database to manage student, teacher, and course information. This project is the fourth activity of Week 3 in the MSE802 course, designed to demonstrate how to build a simple yet complete database application using Python and SQLite.

## 🎯 Project Objectives

- Develop an OOP project to design and manage a database (based on W3-A3)
- Display the number of students for the MSE800 course
- List all teacher names who are teaching MSE802
- Provide complete code comments to demonstrate understanding of the project

## 🗄️ Database Design

### Architecture Overview

This project uses a three-table design: **Students**, **Teachers**, and **Courses**. The Courses table serves both as course information storage and as a bridge table for student-course-teacher relationships. Each row in the Courses table represents a student-course-teacher triplet relationship.

<img src="Design.png">

### Table Structure

#### Table 1: Students

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier for each student |
| name | TEXT | NOT NULL | Full name of the student |
| email | TEXT | UNIQUE NOT NULL | Student email address, must be unique |

#### Table 2: Teachers

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier for each teacher |
| name | TEXT | NOT NULL | Full name of the teacher |
| email | TEXT | UNIQUE NOT NULL | Teacher email address, must be unique |

#### Table 3: Courses

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier for each enrollment record |
| code | TEXT | NOT NULL | Course code identifier (e.g., MSE800, MSE802) |
| name | TEXT | NOT NULL | Full name of the course |
| teacher_id | INTEGER | NOT NULL | Foreign key referencing Teachers table id |
| student_id | INTEGER | NOT NULL | Foreign key referencing Students table id |

**Foreign Key Constraints:**
- `teacher_id` must point to a valid id in the Teachers table
- `student_id` must point to a valid id in the Students table
- Data cannot be deleted if it is linked to other tables

## 🏗️ Technical Architecture

### Core Technology Stack

- **Python 3.x** - Primary programming language
- **SQLite3** - Lightweight relational database
- **Object-Oriented Programming (OOP)** - Code organization approach

### Design Patterns

- **Context Manager Pattern** - Uses `with` statement to ensure proper database connection closure
- **Encapsulation** - Uses private attributes (`_conn`, `_cursor`) to protect database connections
- **Error Handling** - Comprehensive exception handling mechanism

## 📦 Project Structure

```
Week3Activity4/
├── README.md          # Project documentation
└── [Main Program File] # YooBee class implementation file
```

## 🔧 Core Features

### YooBee Class

The `YooBee` class is the core of the entire project, providing complete database management functionality:

#### Main Methods

1. **`__init__(database_name: str)`**
   - Initializes database connection and cursor
   - Automatically creates table structure

2. **`__enter__()` and `__exit__()`**
   - Supports context manager protocol
   - Ensures database connection is properly closed after use

3. **`_create_tables()`**
   - Creates Students, Teachers, and Courses tables
   - Skips creation if tables already exist

4. **`insert_initial_data()`**
   - Inserts predefined initial data
   - Only inserts when tables are empty to avoid duplicate data

5. **`add_student(name: str, email: str) -> bool`**
   - Adds a new student to the Students table

6. **`add_teacher(name: str, email: str) -> bool`**
   - Adds a new teacher to the Teachers table

7. **`add_course(code: str, name: str, teacher_id: int, student_id: int) -> bool`**
   - Adds a new course enrollment record to the Courses table

8. **`get_students_count_for_course(course_code: str) -> int`**
   - Returns the number of students enrolled in a specific course
   - Uses `COUNT(DISTINCT student_id)` to ensure accuracy

9. **`get_teachers_for_course(course_code: str) -> list`**
   - Returns a list of all teacher names teaching a specific course
   - Uses JOIN query to connect Teachers and Courses tables

10. **`close()`**
    - Closes the database connection
    - Resets connection and cursor objects

## 💻 Usage Examples

### Basic Usage

```python
import sqlite3
from yoobee import YooBee  # Assuming main program file is named yoobee.py

# Use context manager to ensure connection is properly closed
with YooBee('database.db') as db_manager:
    # Insert initial data (only executes if tables are empty)
    db_manager.insert_initial_data()
    
    # Query the number of students for MSE800 course
    mse800_students_count = db_manager.get_students_count_for_course('MSE800')
    print(f'There are {mse800_students_count} students taking MSE800.')
    
    # Query teacher names teaching MSE802
    mse802_teacher_names = db_manager.get_teachers_for_course('MSE802')
    print(f"Teachers for MSE802 are: {', '.join(mse802_teacher_names)}.")
    
    # Example of adding new data
    # db_manager.add_student('New Student', 'new@example.com')
    # db_manager.add_teacher('New Teacher', 'newteacher@example.com')
    # db_manager.add_course('MSE803', 'Database Systems', 2, 4)
```

### Expected Output

```
✓ Connected to database: database.db
✓ Tables created (if not already existing).
✓ Inserted 5 initial students.
✓ Inserted 5 initial teachers.
✓ Inserted 3 initial courses.
There are 1 students taking MSE800.
Teachers for MSE802 are: Teacher Wei.
✓ Database connection closed.
```

## 🔍 SQL Query Explanations

### Query MSE800 Student Count

```sql
SELECT COUNT(DISTINCT student_id) 
FROM Courses 
WHERE code='MSE800'
```

### Query MSE802 Teachers (JOIN Query)

```sql
SELECT DISTINCT T.name
FROM Teachers AS T
JOIN Courses AS C ON T.id = C.teacher_id
WHERE C.code = 'MSE802'
```

**Query Explanation:**
- `SELECT T.name`: Select teacher names from the Teachers table
- `FROM Teachers AS T`: Look in the Teachers table (using alias T)
- `JOIN Courses AS C ON T.id = C.teacher_id`: Join the Courses table, matching teacher IDs
- `WHERE C.code = 'MSE802'`: Filter records where course code is MSE802

## 📝 Code Features

### 1. Error Handling

- **Integrity Error Handling**: Catches duplicate entries or foreign key constraint errors
- **Database Error Handling**: Catches general database operation errors
- **Connection Status Check**: Validates connection status before executing queries

### 2. Resource Management

- Uses context manager (`with` statement) to automatically manage database connections
- Ensures connections are properly closed even in exception cases
- Prevents memory leaks and resource waste

### 3. Code Comments

- All methods include detailed docstrings
- Key code lines have inline comments
- Comments explain the logic and purpose of SQL queries

## 🚀 Requirements

### System Requirements

- Python 3.6 or higher
- SQLite3 (Python standard library, no additional installation needed)

### Dependencies

This project only uses Python standard library, no external packages need to be installed:

```python
import sqlite3  # Python standard library
```

## 📚 Learning Points

### Database Concepts

1. **Primary Key**: A field that uniquely identifies each row in a table
2. **Foreign Key**: A field that establishes relationships between tables
3. **AUTOINCREMENT**: Automatically incrementing primary key values
4. **UNIQUE Constraint**: Ensures field values are unique
5. **NOT NULL Constraint**: Ensures fields cannot be empty

### OOP Concepts

1. **Encapsulation**: Uses private attributes to protect internal state
2. **Context Manager**: Implements `__enter__` and `__exit__` methods
3. **Method Design**: Clear method naming and responsibility division
4. **Error Handling**: Comprehensive exception handling mechanism

### SQL Concepts

1. **JOIN Query**: Connects multiple tables for relational queries
2. **DISTINCT**: Removes duplicate results
3. **COUNT**: Counts record numbers
4. **WHERE Clause**: Conditional filtering

## ⚠️ Important Notes

1. **Production Environment Warning**: The test deletion operation (`rm -rf database.db`) in this project is only for development testing. **Never use this in production environments**, as it may cause data loss.

2. **Data Integrity**: Due to foreign key constraints, when deleting data, you must first delete records that depend on that data.

3. **Connection Management**: Always use the `with` statement or manually call the `close()` method to close database connections to avoid resource leaks.

## 👤 Author Information

- **Author**: @tomiezhang
- **GitHub**: [https://github.com/neilzhangpro](https://github.com/neilzhangpro)
- **Project**: Currently developing an AI-based quantitative trading system. If you're interested, please feel free to reach out!

## 📄 License

This project is for educational purposes only, for learning and reference.

## 🔗 Related Resources

- [SQLite Official Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 Module Documentation](https://docs.python.org/3/library/sqlite3.html)
- [Google Colab Original Notebook](https://colab.research.google.com/drive/1jtMLnPUbTrAF5MGEvYJLb420yJ3I5JdO?usp=sharing)

---

**Last Updated**: 2025
