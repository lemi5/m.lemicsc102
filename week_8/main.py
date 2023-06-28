# week9
class Zenith():
    u_services = ['Retirement and education accounts', 'loans and mortgagges', 'Checking and saving', \
                  'Multi-currency management services and products', 'Foreign currency accounts',
                  'Foreign currency credit cards', \
                  'Transborder advisory services', 'Liquidity management', 'Advisory services']
    m_services = ['Lines of credit', 'Investment management and accounts', 'Insurance']

    def __init__(self, name):
        self.name = name

    def checkemployee(self):
        if name in name_records:
            return True
        else:
            return False

    def unique_services(self):
        global u_services
        u_services = ['Retirement and education accounts', 'loans and mortgagges', 'Checking and saving', \
                      'Multi-currency management services and products', 'Foreign currency accounts',
                      'Foreign currency credit cards', \
                      'Transborder advisory services', 'Liquidity management', 'Advisory services']

    def mutual_services(self):
        global m_services
        m_services = ['Lines of credit', 'Investment management and accounts', 'Insurance']


class Retail_banking(Zenith):
    def __init__(self, name):
        Zenith.__init__(self, name)

    def service(self):
        # print the range of values in the list without the square brackets
        services1 = ', '.join(str(x) for x in self.m_services[0:])
        services2 = ', '.join(str(x) for x in self.u_services[0:3])
        print(f"Your services are: {services1}, {services2}.")


class Global_banking(Zenith):
    def __init__(self, name):
        Zenith.__init__(self, name)

    def service(self):
        services = ', '.join(str(x) for x in self.u_services[3:8])
        print(f"Your services are: {services}.")


class Commercial_banking(Zenith):
    def __init__(self, name):
        Zenith.__init__(self, name)

    def service(self):
        services1 = ', '.join(str(x) for x in self.m_services[0:])
        services2 = self.u_services[8]
        print(f"Your services are: {services1}, {services2}.")


name = input("Please input your first name only: ")

name_records = ['Mary', 'Agatha', 'Noel']

obj_retail = Retail_banking(name)
obj_global = Global_banking(name)
obj_commercial = Commercial_banking(name)
obj_retail.checkemployee()

if obj_retail.checkemployee() == True:
    division = input("Please input your division: ")
    division_records = ['Retail Banking', 'Global Banking', 'Commercial Banking']
    if (name == name_records[0]) and (division == division_records[0]):
        obj_retail.service()
    elif (name == name_records[1]) and (division == division_records[1]):
        obj_global.service()
    elif (name == name_records[2]) and (division == division_records[2]):
        obj_commercial.service()
    else:
        print("Sorry, your name does not correlate with your division.")
else:
    print("Sorry, your name does not exist in our records.")