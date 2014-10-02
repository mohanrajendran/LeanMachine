#!/usr/bin/env python

import Controller as Controller

if __name__ == "__main__":
    choice = ""
    c = Controller.Controller()

    while (True):
        print "Main Menu"
        print "1) Add Station"
        print "2) Print Stations"
        print "3) Edit Station"
        print "4) Compute throughput"
        print "5) Compute cycle times"
        print "6) Quit"

        choice = raw_input()

        if choice == "1":
            c.addStation()

        elif choice == "2":
            c.printStations()

        elif choice == "3":
            c.editStation()

        elif choice == "4":
            c.computeThroughput()

        elif choice == "5":
            c.computeCycleTimes()

        elif choice == "6":
            exit()

        else:
            print "Please give a valid input"
