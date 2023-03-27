import datetime
import time


class Clock:
    def __init__(self):
        self.clock = datetime.datetime.now()
        self.pause = False

    def pause(self):
        self.pause = not self.pause

    def getTime(self):
        return self.clock

    def setTime(self, time):
        self.clock = time

    def ToString(self):
        return str(self.clock)

    def start(self):
        #infinite loop
        while True:
            if self.pause == False:
                #als niet op pauze add 5 minuten
                self.clock += datetime.timedelta(minutes=5)
                print(self)

