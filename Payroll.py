# Name:   Bunmi Oluwatudimu
# Date:     March 6th, 2020

from linkedList import LinkedList
from node import Node
from employee import Employee

payroll = LinkedList()

def menu():
    print("\n*** CS 172 Payroll Simulator ***\n"
          "a. Add New Employee\n"
          "b. Calculate Weekly Wages\n"
          "c. Display Payroll\n"
          "d. Update Employee Hourly Rate\n"
          "e. Remove Employee from Payroll\n"
          "f. Exit the program\n")

    choice = input("Enter your choice: ")
    choice = choice.lower()

    trueRate = True
    newID = True
    removeMe = False

    flag = True
    while flag != False:
        if choice == "a":
            ID = input("Enter the new employee ID: ")
            rate = input("Enter the hourly rate:  ")
            new_employee = Employee(ID, rate)
            payroll.append(new_employee)
            menu()

        elif choice == "b":
            for index in range(0, len(payroll)):
                selectEmployee = payroll[index].getID()
                hours = float(input('Enter hours worked for employee ' + str(selectEmployee) + ' : '))
                if float(hours) >= 0:
                    payroll[index].setHours(hours)
                    myWage = str(float(hours) * payroll[index].getRate())
                    payroll[index].setWage(myWage)
                else:
                    print('Invalid number of hours')
            menu()

        elif choice == "c":
            if payroll.isEmpty():
                print('No employee in payroll')
                print()
            else:
                print('\n *** Payroll ***')
                print(payroll)
            menu()

        elif choice == 'd':
            selectEmployee = input('Enter the ID of the employee to update hourly rate: ')
            for i in range(0, len(payroll)):
                if payroll[i].getID() == selectEmployee:
                    updateRate = float(input('Type in the new hourly rate: '))
                    if updateRate > 6:
                        payroll[i].setRate(updateRate)
                        newWage = payroll[i].getRate() * payroll[i].getHours()
                        payroll[i].setWage(newWage)
                        print()
            menu()

        elif choice == 'e':
            selectEmployee = input('Enter the ID of the employee to remove from payroll: ')
            for index in range(0, len(payroll)):
                if payroll[index].getID() == selectEmployee:
                    payroll.remove(payroll[index])
                    print('Done.')
                    break
            print()
            menu()

        elif choice == 'f':
            flag = False
            print('Good-Bye!')
            quit()

        else:
            print("Invalid Option\n")
            menu()

menu()


