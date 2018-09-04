import os.path
from tqdm            import *
from classes.City    import City
from classes.Ride    import Ride
from classes.Vehicle import Vehicle


def checkFileExists(filename):
    if (os.path.isfile(filename)):
        return True
    else:
        raise ValueError("File not found: " + filename)


def importFile(filename, debug=False):
    checkFileExists(filename)
    f = open(filename)

    Ct = None
    index = 0
    for line in f:
        if (index == 0):
            params = line.strip().split(" ")
            R = int(params[0])
            C = int(params[1])
            F = int(params[2])
            N = int(params[3])
            B = int(params[4])
            T = int(params[5])

            Ct = City(R, C, F, N, B, T, debug)
        else:
            params = line.strip().split(" ")
            a = int(params[0])
            b = int(params[1])
            x = int(params[2])
            y = int(params[3])
            s = int(params[4])
            f = int(params[5])

            R = Ride(a, b, x, y, s, f, Ct, index-1)
            Ct.addRide(R)

        index += 1

    return Ct
