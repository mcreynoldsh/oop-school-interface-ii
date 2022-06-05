from classes.person import Person
import csv

class Staff(Person):
    staff_list=[]
    def __init__(self, name, age, role, employee_id, password):
        parent_instance= super()
        parent_instance.__init__(name,age,role,employee_id,password)

    def all_staff():
        staff_list=[]
        with open('/Users/huntermcreynolds/code/exercises/Week2/oop-school-interface-i/data/staff.csv') as f :
            staff_reader = csv.DictReader(f,skipinitialspace=True)
            for row in staff_reader:
                staff_list.append(row)
            return staff_list       