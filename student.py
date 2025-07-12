"""
this class is used to control the degree of each student
"""
class Student:
    _id_counter = 1    #علشان نقول للمبرمجين "ما تعدلوش المتغير ده من بره".

    def __init__(self, name):
        self.student_id = Student._id_counter
        Student._id_counter += 1
        self.name = name
        self.grades = {}
        self.enrolled_courses = []

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Enrolled Courses: {', '.join(self.enrolled_courses)}, Grades: {self.grades}  "

    def add_grade(self, course_id:str, grade:int):
        """
        Adds a grade for a specific course.
        param_1 : take the course_id as a string 
        param_1_type : str
        param_2 : take the grade as a float , float type
        param_2_type : float
        return: None
        """
        self.grades[course_id] = grade

    def enroll_in_course(self, course:str):
        """
        Enrolls the student in a course.
        param_1 : take the course_id as a string 
        param_1_type : str
        return: None
        """
        self.enrolled_courses.append(course)