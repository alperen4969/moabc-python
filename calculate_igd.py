import numpy as np


# measure for performance of MOABC
def calculate_igd(tpf, pf):
    npf = np.size(pf,2)
    ntpf = np.size(tpf,2)
    temp = np.inf
    sum_distance = 0
    for i in range(1, ntpf):
        for j in range(1, npf):
            # distance = np.norm(tp[f:,i] transpose - pf[:,j] transpose)  # TODO, transpose
            distance = np.linalg.norm(tpf[:, i] - pf[:, j])
            if temp > distance:
                temp = distance
        sum_distance = sum_distance + temp
        temp = np.inf
    igd = sum_distance/ntpf

    return igd
