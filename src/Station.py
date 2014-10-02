__author__ = 'MRajendran'

class Station():
    def __init__(self):
        self.name = raw_input("Name: ")
        self.capacity = int(raw_input("Capacity: "))
        self.backlog = 0

    def __repr__(self):
        return "Name: " + self.name + " Capacity: " + str(self.capacity)

    def backlogString(self):
        return "Name: " + self.name + " Capacity: " + str(self.capacity) + " Backlog: " + str(self.backlog)
