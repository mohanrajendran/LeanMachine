__author__ = 'MRajendran'

from Controller import *

if __name__ == "__main__":
    choice = ""
    c = Controller()

    while (choice != "3"):
        print "Main Menu"
        print "1) Add Station"
        print "2) Print Stations"
        print "2) Run"
        print "3) Quit"

        choice = raw_input()

        if choice == "1":
            c.addStation()

        elif choice == "2":
            c.printStations()

        elif choice == "3":
            c.run()

        elif choice != "4":
            print "Please give a valid input"