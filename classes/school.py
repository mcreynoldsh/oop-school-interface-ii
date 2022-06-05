from classes.student import Student
from classes.staff import Staff
class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students= Student.all_students()
       
    def list_students(self):
        counter = 1
        for student in self.students:
            print(f"{counter}. {student.name} {student.id}")
            counter = counter + 1

    def find_student_by_id(self, id_num):
        
        for student in self.students:
            if student.id == id_num:
                return student
        return "student not found"      
