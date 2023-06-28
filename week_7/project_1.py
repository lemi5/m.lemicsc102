# Project 1
# import the random module
import random


# create a class called Employee
class Employee():

    # create a parameterized constructor
    def __init__(self, name, attendance):
        self.name = name
        self.attendance = attendance

    def check_employee(self):
        employees = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", \
                     "Andrew Ugwu", "Stella Mankinde", "Jane Akibo", "Ago James", \
                     "Michell Taiwo", "Abraham Jones", "Nicole Anide", "Kosi Korso", \
                     "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"]
        if name in employees:
            return True
        else:
            return False

    def take_attendance(self):
        if attendance == "yes" or attendance == "Yes":
            return True
        elif attendance == "no" or attendance == "No":
            return False
        else:
            print("Sorry, that is not a correct input.")

    def assign_task(self):
        Tasks = ["Loading", "Transporting", "Reveiwing Orders", \
                 "Customer Service", "Delivering Items"]
        global task
        task = random.choice(Tasks)

    def refuse_access(self):
        print("Sorry, your name is not registered a an employee")


print("Note: this code is case sensitive")
name = input("Input your name: ")
run = Employee(name, attendance)
run.check_employee()

if run.check_employee() == True:
    print(f"Welcome {name}!")
    attendance = input("Are you present?(yes or no): ")
    run.take_attendance()
    if run.take_attendance() == True:
        print("Attendance taken: Present")
        run.assign_task()
        print(f"Your task is {task}.")
    elif run.take_attendance() == False:
        print("Attendance taken: Absent")
        print("Since your attendance says 'Absent', no task is assigned to you.")

else:
    run.refuse_access()

print("Thank you.")