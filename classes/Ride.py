import copy

class Ride:
    def __init__(self, x1, y1, x2, y2, S, F, C, index):
        self.x1 = x1 #startX
        self.y1 = y1 #startY
        self.x2 = x2 #endX
        self.y2 = y2 #endY
        self.S  = S  #The earliest start
        self.F  = F  #The latest finish
                     #You recieve bonus if started exactly at the right start moment
                     #Ride must end before finish
                     #Waiting is possible
        self.score = abs(x1-x2) + abs(y1-y2)
        self.index = index
        self.City  = C
        self.onTime = False

    def duration(self):
        return self.score

    def getScore(self):
        score = self.score

        if (self.onTime == True):
            score += self.City.B

        return score