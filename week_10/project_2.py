from abc import ABC, abstractmethod
import pandas as pd

file_path = 'menu.csv'


class External_Vendors(ABC):
    @abstractmethod
    def menu(self):
        pass


class Faith(External_Vendors):
    def menu(self):
        menu = {
            'Fried Rice': 400,
            'White Rice and Stew': 400,
            'Jollof Rice': 400,
            'Beans': 200,
            'Chicken': 1000
        }
        menu_df = pd.DataFrame.from_dict(menu, orient='index', columns=['Price'])
        menu_df.index.name = 'Main Meals'
        menu_df.to_csv(file_path)


class Cooperative(External_Vendors):
    def menu(self):
        menu = {
            'Jollof Rice and Stew': 200,
            'White Rice and Stew': 200,
            'Fried Rice': 200,
            'Salad': 100,
            'Plantain': 100
        }
        menu_df = pd.DataFrame.from_dict(menu, orient='index', columns=['Price'])
        menu_df.index.name = 'Main Meals'
        menu_df.to_csv(file_path)


class S_center(External_Vendors):
    def menu(self):
        menu = {
            'Chicken and Fried Rice': 800,
            'Pomo Sauce': 'Sauce',
            'Spaghetti Jollof': 500,
            'Amala/Ewedu': 500,
            'Semo with Eforiro Soup': 500
        }
        menu_df = pd.DataFrame.from_dict(menu, orient='index', columns=['Price'])
        menu_df.index.name = 'Main Meals'
        menu_df.to_csv(file_path)


vendor = input("What vendor would you like to buy from?")

if vendor == "Faith hostel":
    F = Faith()
    F.menu()
elif vendor == "Cooperative hostel":
    C = Cooperative()
    C.menu()
elif vendor == "Student center":
    S = S_center()
    S.menu()
else:
    print("Sorry, the vendor you mentioned does not exist.")