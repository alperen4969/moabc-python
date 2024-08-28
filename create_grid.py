import numpy as np


def create_grid(archive, epsilon, alpha):
    c = np.array([indv["cost"][0] for indv in archive])  # TODO: ?
    c2 = np.array([indv["cost"][1] for indv in archive])
    c = np.hstack((c, c2))
    # c_min = min(c, [], 2)
    # c_max = max(c, [], 2)
    # c_min = np.min(c, axis=0, initial=2)
    c_min = np.nanmin(c, axis=0)
    # c_min = np.argmin(c, axis=1)
    c_max = np.nanmax(c, axis=0)
    # c_max = np.amax(c, axis=1)
    dc = c_max - c_min
    c_min = c_min - (alpha * dc)
    c_max = c_max + (alpha * dc)
    n_obj = np.size(c, 1)
    # EMPTY_GRID
    # grid = np.tile(empty_grid, n_obj)
    grid = []
    for m in range(2):
        empty_grid = {
            "LB": [],
            "UB": []
        }
        grid.append(empty_grid)

    # grid = np.reshape(grid, (2 ,1))

    for j in range(0, n_obj):
        # debug_diff = c_max[j] - c_min[j]
        # debug_diff = debug_diff / 1069
        # debug_diff = debug_diff / 106900
        # debug_diff = np.round(debug_diff)
        # debug_diff = debug_diff.astype(int)
        # n = debug_diff
        # n_debug = np.round((c_max[j] - c_min[j]))
        n = np.round((c_max[j] - c_min[j]) / epsilon)
        # n = (n / 999999) / epsilon
        # n = np.round(n)
        n = n.astype(int)
        # n = (debug_diff / epsilon).astype(int)
        # n = 1868817  # for debugging
        # DEBUG_VAR = np.array(([14520500.62532596, 8640614.80602015]))  # for debugging, positive olmalı
        # n = 10000000
        # cj = np.linspace(c_min[j], c_max[j], n + 1)
        n = 100
        cj = np.linspace(c_min[j], c_max[j], n)
        # cj = np.reshape(cj, cj.size)
        temp_a = [-np.inf]
        temp_b = np.array([np.inf])
        grid[j]["LB"] = np.concatenate((temp_a, cj))
        grid[j]["UB"] = np.concatenate((cj, temp_b))

    return grid
