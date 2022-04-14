# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

nx = np.arange(1, 100, 1)

ny = []


def sup(x_):
    y_ = 1 / (((x_ / 4) - 2) ** 2 + 1)
    return y_


def addd(xxx):
    result = 0
    for xx in range(xxx):
        result += sup(xx)

    # print(result)
    stepL = 1000 - result * 90
    return stepL


for x in nx:
    ry = addd(x)
    ny.append(ry)

plt.figure(num='速度变化')
plt.plot(nx, ny, label='Speed')

plt.show()
