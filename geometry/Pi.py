import random
from math import sqrt

def pi_approx(n):
    incircle = 0

    for i in range(n):
        x = random.random()
        y = random.random()

        if sqrt(x ** 2 + y ** 2) < 1:
            incircle += 1

    return 4 * incircle / n