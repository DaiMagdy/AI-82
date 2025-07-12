from system import SysemManager

"""
SystemManager class to manage students and courses in an educational system.
It allows adding and removing students and courses, enrolling students in courses,
recording grades, and searching for courses by name.
"""

def show_menu():
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Add Course")
    print("4. Remove Course")
    print("5. Enroll Student in Course")
    print("6. Record Grade")
    print("7. Search Course by Name")
    print("8. Exit")