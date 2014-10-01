__author__ = 'MRajendran'

class Station():
    def __init__(self):
        self.name = raw_input("Name: ")
        self.capacity = float(raw_input("Capacity: "))
        self.backlog = []

    def __repr__(self):
        return "Name: " + self.name + "Capacity: " + str(self.capacity)
