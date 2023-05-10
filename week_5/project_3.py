import pandas as pd

# welcome message
print("Pan-Atlantic University")
print("Determine your admission into the university now!")

# user option to choose
print("What course are applying for?: ")
course = str(input("Course: "))

if course == "Computer Science":
    def compsci():

        data = {}
        fname = str(input("Student's First Name: "))
        lastname = str(input("Student's Last Name: "))

        jamb_score = int(input("Student's JAMB Score: "))

        print(
            "For you to be admitted into the Computer Science Undergraduate Programme, you must have at least 5 credits in your 5 core subjects. \n They include: English, Mathematics, Physics, Chemistry, and any of Geography, Biology, or Economics")
        print("Please input the your course grades according to the displayed information below")
        print(
            "A1 = 75-100 \nB2 = 70-74 \nB3 = 65-69 \nC4 = 60-64 \nC5 = 55-59 \nC6 = 50-54 \nD7 = 45-49 \nE8 = 40-44 \nF9 = 0-39")

        english = str(input("English: "))
        math = str(input("Mathematics: "))
        physics = str(input("Physics: "))
        chem = str(input("Chemistry: "))
        geo_bio_econ = str(input("Geography, Biology or Economics: "))

        subjects = [english, math, physics, chem, geo_bio_econ]

        print(
            f"Here are the subjects you entered: English: {english} \nMathematics: {math} \nPhysics: {physics} \nChemistry: {chem} \nGeography, Biology, or Economics: {geo_bio_econ}")

        if jamb_score < 230.0 or english in ["D7", "E8", "F9"] or math in ["D7", "E8", "F9"] or physics in ["D7", "E8",
                                                                                                            "F9"] or chem in [
            "D7", "E8", "F9"] or geo_bio_econ in ["D7", "E8", "F9"]:
            print("Sorry, you have not been admitted into the Computer Science Programme")
            data["First Name"] = [fname]
            data["Last Name"] = [lastname]
            data["Jamb Score"] = [jamb_score]
            data["English"] = [english]
            data["Mathematics"] = [math]
            data["Physics"] = [physics]
            data["Chemistry"] = [chem]
            data["Geography, Biology or Economics"] = [geo_bio_econ]

            df = pd.DataFrame(data)
            df.to_csv("not-admitted.csv", index=False)


        else:
            print(
                f"Congratulations, you have been admitted into the Computer Science Programme. Welcome to Pan-Atlantic University")
            data["First Name"] = [fname]
            data["Last Name"] = [lastname]
            data["Jamb Score"] = [jamb_score]
            data["English"] = [english]
            data["Mathematics"] = [math]
            data["Physics"] = [physics]
            data["Chemistry"] = [chem]
            data["Geography, Biology or Economics"] = [geo_bio_econ]

            df = pd.DataFrame(data)
            df.to_csv("admitted.csv", index=False)


    compsci()

elif course == "Mass Communication":
    def masscomm():

        data = {}
        fname = str(input("Student's First Name: "))
        lastname = str(input("Student's Last Name: "))

        jamb_score = int(input("Student's JAMB Score: "))

        print(
            "For you to be admitted into the Mass Communication Undergraduate Programme, you must have at least 5 credits in your 5 core subjects. \n They include: English, Mathematics, Literature, Government and any one of History, Commerce, Business Studies or Marketing")
        print("Please input the your course grades according to the displayed information below")
        print(
            "A1 = 75-100 \nB2 = 70-74 \nB3 = 65-69 \nC4 = 60-64 \nC5 = 55-59 \nC6 = 50-54 \nD7 = 45-49 \nE8 = 40-44 \nF9 = 0-39")

        english = str(input("English: "))
        math = str(input("Mathematics: "))
        lit = str(input("Literature: "))
        gov = str(input("Government: "))
        his_mar = str(input("History, Commerce, Business Studies or Marketing: "))

        subjects = [english, math, lit, gov, his_mar]

        if jamb_score < 220.0 or english in ["D7", "E8", "F9"] or math in ["D7", "E8", "F9"] or lit in ["D7", "E8",
                                                                                                        "F9"] or gov in [
            "D7", "E8", "F9"] or his_mar in ["D7", "E8", "F9"]:
            print("Sorry, you have not been admitted into the Mass Communication Programme")
            data["First Name"] = [fname]
            data["Last Name"] = [lastname]
            data["Jamb Score"] = [jamb_score]
            data["English"] = [english]
            data["Mathematics"] = [math]
            data["Literature"] = [lit]
            data["Government"] = [gov]
            data["History, Commerce, Business Studies or Marketing"] = [his_mar]

            df = pd.DataFrame(data)
            df.to_csv("not-admitted.csv", index=False)


        else:
            print(
                f"Congratulations, you have been admitted into the Mass Communication Programme. Welcome to Pan-Atlantic University")
            data["First Name"] = [fname]
            data["Last Name"] = [lastname]
            data["Jamb Score"] = [jamb_score]
            data["English"] = [english]
            data["Mathematics"] = [math]
            data["Literature"] = [lit]
            data["Government"] = [gov]
            data["History, Commerce, Business Studies or Marketing"] = [his_mar]

            df = pd.DataFrame(data)
            df.to_csv("admitted.csv", index=False)


    masscomm()

else:
    print("The Course you have inputted is not available")