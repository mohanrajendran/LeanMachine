__author__ = 'MRajendran'

import Task
import Queue

class Station():
    def __init__(self):
        self.name = raw_input("Name: ")
        self.capacity = int(raw_input("Capacity: "))
        self.backlog = 0
        self.tasks = Queue.Queue()
        self.queueLength = 0

    def __repr__(self):
        return "Name: " + self.name + " Capacity: " + str(self.capacity)

    def backlogString(self):
        return "Name: " + self.name + " Capacity: " + str(self.capacity) + " Backlog: " + str(self.backlog)

    def addTasks(self, pulse, tasks):
        for t in tasks:
            t.addEvent(pulse, "Queued to Task: " + self.name)
            self.tasks.put(t)
            self.queueLength += 1

    def completeTasks(self, pulse):
        tasksToComplete = min(self.capacity, self.queueLength)
        completedTasks = []

        for i in range(tasksToComplete):
            t = self.tasks.get()
            t.addEvent(pulse, "Completed Task: " + self.name)
            completedTasks.append(t)
            self.queueLength -= 1

        return completedTasks