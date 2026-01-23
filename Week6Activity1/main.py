"""
This file is used to demonstrate the StudentDatabase class.
@author: Yaohui Zhang @tomie
Date: 2026-01-24
"""
class StudentDatabase:

    def __init__(self):
        self.students = {}
        self.mse800_scores = {}
        self.result_list = {}

    def add_student(self, ID, name):
        if ID is None or name is None:
            raise ValueError("ID and name cannot be None")
        self.students[ID] = name
    
    def add_mse800_score(self, ID, score):
        if ID is None or score is None:
            raise ValueError("ID and score cannot be None")
        self.mse800_scores[ID] = score
    
    def JoinAndCompare(self):
        # Combine students and scores where score >= 50
        merged = {**self.students, **self.mse800_scores}
        for ID, score in merged.items():
            if score >= 50:
                self.result_list[ID] = {
                    "name": self.students[ID],
                    "score": score
                }
        return self.result_list

if __name__ == "__main__":
    db = StudentDatabase()
    db.add_student("1234567890", "tomie1")
    db.add_student("1234567891", "tomie2")
    db.add_student("1234567892", "tomie3")
    db.add_mse800_score("1234567890", 50)
    db.add_mse800_score("1234567891", 40)
    db.add_mse800_score("1234567892", 30)
    print(db.JoinAndCompare())