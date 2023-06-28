from abc import ABC, abstractmethod


class coup_de_ecriva(ABC):
    @abstractmethod
    def Fan_Page(self):
        pass


class FC_Cirok(coup_de_ecriva):
    def Fan_Page(self, clubname):
        print("Welcome to ", clubname)


class Madiba_FC(coup_de_ecriva):
    def Fan_Page(self, clubname):
        print("Welcome to ", clubname)


class Blue_Jay_FC(coup_de_ecriva):
    def Fan_Page(self, clubname):
        print("Welcome to ", clubname)


class TSG_Walker(coup_de_ecriva):
    def Fan_Page(self, clubname):
        print("Welcome to ", clubname)


clubname = input("What club do you support? ")

if clubname == "FC_Cirok":
    F = FC_Cirok()
    F.Fan_Page(clubname)
elif clubname == "Madiba_FC":
    F = Madiba_FC()
    F.Fan_Page(clubname)
elif clubname == "Blue_Jay_FC":
    F = Blue_Jay_FC()
    F.Fan_Page(clubname)
elif clubname == "TSG_Walker":
    F = TSG_Walker()
    F.Fan_Page(clubname)
else:
    print("Sorry, the club you input doess not exist")

