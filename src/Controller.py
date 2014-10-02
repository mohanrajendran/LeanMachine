__author__ = 'MRajendran'

import Station
import sys

class Controller():
    def __init__(self):
        self.stations = []

    def addStation(self):
        try:
            self.stations.append(Station.Station())
        except ValueError:
            print "Capacity should be an integer. Please try again"

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

        self.stations[choice - 1] = Station.Station()

    def run(self):
        if len(self.stations) == 0:
            print "You have not added any stations. Please add stations and try again"
            return

        jobsAvailable = self.stations[0].capacity

        for station in self.stations:
            station.backlog = max(0, jobsAvailable - station.capacity)
            jobsAvailable -= station.backlog

        self.printBacklog()

    def printBacklog(self):
        for idx, station in enumerate(self.stations):
            if(idx != 0):
                sys.stdout.write("-" + str(station.backlog) + "-")
            sys.stdout.write("[" + station.name + ":" + str(station.capacity) + "]")
        print
        print "Throughput: ", min(s.capacity for s in self.stations)