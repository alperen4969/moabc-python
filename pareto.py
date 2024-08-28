import numpy as np


def pareto(name, no, dim):
    # no = 21
    # pf = np.zeros(2, no)
    # pf[1,:] = (0:1:20) / 20.0  # TODO: np.linspace?
    # pf[2,:] = 1 - pf[0,:]
    # ps = []

    no = 21
    pf = np.zeros((2, no))
    # pf[0, :] = np.linspace(0, 20, 1)
    pf[0, :] = np.arange(0, 20, 1)
    pf[1, :] = 1 - pf[0, :]
    ps = []

    return pf, ps