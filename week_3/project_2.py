print("Welcome!! This is a programme to determine your Annual Tax Rvenue (ATR)")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
expe = int(input("Enter your years of work experience: "))
print("\n")
if age >= 55 and expe > 25:
    print(name +" Your ATR is N5,600,000.\nTHANK YOU!")
elif age >= 45 and expe > 20:
    print(name +" Your Annual ATR is 4,480,000.\nTHANK YOU!")
elif age >= 35 and expe > 10:
    print(name +" Your Annual ATR is 1,500.000.\nTHANK YOU!")
elif age < 35 and expe < 10:
    print(name +" Your Annual ATR is 550.000.\nTHANK YOU!")

else:
    print("Incorrect Entry")