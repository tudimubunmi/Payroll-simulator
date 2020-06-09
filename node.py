# Name:   Bunmi Oluwatudimu
# Date:     March 6th, 2020

# The Node class - to be used to create linked lists
# Code provided and used in this file is from lecture slides -- CITATION
class Node():
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    # getters
    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    # setters
    def setData(self, d):
        self.__data = d

    def setNext(self, n):
        self.__next = n

    # overloaded operators
    def __str__(self):
        return str(self.__data) + " whose next node is " + str(self.__next)