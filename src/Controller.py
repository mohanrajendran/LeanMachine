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
            self.addStation()

    def printStations(self):
        for station in self.stations:
            print station

    def run(self):
        if len(self.stations) == 0:
            print "You have not added any stations. Please add stations and try again"
            return