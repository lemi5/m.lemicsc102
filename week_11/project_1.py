# week13
# Import the pandas library
import pandas as pd

# Create an empty list that will contain the student info
student_info = []
filename = "PAU_SMIS.csv"


class SMIS():
    def __init__(self, name, matric, depertment, level):
        self.name = name
        self.matric = matric
        self.depertment = depertment
        self.level = level

    # This method creates the file
    def create_file(self):
        data = {"Student Name": self.name, "Matric. Number": self.matric, "Depertment": self.depertment,
                "Level": self.level}
        student_info.append(data)

        df = pd.DataFrame(student_info)
        df.to_csv(filename)
        print(df)


student_frequency = int(input("Input the number of students: "))

for i in range(student_frequency):
    name = input("Input your fullname: ")
    matric = input("Input your matriculation number: ")
    depertment = input("What depertment are you in? ")
    level = input("What level are you in? ")
    obj = SMIS(name, matric, depertment, level)
    obj.create_file()