import numpy as np
import random as random
import problem
import scipy.io as sio
import copy
import reshape_variables
import pandas as pd
import var_limit


def init(foods, x_range, imported_data):
    food_number = len(foods)  # todo: numel'di # must equal to 20
    pops = []
    NN = food_number
    # dim = np.size(x_range, 0)
    dim = x_range.shape[0]

    # points = ((np.tile(x_range[:, 0], [0, NN]) + np.tile((x_range[:, 1] - x_range[:, 0]), [0, NN])) * np.random.rand(dim, NN))
    # points = np.random.rand(dim, food_number) * (x_range[:, 1] - x_range[:, 0]) + x_range[:, 0]
    debug0 = x_range[:, 0]
    tile1 = np.tile(x_range[:, 0], (20, 1))
    tile2 = np.tile(x_range[:, 1] - x_range[:, 0], (1, 20))

    points = np.transpose(np.tile(x_range[:, 0], (NN, 1))) + np.transpose(np.tile(x_range[:, 1] - x_range[:, 0], (NN, 1))) * np.random.rand(dim, NN)
    points = np.array(points)

    # debug_foods = sio.loadmat('foods.mat')["foods"]
    # m = 0
    # test1 = debug_foods[m, 0][0][:,  0]
    # test2 = points[:, m]
    # test_len = len(foods)

    # for m in range(len(foods)):
    #     points[:, m] = debug_foods[m, 0][0][:,  0]

    # for debugging
    # dfrx = (0.800068480224308, 0.431413827463545, 0.910647594429523)
    # x = np.reshape(dfrx, (3, 1))
    # points = x
    # food_number = 1
    # debugging son
    for i in range(0, food_number):
        # foods[i]["position"] = points[:, i]
        # print(foods[i]["position"])  # for debug
        # # foods[i]["cost"] = cost_function.cf1[foods[i]["position"]]
        # foods[i]["cost"] = problem.cf1(foods[i]["position"])
        # foods[i]["is_dominated"] = False
        indv = {"position": points[:, i], "cost": [], "trial": 0, "is_dominated": False, "grid_index": [], "grid_subindex": []}
        # üstteki orijinal, indv debugging
        # indv = {"position": points, "cost": [], "trial": 0, "is_dominated": False, "grid_index": [], "grid_subindex": []}
        # foods[i]["cost"] = cost_function.cf1[foods[i]["position"]]
        indv["cost"] = problem.cf1(indv["position"], imported_data)
        indv["is_dominated"] = False
        pops.append(indv)
    # return foods
    return pops


def init_gep(foods, imported_data):
    # nd(352,1) olmalı positiobs
    food_number = len(foods)  # todo: numel'di # must equal to 20
    # dim = x_range.shape[0]
    population = []
    pop_size = food_number
    for i in range(pop_size):
        lower_bound = np.array([0] * 352)  # .astype(int)
        ub_excel = (imported_data["capfactor"] * 8760 * imported_data["cap"] * 10)
        ub_excel = ub_excel.reshape(176)
        ub_inv = np.array(imported_data["ub"][176:352])
        ub_inv = ub_inv.reshape(176)
        ubx = np.hstack((ub_excel, ub_inv))  # axis = 1 for horizantally
        variables = np.array([lower_bound[j] + random.random() *
                              (ubx[j] - lower_bound[j]) for j in range(len(lower_bound))])
        variables = variables.reshape(352, 1)
        # variables[0, 176:352] = np.round(variables[0, 176:352])
        variables = np.round(variables)
        # variables = var_limit.var_limit(variables, imported_data['lb'], imported_data['ub'])
        new_copy_variables = copy.deepcopy(variables)
        new_copy_variables = var_limit.var_limit(new_copy_variables, imported_data['lb'], imported_data['ub'], imported_data)
        # new_copy_variables = new_copy_variables.T  # gerek kalmadı
        temp_cost, _ = problem.cf1(new_copy_variables, imported_data)
        # temp_cost = random.random(), random.random()
        population.append({
            'position': new_copy_variables,
            'position_str': reshape_variables.reshape_variables_moabc(new_copy_variables),
            'cost': temp_cost,  # np.zeros((2, 1)),
            "trial": 0,
            "is_dominated": False,
            "grid_index": [],
            "grid_subindex": [],
            "pui": 0,
            "nbhds": []
        })
    population = np.array(population)
    whole_pop = population
    return whole_pop


def pop_from_exist(foods, imported_data):  # args: imported_data, opt
    food_number = len(foods)  # todo: numel'di # must equal to 20
    pop_size = food_number
    # dim = x_range.shape[0]
    # num_var = 352
    # exist_pop = sio.loadmat("existed_pop.mat")  # trgep
    exist_pop = sio.loadmat("28_existed.mat")  # trgep
    exist_pop_size = exist_pop["temp_var"].size  # 28
    population = []
    existed_array = exist_pop["temp_var"]
    for i in range(0, exist_pop_size):
        variables = existed_array[0, i]  # TEST TODO [0]
        new_copy_variables = copy.deepcopy(variables)
        new_copy_variables = new_copy_variables.T
        temp_cost, violation = problem.cf1(new_copy_variables, imported_data)
        trial_init = 0
        if violation > 0:
            trial_init = 999

        # temp_cost = random.random(), random.random()
        population.append({
            'position': new_copy_variables,
            'position_str': reshape_variables.reshape_variables_moabc(new_copy_variables),
            'cost': temp_cost,  # np.zeros((2, 1)),
            "trial": trial_init,
            "is_dominated": False,
            "grid_index": [],
            "grid_subindex": [],
            "rank": 0
        })
    lack_pop_size = pop_size - 28
    if lack_pop_size > 0:
        temp_arr = np.ones(lack_pop_size)
        lack_pop = init_gep(temp_arr, imported_data)
        population = np.array(population)
        whole_pop = np.concatenate((population, lack_pop))
    else:
        whole_pop = population
    return whole_pop  # nd(352,1)
