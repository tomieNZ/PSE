# YooBee MSE802 Week3 - Activity4

## Project Overview

An Object-Oriented Programming (OOP) based database management system using SQLite to manage student, teacher, and course information. This project demonstrates building a database application with Python and SQLite.

## Objectives

- Design and manage a database using OOP principles
- Display the number of students enrolled in MSE800 course
- List all teachers teaching MSE802 course

## Database Design

This project uses a three-table design: **Students**, **Teachers**, and **Courses**. The Courses table serves as both course information storage and a bridge table for student-course-teacher relationships.

<img src="Design.png">

### Table Structure

#### Students

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier |
| name | TEXT | NOT NULL | Student full name |
| email | TEXT | UNIQUE NOT NULL | Student email address |

#### Teachers

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier |
| name | TEXT | NOT NULL | Teacher full name |
| email | TEXT | UNIQUE NOT NULL | Teacher email address |

#### Courses

| Field Name | Data Type | Constraints | Description |
|------------|-----------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier |
| code | TEXT | NOT NULL | Course code (e.g., MSE800, MSE802) |
| name | TEXT | NOT NULL | Course full name |
| teacher_id | INTEGER | NOT NULL | Foreign key to Teachers.id |
| student_id | INTEGER | NOT NULL | Foreign key to Students.id |

## YooBee Class

The `YooBee` class provides database management functionality with the following methods:

- `__init__(database_name: str)` - Initializes connection and creates tables
- `__enter__()` / `__exit__()` - Context manager support
- `insert_initial_data()` - Inserts sample data (only if tables are empty)
- `add_student(name: str, email: str) -> bool` - Adds a new student
- `add_teacher(name: str, email: str) -> bool` - Adds a new teacher
- `add_course(code: str, name: str, teacher_id: int, student_id: int) -> bool` - Adds a course enrollment
- `get_students_count_for_course(course_code: str) -> int` - Returns student count for a course
- `get_teachers_for_course(course_code: str) -> list` - Returns list of teacher names for a course
- `close()` - Closes database connection

## Usage

```python
from yoobee import YooBee

with YooBee('database.db') as db:
    # Insert initial data
    db.insert_initial_data()
    
    # Query MSE800 student count
    count = db.get_students_count_for_course('MSE800')
    print(f'There are {count} students taking MSE800.')
    
    # Query MSE802 teachers
    teachers = db.get_teachers_for_course('MSE802')
    print(f"Teachers for MSE802: {', '.join(teachers)}")
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

## Requirements

- Python 3.6+
- SQLite3 (included in Python standard library)

No external dependencies required.

## Author

- **Author**: @tomiezhang
- **GitHub**: [https://github.com/neilzhangpro](https://github.com/neilzhangpro)
