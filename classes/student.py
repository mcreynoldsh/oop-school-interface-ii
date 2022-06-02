from classes.person import Person
import csv

class Student(Person):
    student_list=[]
    def __init__(self, name, age, role, school_id, password):
        parent_instance= super()
        parent_instance.__init__(name,age,role,school_id,password)

    def all_students():
        student_list=[]
        with open('/Users/huntermcreynolds/code/exercises/oop-school-interface-i/data/students.csv') as f :
            student_reader = csv.DictReader(f,skipinitialspace=True)
            for row in student_reader:
                student_list.append(row)
            return student_list    


              