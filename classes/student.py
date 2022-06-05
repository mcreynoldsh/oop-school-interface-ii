from classes.person import Person
import csv

class Student(Person):
    student_list=[]
    def __init__(self, name, age, role, school_id, password):
        parent_instance= super()
        parent_instance.__init__(name,age,role,school_id,password)
    
    def __str__(self):
        return f"""
        {self.name.upper()}
        ---------------
        age: {self.age}
        id: {self.id}"""

    def all_students():
        student_list=[]
        with open("/Users/huntermcreynolds/code/exercises/Week2/oop-school-interface-i/data/students.csv") as f :
            student_reader = csv.DictReader(f,skipinitialspace=True)
            for row in student_reader:
                student_list.append(Student(**dict(row)))
            return student_list    


              