'''
Created on 18-Dec-2016

@author: honey
'''
import sys
import os


class car(object):
    def __init__(self, name, model, make, color, regNo):
        self.name = name
        self.model = model
        self.make = make
        self.color = color
        self.regNo = regNo

    def addCarDetails(self):
        print("Creating a new file...")
        name = self.regNo+".txt"
        try:
            file = open(name, "w")
            file.write("Car Details:\n" + "---------------------")
            file.write("\nName : " + self.name)
            file.write("\nModel : " + self.model)
            file.write("\nMake : " + self.make)
            file.write("\nColor : " + self.color)
            file.write("\nRegistration No : " + self.regNo)
            file.close()
        except:
            print("Error Occurred")
            sys.exit()

    def deleteCarDetails(self, reg):
        name = reg + ".txt"
        os.remove(name)
        print("Deleted Successfully")

    def showCarDetails(self, reg):
        name = reg + ".txt"
        try:
            file = open(name, "r")
            print(file.read())
            file.close()
        except:
            print("Error opening file, No such file exists...")
            sys.exit()

    def printCarDetails(self):
        print("Car Details:\n" + "---------------------")
        print("Name : " + self.name)
        print("Model : " + self.model)
        print("Make : " + self.make)
        print("Color : " + self.color)

while 1:
    print("\nMenu:")
    print("1. Add Car Details\n"+"2. Delete Car Details\n"+"3. Get Car Details\n"+"4. Exit")
    option = int(input("Select any option to proceed:"))
    
    
    if option == 1:
        name = input("Enter name of the car :")
        model = input("Enter model of the car :")
        make = input("Enter make of the car :")
        color = input("Enter color of the car :")
        regNo = input("Enter registration no of the car(only testing purpose,should find other way) :")
        carObj = car(name, model, make, color, regNo)
        carObj.addCarDetails()
        carObj.printCarDetails()
    
    if option == 2:
        reg = input("Enter registration number:")
        car.deleteCarDetails(None, reg)
    
    if option == 3:
        reg = input("Enter registration number:")
        car.showCarDetails(None, reg)
    
    if option == 4:
        print("Exiting....")
        sys.exit()
