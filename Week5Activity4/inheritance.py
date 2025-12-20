"""
This file is used to demonstrate the inheritance in Python.
I will design a class hierarchy of Person, with the following classes:
- Person (Parent Class)
- Student (inherits from Person)
- Staff (inherits from Person)
- General (inherits from Staff)
- Academic (inherits from Staff)

The Person class will be the parent class, and the other classes will inherit from it.
The Student class will have student_id attribute, and the Staff class will have staff_id and tax_num.
The General class will inherit from Staff and have rate_of_pay attribute.
The Academic class will inherit from Staff and have publications attribute.

@author: Yaohui Zhang (tomie)
Date: 2025-12-21
"""

# Parent class
class Person:
    """
    Base class representing a person.
    Attributes:
        Id: The ID of the person
        name: The name of the person
    """
    def __init__(self, Id, name):
        # Initialize the person with ID and name
        print(f"Person {name} (ID: {Id}) is created!")
        self.Id = Id
        self.name = name


# Student inherits from Person
class Student(Person):
    """
    Child class representing a student.
    Attributes:
        student_id: The student ID
        name: The name of the student (inherited from Person)
        Id: The ID of the person (inherited from Person)
    """
    def __init__(self, Id, name, student_id):
        # Call the parent class constructor using super()
        super().__init__(Id, name)
        # Set the student-specific attribute
        self.student_id = student_id
        print(f"Student {self.name} with student_id {self.student_id} is created!")


# Staff inherits from Person
class Staff(Person):
    """
    Child class representing a staff member.
    Attributes:
        staff_id: The staff ID
        tax_num: The tax number
        Id: The ID of the person (inherited from Person)
        name: The name of the staff (inherited from Person)
    """
    def __init__(self, Id, name, staff_id, tax_num):
        # Call the parent class constructor using super()
        super().__init__(Id, name)
        # Set the staff-specific attributes
        self.staff_id = staff_id
        self.tax_num = tax_num
        print(f"Staff {self.name} with staff_id {self.staff_id} is created!")


# General inherits from Staff (multi-level inheritance)
class General(Staff):
    """
    Child class representing a general staff member.
    Attributes:
        Id: The ID of the person (inherited from Person via Staff)
        rate_of_pay: The rate of pay
        name: The name (inherited from Person via Staff)
        staff_id: The staff ID (inherited from Staff)
        tax_num: The tax number (inherited from Staff)
    """
    def __init__(self, Id, name, staff_id, tax_num, rate_of_pay):
        # Call the parent class constructor using super()
        # This will call Staff.__init__(), which will call Person.__init__()
        super().__init__(Id, name, staff_id, tax_num)
        # Set the general staff-specific attribute
        self.rate_of_pay = rate_of_pay
        print(f"General staff {self.name} with rate of pay {self.rate_of_pay} is created!")


# Academic inherits from Staff (multi-level inheritance)
class Academic(Staff):
    """
    Child class representing an academic staff member.
    Attributes:
        id: The ID of the person (inherited from Person via Staff, note: uses 'id' instead of 'Id')
        publications: The number of publications
        name: The name (inherited from Person via Staff)
        staff_id: The staff ID (inherited from Staff)
        tax_num: The tax number (inherited from Staff)
    """
    def __init__(self, Id, name, staff_id, tax_num, publications):
        # Call the parent class constructor using super()
        # This will call Staff.__init__(), which will call Person.__init__()
        super().__init__(Id, name, staff_id, tax_num)
        # Set the academic staff-specific attribute
        self.publications = publications
        print(f"Academic staff {self.name} with {self.publications} publications is created!")


def main():
    """
    Main function to demonstrate the inheritance hierarchy.
    """
    print("=" * 50)
    print("Demonstrating Person Inheritance Hierarchy")
    print("=" * 50)
    print()
    
    # Create a Student instance
    print("1. Creating a Student:")
    student = Student("P001", "Alice", "S12345")
    print(f"   Student ID: {student.student_id}")
    print(f"   Name: {student.name}")
    print(f"   Person ID: {student.Id}")
    print()
    
    # Create a General Staff instance
    print("2. Creating a General Staff:")
    general = General("P002", "Bob", "ST001", "TX001", 25.50)
    print(f"   Staff ID: {general.staff_id}")
    print(f"   Tax Number: {general.tax_num}")
    print(f"   Rate of Pay: ${general.rate_of_pay}/hour")
    print(f"   Name: {general.name}")
    print(f"   Person ID: {general.Id}")
    print()
    
    # Create an Academic Staff instance
    print("3. Creating an Academic Staff:")
    academic = Academic("P003", "Charlie", "ST002", "TX002", 15)
    print(f"   Staff ID: {academic.staff_id}")
    print(f"   Tax Number: {academic.tax_num}")
    print(f"   Publications: {academic.publications}")
    print(f"   Name: {academic.name}")
    print(f"   Person ID: {academic.Id}")
    print()
    
    print("=" * 50)
    print("Inheritance demonstration complete!")
    print("=" * 50)
    
    # Demonstrate that all classes are instances of Person
    print("\nType checking:")
    print(f"Student is instance of Person: {isinstance(student, Person)}")
    print(f"General is instance of Staff: {isinstance(general, Staff)}")
    print(f"General is instance of Person: {isinstance(general, Person)}")
    print(f"Academic is instance of Staff: {isinstance(academic, Staff)}")
    print(f"Academic is instance of Person: {isinstance(academic, Person)}")


if __name__ == "__main__":
    main()
