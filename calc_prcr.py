import numpy as np


def calc_pr_discrete(guy1, guy2, k, ro):
    guy1["variance"] = np.array(guy1["variance"])
    guy1["mean"] = np.array(guy1["mean"])
    n_p = len(guy1["variance"][:])
    pr = 0

    for i in range(n_p):
        pr += np.sum(guy1["variance"][i, k] > guy2["variance"][:, k]) * \
              np.exp(ro[k] * ((guy1["variance"][i, k] - guy1["mean"][k]) / guy1["mean"][k]))

    pr = pr / (n_p ** 2)
    return pr
