import pandas as pd

# Create an empty list that will contain the companies info
companies_f = []
filename = "Companies.csv"


class Economy():
    def __init__(self, company, date, asset, liability):
        self.company = company
        self.date = date
        self.asset = asset
        self.liability = liability
        leverage = 0

    # This method calculates the leverage value in %
    def leverage_calc(self):
        self.leverage = (self.asset - self.liability) / self.asset
        self.leverage = self.leverage * 100

    # this method creates the file
    def create_file(self):
        companies = {"Company": self.company, "Date Founded": self.date, "Company's Shares": self.asset,
                     "Company's Liabilities": self.liability, "Leverage(%)": self.leverage}
        companies_f.append(companies)

        global df
        df = pd.DataFrame(companies_f)
        df.to_csv(filename)


# Lists containing the companies data
company_list = ["Enron", "Anderson", "GK Jones", "Mica", "Dune"]
date_list = [1987, 1936, 2001, 1996, 2008]
asset_list = [1000000, 1500000, 3000000, 250000, 800000]
liability_list = [200000, 500000, 1500000, 50000, 300000]

# Loop for each company
for company, date, asset, liability in zip(company_list, date_list, asset_list, liability_list):
    obj = Economy(company, date, asset, liability)
    obj.leverage_calc()import pandas as pd

# Create an empty list that will contain the companies info
companies_f = []
filename = "Companies.csv"

class Economy():
    def __init__(self, company, date, asset, liability):
        self.company = company
        self.date = date
        self.asset = asset
        self.liability = liability
        leverage = 0

    # This method calculates the leverage value in %
    def leverage_calc(self):
        self.leverage = (self.asset - self.liability)/self.asset
        self.leverage = self.leverage * 100

    # this method creates the file
    def create_file(self):
        companies = {"Company": self.company, "Date Founded": self.date, "Company's Shares": self.asset, "Company's Liabilities": self.liability, "Leverage(%)": self.leverage}
        companies_f.append(companies)

        global df
        df = pd.DataFrame(companies_f)
        df.to_csv(filename)


# Lists containing the companies data
company_list = ["Enron", "Anderson", "GK Jones", "Mica", "Dune"]
date_list = [1987, 1936, 2001, 1996, 2008]
asset_list = [1000000, 1500000, 3000000, 250000, 800000]
liability_list = [200000, 500000, 1500000, 50000, 300000]

# Loop for each company
for company, date, asset, liability in zip(company_list, date_list, asset_list, liability_list):
    obj = Economy(company, date, asset, liability)
    obj.leverage_calc()