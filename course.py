class Course:
    _id_counter = 1    #علشان نقول للمبرمجين "ما تعدلوش المتغير ده من بره".

    def __init__(self, name:str):
            self.course_id = Course._id_counter
            Course._id_counter += 1
            self.name = name
            self.enrolled_students = []

    def __str__(self):
        return f"Course ID: {self.course_id}, Course_Name: {self.name}, Enrolled Students: {len(self.enrolled_students)}"
    
    def enroll_student(self, student_id:int):
        """
        Enrolls a student in the course.
        param_1 : take the student_id as an int 
        param_1_type : int
        return: None
        """
        if student_id not in self.enrolled_students:
            self.enrolled_students.append(student_id)
        else:
            print(f"Student {student_id} is already enrolled in this course.")

    def remove_student(self, student_id:int):
        """
        Removes a student from the course.
        param_1 : take the student_id as an int 
        param_1_type : int
        return: None
        """
        for course in self.Courses.values():
            if student_id in course.enrolled_students:
                course.enrolled_students.remove(student_id)
               
