# importing pandas as pd
import pandas as pd
import csv

# welcome message/note
print("Welcome to JT Ventures")
print("We are a company that provides delivery services to various businesses nationwide. Your package, we handle.")


def ventures(str):
    last_name = str(input("What is your last name?: "))
    first_name = str(input("What is your first name?: "))
    dept = str(input("What is your department: "))

    def search_csv(lname, fname, dept, csv_file):
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if lname == row[1] and fname == row[2] and dept == row[3]:
                    print(f"Hello {last_name} {first_name} from {dept}!")

                    return

            print("The inputted data is not contained in our database.")

    search_csv(last_name.upper(), first_name.capitalize(), dept.capitalize(), "jt-ventures.csv")
    print(last_name.upper(), first_name.capitalize(), dept.capitalize())

    data = pd.read_csv("jt-ventures.csv")
    print(data)


ventures(str)
