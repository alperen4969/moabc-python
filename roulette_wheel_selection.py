import random as random
import numpy as np


def roulette_wheel_selection(p):
    r = random.random()
    C = np.cumsum(p)
    # r = 0.736340074301202  # for debugging
    # i = np.where(r <= C, 1, 'first')
    # xx = temp_grid_ub[0]
    i = np.where(r <= C)[0]

    return i[0]
