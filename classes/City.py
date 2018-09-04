from tqdm import *
from classes.Ride import *
from classes.Vehicle import *


class City:
    def __init__(self, R, C, F, N, B, T, debug=False):
        self.R = R #number of rows 
        self.C = C #number of cols
        self.F = F #number of vehicles
        self.B = B #per ride bonus
        self.T = 0 #current step in simulation
        self.maxT        = T               #max steps in simulation
        self.rides       = [None] * N      #array containing all rides
        self.free        = [[] for i in range(T)]#array containing free rides at every instant
        self.currRide    = 0               #index indicating last added ride position
        self.vehicles    = [None] * F      #array containing all vehicles
        self.currVehicle = 0               #index indicating last added vehicle position
        self.debug = debug

        for i in range(self.F):
            self.addVehicle(Vehicle(self))

        #only calculate 10% of nodes in debug mode
        if (debug == True):
            lowerbound = min(10, self.maxT)
            self.maxT = max(lowerbound, int(self.maxT / 20))

    '''Distance from intersection to intersection'''
    def distance(self, R1, C1, R2, C2):
        return abs(R1 - R2) + abs(C1 - C2)

    '''Distance from vehicle to ride'''
    def VRDistance(self, V1, R2):
        return abs(V1.x - R2.x1) + abs(V1.y - R2.y1)

    '''Function to plan busy vehicles'''
    def VehicleBusy(self, V, end):
        self.free[self.T].remove(V)
        self.free[end].append(V)

    def removeRide(self, R):
        self.rides.remove(R)

    def addVehicle(self, V):
        self.vehicles[self.currVehicle] = V
        self.free[self.T].append(V)
        self.currVehicle += 1

    def addRide(self, R):
        self.rides[self.currRide] = R 
        self.currRide += 1

    def iteration(self):
        for i in range(len(self.free[self.T])-1, -1, -1):
            V = self.free[self.T][i]
            V.finishRide()
            R = V.findOptimalRide()
            if (R != None):
                V.addRide(R)

        self.T += 1

    def findSolution(self):
        for i in tqdm(range(0, self.maxT)):
            self.iteration()
        print("")

    def printOutput(self, outputFile):
        i = 0
        score = 0
        print("Calculating score...")
        for V in self.vehicles:
            for R in V.Rides:
                score += R.getScore()

        print("Total score:", "{:,}".format(score))
        print("")

        if (self.debug == False):
            print("Writing solutions...")
            f = open(outputFile + str(score) + ".out", "w")
            
            for V in self.vehicles:
                line = str(len(V.Rides))
                for R in V.Rides:
                    line = line + " " + str(R.index)
                f.write(line)
                f.write("\n")

            f.close()

        print("Finished!")

