# Name:   Bunmi Oluwatudimu
# Date:     March 6th, 2020

# The LinkedList class: a collection of nodes (Node: data and a link to the next node)
from node import Node

class LinkedList():
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head == None

    # add a node at the end of the linked list
    def append(self, data):
        newNode = Node(data)

        if self.isEmpty():  # if list is empty, head will point to newNode
            self.__head = newNode

        else:  # list is not empty, go to end of list and add newNode there
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)

    # remove a node from the linked list
    def remove(self, item):
        current = self.__head
        previous = None
        found = False

        # first find item in the list
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:  # item was in the fist node
            self.__head = current.getNext()
        else:  # item was somewhere after the first node
            previous.setNext(current.getNext())

    # search for item in linked list
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    # overloaded operators
    def __getitem__(self, index):  # used to suppport []
        current = self.__head

        for i in range(index):
            current = current.getNext()

        return current.getData()

    def __str__(self):  # used to support print(myLinkedList)
        mystr = ''
        current = self.__head

        while current != None:
            mystr += str(current.getData())
            current = current.getNext()
        return mystr

    def __len__(self):  # used to support len(myLinkedList)
        if self.__head == None:  # if list is empty return 0
            return 0

        current = self.__head  # list is not empty and has at least 1 Node
        counter = 1

        while current.getNext() != None:
            counter += 1
            current = current.getNext()
        return counter
