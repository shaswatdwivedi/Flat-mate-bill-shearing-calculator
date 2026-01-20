from os import name


class Bill:

     def __init__(self,amount, period):
         self.amount = amount
         self.period = period

class Flatmate:


    def __init__(self,name,days_in_house):
        self.name = name
        self.days_in_house = days_in_house
    def pays(self,Bill,flatmate2):
             weight =self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
             to_pay = Bill.amount * weight
             return to_pay
class Pdfreport:
    def __init__(self,filename):
        self.filename = filename

    def genrate(self,flatmate1,flatmate2,Bill):
        pass

Bill =Bill(amount =128,period = "March 2021")
john = Flatmate(name="john",days_in_house=20)
marry = Flatmate(name="marry",days_in_house=25)
"""
 remember to write class , function , object as it is
"""

print(john.pays(Bill=Bill,flatmate2=marry))
print(marry.pays(Bill=Bill,flatmate2=john))
