import numpy as np
import dominates
import problem
import copy
import reshape_variables
import var_limit
import plot_costs


def send_employed_bees(x_range, foods, archive, imported_data):
    # print("/")
    # print("/")
    food_number = len(foods)
    w1 = .9  # TODO ??
    for i in range(0, food_number):
        food = foods[i]
        d = np.random.randint(0, x_range.shape[0])
        r = np.random.randint(0, len(archive))
        # d, r = 0, 0  # for debugging, ayrıca indexlere -1 uygulandı
        leader = archive[r]
        # leader = archive[0]
        new_food = copy.deepcopy(food)
        # print(new_food)
        # new_food["position"][d] = (new_food["position"][d] + w1 * unifrnd(-1, 1) * (new_food["position"][d] - leader["position"][d]))
        det_num = -0.806539948438266  # for debugging
        # for d in range(len(new_food["position"])):  # len(new_food["position"])/88, 4
        #     # d = np.random.randint(0, x_range.shape[0])
        #     new_food["position"][d] += w1 * np.random.uniform(-1, 1) * (new_food["position"][d] - leader["position"][d])
        #     new_food["position"] = np.round(new_food["position"])
        #     new_food["position"] = var_limit.var_limit(new_food["position"], imported_data['lb'], imported_data['ub'], imported_data)
        # plot_costs.plot_costs(foods, archive, imported_data)
        trial_ratio = new_food["trial"] / imported_data["max_trial"]
        # pop_ratio = len(foods) / len(archive)
        new_food["position"][d] += w1 * np.random.uniform(-1, 1) * (new_food["position"][d] - leader["position"][d])
        new_food["position"] = np.round(new_food["position"])
        new_food["position"] = var_limit.var_limit(new_food["position"], imported_data['lb'], imported_data['ub'], imported_data)

        # debug_range = max(x_range[d, 0], min(new_food["position"][d], x_range[d, 1]))
        # if np.any(new_food["position"][176:, 0] > imported_data["ub"][176:]):
        #     new_food["position"][d] = max(x_range[d, 0], min(new_food["position"][d], x_range[d, 1]))

        # new_food["position"][d] += w1 * det_num * (new_food["position"][d] - leader["position"][d])
        # newfood["position"][d] = max(x_range[d, 1], min(newfood["position"][d], x_range[d, 2]))
        # new_food["cost"] = cost_func(new_food["position"])
        new_food["cost"], violation = problem.cf1(new_food["position"], imported_data)  # returns : new_food["trial"]
        # new_food['position_str'] = reshape_variables.reshape_variables_moabc(new_food['position'])  # for TRGEP

        if dominates.dominates(new_food, food):
            food["position"] = new_food["position"]
            food["cost"] = new_food["cost"]
            food["position_str"] = reshape_variables.reshape_variables_moabc(new_food['position'])  # for TRGEP
            food["trial"] = 0
            food["is_dominated"] = False
        else:
            food["trial"] = food["trial"] + 1
            # if violation > 0:
            #     food["trial"] += 25
        foods[i] = food
    # plot_costs.plot_costs(foods, archive, imported_data)
    return foods



