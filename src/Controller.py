__author__ = 'MRajendran'

from Station import *

choice = -1
stations = []
while (choice != 3):
    print "Main Menu"
    print "1) Add Station"
    print "2) Run"
    print "3) Quit"

    choice = int(raw_input())

    if choice == 1:
        name = raw_input("Name?: ")
        capacity = raw_input("Capacity?: ")
        stations.append(Station(name, capacity))

    if choice == 2:
        print "List of stations:-"
        for station in stations:
            print "Name:", station.name, " Capacity: ", station.capacity
        print