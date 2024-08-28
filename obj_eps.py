import numpy as np
from scipy.stats import norm


def eps_cons_obj(x, opt):
    nObj = opt['numObj']
    nCons = 10

    coeff_mean_1 = opt['coeff_mean_1']
    coeff_mean_2 = opt['coeff_mean_2']
    less = opt['less']
    greater = opt['greater']
    less_var = opt['less_var']
    greater_var = opt['greater_var']
    alpha = opt['alpha']

    y = {'mean': np.zeros(nObj), 'var': np.zeros(nObj)}
    cons = np.zeros(nCons)

    x1 = np.sum(x, axis=1)
    costpoints = np.zeros((opt['C'].shape[0], len(x1)))
    for i in range(len(x1)):
        costpoints[:, i] = x1[i] * opt['C'][:, i]
    debug_costpoint = np.sum(costpoints, axis=1)
    y['variance'] = np.zeros((opt['C'].shape[0], 2))
    y['variance'][:, 0] = np.sum(costpoints, axis=1)

    empoints = np.zeros((opt['E'].shape[0], len(x1)))
    for i in range(len(x1)):
        empoints[:, i] = x1[i] * opt['E'][:, i]
    y['variance'][:, 1] = np.sum(empoints, axis=1)

    variance = y['variance']
    meann = np.sum(variance, axis=0) / 1000
    y['mean'][0] = meann[0]
    y['mean'][1] = meann[1]

    test2 = np.sum(x[0, :])
    if alpha[0] == 1:
        for i in range(len(less)):
            debug_sum = np.sum(x[i, :])
            if np.sum(x[i, :]) > less[i]:
                cons[i] = np.sum(x[i, :]) - less[i]
    else:
        for i in range(len(less)):
            if 1 - norm.cdf(np.sum(x[i, :]), less[i], less_var[i]) < alpha[0]:
                test = np.sum(x[i, :]) - less[i]
                cons[i] = np.sum(x[i, :]) - less[i]

    l = len(less)
    if alpha[1] == 1:
        for i in range(len(greater)):
            test_sum1 = np.sum(x[:, i])
            if np.sum(x[:, i]) < greater[i]:
                cons[l + i] = abs(np.sum(x[:, i]) - greater[i])
    else:
        for i in range(len(greater)):
            if norm.cdf(np.sum(x[:, i]), greater[i], greater_var[i]) < alpha[1]:
                cons[l + i] = abs(np.sum(x[:, i]) - greater[i])

    if x[8] != 0:
        cons[7] = abs(x[8])

    if x[1] != 0:
        cons[8] = abs(x[1])

    if x[7] != 0:
        cons[9] = abs(x[7])

    return y, cons
