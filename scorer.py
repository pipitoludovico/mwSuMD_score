import math
import random
import collections


class Scorer:
    def __init__(self):
        self.n = None
        self.ranked = None
        self.standDev = None
        self.selection = None
        self.counter = None
        self.stdDev = None
        self.mean = None
        self.scoresList = []
        for x in range(16):
            x = random.uniform(1.0, 1.2)
            self.scoresList.append(round(x, 2))
            self.scoresList.sort()

    def varianceGetter(self, dof=0) -> float:
        self.n = len(self.scoresList)
        self.mean = sum(self.scoresList) / self.n
        print("Mean: " + str(self.mean))
        variance = (sum((x - self.mean) ** 2 for x in self.scoresList) / (self.n - dof))
        print("Variance: " + str(variance))
        return sum((x - self.mean) ** 2 for x in self.scoresList) / (self.n - dof)

    def stDev(self) -> float:
        self.stdDev = math.sqrt(self.varianceGetter())
        print("Standard Deviation: " + str(self.stdDev))
        return float(self.stdDev)

    def frequency(self) -> dict:
        self.counter = collections.Counter(self.scoresList)
        return self.counter

    def selectBatch(self):
        self.selection = []
        self.standDev = self.stdDev
        self.ranked = dict(sorted(self.counter.most_common(), key=lambda item: item[1]))
        print("Results grouped and ranked by frequency: ")
        print((sorted(self.ranked.items(), key=lambda item: item[1], reverse=True)))
        print((self.mean - self.standDev), (self.mean + self.standDev))
        for k, v in self.ranked.items():
            # potremmo considerare anche questo per essere più comprensivi
            if (self.mean - self.standDev) < k < (self.mean + self.standDev) and v > 1:
            # if v > 1:
                self.selection.append((k, v))
        print(self.selection)
