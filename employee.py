# Name:   Bunmi Oluwatudimu
# Date:     March 6th, 2020

class Employee():

    def __init__(self, ID, rate, hours = 0.00, wage = 0.00):
        self.ID = ID
        self.hours = float(hours)
        self.rate = float(rate)
        self.wage = float(wage)

    #Setters
    def setID(self, ID):
        self.ID = ID

    def setHours(self, hours):
        self.hours = float(hours)

    def setRate(self, rate):
        self.rate = float(rate)

    def setWage(self, wage):
        self.wage = float(wage)

    # Getters
    def getID(self):
        return self.ID

    def getHours(self):
        return self.hours

    def getRate(self):
        return self.rate

    def getWage(self):
        return self.wage

    #__str__ function that enables you to print an Employee object
    def __str__(self):
        return ("Employee ID:  {}\n"
                "Hourly Rate:  {}\n"
                "Hours Worked: {}\n"
                "Gross Wages:  {}\n\n".format(self.ID, self.rate, self.hours, self.wage))



