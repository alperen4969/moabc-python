import numpy as np


def find_grid_index(particle, grid):
    n_obj = len(particle["cost"])
    # n_grid = len(grid[0]["LB"])
    # test = grid[0]["LB"]
    n_grid = len(grid[0]["LB"])
    particle["grid_subindex"] = np.zeros((1, n_obj))  # 1, n_obj

    for j in range(0, n_obj):
        grid_subindex = particle["grid_subindex"][0, j]
        tem_part = particle["cost"][j]
        temp_grid = grid[j]
        temp_grid_ub = grid[j]["UB"]
        # xx = temp_grid_ub[0]
        # test_res = np.where(particle["cost"][j] < temp_grid_ub[0])[0][0]
        test_res = np.where(particle["cost"][j] < temp_grid_ub)
        # test_res = np.where(particle["cost"][j] < temp_grid_ub[0])
        particle["grid_subindex"][0, j] = np.where(particle["cost"][j] < temp_grid_ub)[0][0]  # [0][0]  grid[j]['UB']
        # particle["grid_subindex"][0, j] = np.where(particle["cost"][j] < temp_grid_ub[0])  # [0][0]  grid[j]['UB']
        # particle["grid_subindex"][0, j] = np.where(particle["cost"][j] < grid[j]["UB"])
        # particle.grid_sub_index[j] = np.where(particle.cost[j] < temp_grid_ub, True)[0][0]

    particle["grid_index"] = particle["grid_subindex"][0][0]
    # testx = particle["grid_subindex"][0, 0]
    for j in range(1, n_obj):
        particle["grid_index"] = particle["grid_index"] - 1
        particle["grid_index"] = n_grid * particle["grid_index"]
        particle["grid_index"] = particle["grid_index"] + particle["grid_subindex"][0, j]
        debugx = particle["grid_subindex"][0, j]

    return particle
