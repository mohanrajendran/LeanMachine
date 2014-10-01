__author__ = 'MRajendran'

from Station import *

class Controller():
    def __init__(self):
        self.stations = []

    def addStation(self):
        try:
            self.stations.append(Station())
        except ValueError:
            print "Capacity should be a number. Please try again"

    def printStations(self):
        for station in self.stations:
            print station

    def editStation(self):
        if len(self.stations) == 0:
            print "You have not added any stations. Please add stations and try again"
            return

        print "Please choose a station to edit"
        for index, station in enumerate(self.stations):
            print index + 1, " ", station

        try:
            choice = int(raw_input())
        except ValueError:
            print "Please enter a valid integer"
            return

        if choice < 1 or choice > len(self.stations):
            print "Please enter a valid integer"
            return

        self.stations[choice - 1] = Station()

    def run(self):
        if len(self.stations) == 0:
            print "You have not added any stations. Please add stations and try again"
            return