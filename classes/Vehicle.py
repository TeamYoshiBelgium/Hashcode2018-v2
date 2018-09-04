import math
from classes.Ride import *
from classes.City import *


class Vehicle:
    def __init__(self, City):
        self.x = 0
        self.y = 0
        self.busy    = False
        self.Ride    = None
        self.City    = City
        self.Rides   = []
        self.RidesNo = 0


    def addRide(self, R):
        now   = self.City.T
        start = max(now + self.City.VRDistance(self, R), R.S)
        end   = start + R.duration()

        if (end < R.F):
            self.Ride = R
            self.busy = True
            self.City.VehicleBusy(self, end)
            self.City.removeRide(R)
            self.Rides.append(R)
            self.RidesNo += 1

            if (start == R.S):
                R.onTime = True

    def finishRide(self):
        # In the first iteration there was no prev Ride
        if (self.Ride != None):
            self.x = self.Ride.x2
            self.y = self.Ride.y2
            self.busy = False
            self.Ride = None

    def findOptimalRide(self):
        best = None
        score = 0
        for R in self.City.rides: 
            s = self.calcScore(R)
            if (s != False and s > score):
                best = R
                score = s

        return best

    def calcScore(self, R):
        score = 0
        start = max(self.City.T + self.City.VRDistance(self, R), R.S)
        
        if (start + R.duration() > R.F):
            return False

        if (start == R.S):
            score += self.City.B

        score += R.score 

        return score / (start + R.duration() - self.City.T)

