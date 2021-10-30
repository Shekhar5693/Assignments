# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 16:01:42 2021

@author: shekh
"""

import time

class Stopwatch:
    def __init__(self):
        self.startTime = time.clock()

        self.endTime = None

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def start(self):
        self.startTime = time.time()

    def stop(self):
        self.endTime = time.time()

    def getElapsedTime(self):
        elapsedTime = None;
        if (self.endTime != None):
            elapsedTime = (self.endTime - self.startTime) * 1000
        return elapsedTime


def measure_time():
    sum = 0
    timer = Stopwatch()
    timer.start()

    for i in range(1, 1000000):
        sum = sum + i
    timer.stop()

    print("Execution time :", timer.getElapsedTime());

measure_time()