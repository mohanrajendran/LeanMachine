__author__ = 'MRajendran'

import Station
import sys
import Task
import Queue

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

    def computeThroughput(self):
        if len(self.stations) == 0:
            print "You have not added any stations. Please add stations and try again"
            return

        jobsAvailable = self.stations[0].capacity

        for station in self.stations:
            station.backlog = max(0, jobsAvailable - station.capacity)
            jobsAvailable -= station.backlog

        self.printBacklog()

    def printBacklog(self):

        throughput = sys.maxint
        bottleneck = ""

        for idx, station in enumerate(self.stations):
            if(idx != 0):
                sys.stdout.write("-" + str(station.backlog) + "-")
            sys.stdout.write("[" + station.name + ":" + str(station.capacity) + "]")
            if station.capacity < throughput:
                throughput = station.capacity
                bottleneck = station.name
        print

        print "Throughput: ", throughput
        print "Bottleneck: ", bottleneck

    def computeCycleTimes(self):
        if len(self.stations) == 0:
            print "You have not added any stations. Please add stations and try again"
            return

        try:
            pulses = int(raw_input("Enter the number of pulses to simulate: "))
        except ValueError:
            print("Please enter an integer")
            return

        try:
            workPerPulse = int(raw_input("Enter the number of tasks to push per pulse: "))
        except ValueError:
            print("Please enter an integer")
            return

        self.completed = []
        averages = []
        sizes =[]

        for station in self.stations:
            station.queueLength = 0
            station.tasks = Queue.Queue()

        for pulse in range(pulses):
            self.pulseAndWork(pulse, workPerPulse)
            s = 0
            for task in self.completed:
                s += (task.events[-1][0] - task.events[0][0] + 1)
            averages.append(float(s) / len(self.completed))
            sizes.append(len(self.completed))

        print "Average cycle time at pulses"
        for idx, average in enumerate(averages):
            print "End of cycle", idx, ":"
            print "   Number of tasks completed:", sizes[idx]
            print "          Average time taken:", average

        #for idx, task in enumerate(self.completed):
        #    print idx+1, task.events[-1][0] - task.events[0][0] + 1

    def pulseAndWork(self, pulse, work):
        completedTasks = [Task.Task() for i in range(self.stations[0].capacity)]

        for station in self.stations:
            station.addTasks(pulse, completedTasks)
            completedTasks = station.completeTasks(pulse)

        map(self.completed.append, [t for t in completedTasks])