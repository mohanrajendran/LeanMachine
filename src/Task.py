__author__ = 'MRajendran'

class Task():
    def __init__(self):
        self.events = []

    def addEvent(self, time, event):
        self.events.append((time, event))