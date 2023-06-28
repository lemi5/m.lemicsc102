import random

class employee:
    a1 = "Mary Evans"
    a2 = "Eyo Ishan"
    a3 = "Durojaiye Dare"
    a4 = "Adams Ali"
    a5 = "Adams Ali"
    a6 = "Stella Mankinde"
    a7 = "Jane Akibo"
    a8 = "Ago James"
    a9 = "Michell Taiwo"
    a10 = "Abraham Jones"
    a11 = "Nicole Anide"
    a12 = "Kosi Korse"
    a13 = "Adele Martins"
    a14 = "Emmanuel ojo"
    a15 = "Ajayi Fatima"
    t1 = ["Loading", "Transporting", "Reviewing orders", "Customer service", "Delivering Items"]


    def __init__(self, name):
        self.name = name

    def check_employee(self):
        if done.name == done.a1 or done.name == done.a2 or done.name == done.a3 or done.name == done.a4 or done.name == done.a5\
                or done.name == done.a6 or done.name == done.a7 or done.name == done.a8 or done.name == done.a9 or done.name == done.a10\
                or done.name == done.a11 or done.name == done.a12 or done.name == done.a12 or done.name == done.a14 or done.name == done.a15:
            print("{} is a staff of this company ".format(self.name))
        else:
            print("Sorry you are not a staff of this company")

    def take_attendance(self):
        if done.name == done.a1 or done.name == done.a2 or done.name == done.a3 or done.name == done.a4 or done.name == done.a5 \
                or done.name == done.a6 or done.name == done.a7 or done.name == done.a8 or done.name == done.a9 or done.name == done.a10 \
                or done.name == done.a11 or done.name == done.a12 or done.name == done.a12 or done.name == done.a14 or done.name == done.a15:
            print("Your Attedance has been taken sucessfully")

    def assign_task(self):
        if done.name == done.a1 or done.name == done.a2 or done.name == done.a3 or done.name == done.a4 or done.name == done.a5 \
                or done.name == done.a6 or done.name == done.a7 or done.name == done.a8 or done.name == done.a9 or done.name == done.a10 \
                or done.name == done.a11 or done.name == done.a12 or done.name == done.a12 or done.name == done.a14 or done.name == done.a15:
            print("Your task for the day is {}".format(random.choice(done.t1)))


done = employee(input("Eter your name: "))
done.check_employee()
done.take_attendance()
done.assign_task()
