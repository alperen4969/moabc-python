import numpy as np
import random


def dominates(x,y):

    # TODO 2 tane isstruct methodu vardı
    x = x["cost"]
    y = y["cost"]
    # b = x.all() <= y.all() and x.any() < y.any()
    b = np.all(x <= y) and np.any(x < y)
    # b = 1
    # dom_list.append(b)
    # print(int(b), end="")

    # for deubugging
    # coin = [0, 1]
    # b = random.choice(coin)

    return b
