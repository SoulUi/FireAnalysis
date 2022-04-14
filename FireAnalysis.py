# coding: utf-8
import rhinoscriptsyntax as rs

people = []
see = 1000
step_length = 1000


def sup(x_):
    y = 1 / (((x_ / 4) - 2) ** 2 + 1)
    return y


class Person:
    def __init__(self, pt_, path_):
        self.pos = pt_
        self.path = path_
        self.temp = 0
        self.step = 0
        self.crowd = []

        people.append(self)

    def findNeighbour(self):
        self.crowd = []
        for tPerson in people:
            dist = rs.Distance(tPerson.pos, self.pos)
            if dist < see:
                self.crowd.append(tPerson)

    def run(self):
        x = len(self.crowd)
        result = 0
        for xx in range(x):
            result += sup(xx)

        # print(result)
        stepL = step_length - result * 90
        # print(stepL)
        return stepL

    def move(self):
        self.findNeighbour()
        run_length = self.run()
        # print(run_length)

        if run_length+self.temp < rs.CurveLength(self.path):
            self.pos = rs.DivideCurveLength(self.path, run_length+self.temp)[1]
            self.temp += run_length
            self.step += 1
            self.display()
        else:
            people.remove(self)

    def display(self):
        rs.AddPoint(self.pos)
        # print(self.step)
        print(len(self.crowd))


Path = rs.GetObjects("Pick some curves", rs.filter.curve)

for p in Path:
    stpt = rs.CurveStartPoint(p)
    testP = Person(stpt, p)

second = 180
for time in range(second):
    # print(len(people))
    if len(people) > 0:
        for myPerson in people:
            myPerson.move()

        rs.Sleep(1)
