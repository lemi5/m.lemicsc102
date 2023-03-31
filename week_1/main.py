# Program to calculate Simple interest, Compound interest
# and Annuity plan

def simple_interest():
    P = float(input("Input Price: "))
    R = float(input("Input Rate: "))
    T = float(input("Input Period: "))
    S = (1 + R/100)*T
    A = P * S
    print("Your Answer is: ")
    print(A)

def compound_interest():
    P = float(input("Input Price: "))
    R = float(input("Input Rate: "))
    t = float(input("Input Period: "))
    n = float(input("Input number of years: "))
    S = P * (1 + R/n)
    W = n * t
    A = pow(S, W)
    print("Your Answer is: ")
    print(A)

def annuity_plan():
    PMT = float(input("Input PMT: "))
    t = float(input("Input Period: "))
    R = float(input("Input Rate: "))
    n = float(input("Input number of years: "))
    S = (1 + R/n)
    W = n * t
    Q = pow(S, W)
    E = Q - 1
    U = R/n
    O = E / U
    A = PMT * O

    print("Your Answer is: ")
    print(A)
def call():
    print("PROGRAM TO CACULATE\nSIMPLE INTEREST--(SI)\nCOMPOUND INTEREST..(CI)\nANNUITY PLAN..(AP).")
    input1 = input("Please pick from the list above\nwhich operation you would like to perform\n: ")
    if input1 == "SI":
        print(simple_interest())
    elif input1 == "CI":
        print(compound_interest())
    elif input1 == "AP":
        print(annuity_plan())
    else:
        print("Invalid input")
    input2 = input("Do you wish to perform futher operations?\nYES/NO: ")
    if input2 == "YES":
        print(cal())
    else:
        print("OK BYE FOR NOW!!")


def cal():
    print("PROGRAM TO CACULATE\nSIMPLE INTEREST--(SI)\nCOMPOUND INTEREST..(CI)\nANNUITY PLAN..(AP).")
    input1 = input("Please pick from the list above\nwhich operation you would like to perform\n: ")
    if input1 == "SI":
        print(simple_interest())
    elif input1 == "CI":
        print(compound_interest())
    elif input1 == "AP":
        print(annuity_plan())
    else:
        print("Invalid input")
    input2 = input("Do you wish to perform futher operations?\nYES/NO: ")
    if input2 == "YES":
        print(call())
    else:
        print("OK BYE FOR NOW!!")


print(call())

