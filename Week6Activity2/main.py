"""
This file is used to demonstrate the StudentDatabase class with SQLite3.
@author: Yaohui Zhang @tomie
Date: 2026-01-24
"""
import sqlite3
from datetime import datetime


class StudentDatabase:
    """Student database management class - using SQLite3 for persistent storage"""

    def __init__(self, db_path="students.db"):
        """Initialize database connection and create table"""
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Create students table if not exists"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                student_name TEXT NOT NULL,
                score INTEGER NOT NULL,
                created_date TEXT NOT NULL,
                passed INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def add_student(self, student_id, name, score):
        """
        Add student record to database
        Auto-calculate passed field and created_date
        """
        if student_id is None or name is None or score is None:
            raise ValueError("student_id, name and score cannot be None")

        # Auto-calculate pass status
        passed = 1 if score >= 50 else 0
        created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insert or replace record
        self.cursor.execute('''
            INSERT OR REPLACE INTO students 
            (student_id, student_name, score, created_date, passed)
            VALUES (?, ?, ?, ?, ?)
        ''', (student_id, name, score, created_date, passed))
        self.conn.commit()

    def get_passed_students(self):
        """
        Query all passed students
        Returns: {student_id: {"name": name, "score": score}}
        """
        self.cursor.execute('''
            SELECT student_id, student_name, score 
            FROM students 
            WHERE passed = 1
        ''')
        rows = self.cursor.fetchall()

        result = {}
        for row in rows:
            result[row[0]] = {
                "name": row[1],
                "score": row[2]
            }
        return result

    def get_top_students(self, n=3):
        """
        Query top N students (ordered by score descending)
        Returns: [(student_id, student_name, score), ...]
        """
        self.cursor.execute('''
            SELECT student_id, student_name, score 
            FROM students 
            ORDER BY score DESC 
            LIMIT ?
        ''', (n,))
        return self.cursor.fetchall()

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    # Create database instance
    db = StudentDatabase()

    # Add 5 student records
    db.add_student("S001", "tomie1", 85)
    db.add_student("S002", "tomie2", 45)
    db.add_student("S003", "tomie3", 72)
    db.add_student("S004", "tomie4", 38)
    db.add_student("S005", "tomie5", 90)

    # Query passed students
    print("\nPassed Students:\n", db.get_passed_students())

    # Query Top 3 students
    print("\nTop 3 Students:\n", db.get_top_students(3))

    # Close database connection
    db.close()
