import numpy as np
import init


def send_scout_bees(x_range, foods, max_trial, imported_data):
    foods = np.array(foods)
    trials = np.array([food["trial"] for food in foods])
    # [random.random() for _ in range(n_var)]
    index = np.where(trials > max_trial)  # foods["trial"]
    # index = [1, 2]  # for debugging
    # test_nenzero = np.count_nonzero(index)
    if np.count_nonzero(index):
        # print(foods[index])
        # foods[index] = init.init(foods[index], x_range, imported_data)  # for CF1
        # foods[index] = init.init_gep(foods[index], imported_data)  # for GEP, boundary problemli şu an TODO
        temp_foods = np.zeros(28)
        debug_list = init.pop_from_exist(temp_foods, imported_data)
        foods[index] = np.array(init.pop_from_exist(temp_foods, imported_data))[0]
        # print(foods[index])
        # print("/")
    return foods

