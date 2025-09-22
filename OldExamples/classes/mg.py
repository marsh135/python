

class Assignment:
    def __init__(self, name, pointsE, pointsP, weight):
        self.name = name
        self.pointsE = pointsE
        self.pointsP = pointsP
        self.weight = weight
        avg = pointsE/pointsP*100
        weightScore =  avg*weight
        self.wS = weightScore
        self.avg = avg

    def __str__(self):
        return f"{self.name}: {self.avg}"

a1 = Assignment("test1", 82, 100, 2)
a2 = Assignment("ch1", 20, 20, 1)
print(a1)
print(a2)