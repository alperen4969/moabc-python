import numpy as np
import dominates
import roulette_wheel_selection
import problem
import copy
import reshape_variables
import var_limit
# elitin seçiminde pui

def send_onlooker_bees(x_range, foods, imported_data, cost_func):
    # print("/")
    # print("/")
    n = len(foods)
    dom = np.zeros((1, n))
    for i in range(0, n):
        for j in range(i+1, n):
            if dominates.dominates(foods[i], foods[j]):
                dom[0, i] = dom[0, i] + 1
            else:
                dom[0, j] = dom[0, j] + 1
    fit = dom / n
    testsum = np.sum(fit)
    p = fit / testsum  # sum(fit)

    w2 = .2
    for i in range(0, n):
        food = foods[i]
        d = np.random.randint(0, x_range.shape[0])
        # d = 1  # for debugging, ayrıca indexlere -1 uygulandı
        index = roulette_wheel_selection.roulette_wheel_selection(p)
        leader = foods[index]
        # new_food = food  # !
        new_food = copy.deepcopy(food)
        # det_num = 0.2  # for debugging
        # new_food["position"][d] += w2 * np.random.uniform(-1, 1) * (new_food["position"][d] - leader["position"][d])
        trial_ratio = new_food["trial"] / imported_data["max_trial"]
        new_food["position"][d] += w2 * (trial_ratio * np.random.uniform(-1, 1)) * (new_food["position"][d] - leader["position"][d])
        new_food["position"] = np.round(new_food["position"])
        new_food["position"] = var_limit.var_limit(new_food["position"], imported_data['lb'], imported_data['ub'], imported_data)
        # new_food["position"][d] += w2 * det_num * (new_food["position"][d] - leader["position"][d])
        # test_poss = max(x_range[d, 0], min(new_food["position"][d], x_range[d, 1]))
        # new_food["position"][d] = max(x_range[d, 0], min(new_food["position"][d], x_range[d, 1]))
        new_food["cost"], violation = problem.cf1(new_food["position"], imported_data)  # returns : new_food["trial"]
        # new_food['position_str'] = reshape_variables.reshape_variables_moabc(new_food['position'])   # for TRGEP

        if dominates.dominates(new_food, food):
            food["position"] = new_food["position"]
            food["position_str"] = reshape_variables.reshape_variables_moabc(new_food['position'])   # for TRGEP
            food["cost"] = new_food["cost"]
            food["trial"] = 0
            food["is_dominated"] = False
        else:
            food["trial"] = food["trial"] + 1
            # if violation > 0:
            #     food["trial"] += 50
        foods[i] = food
    return foods
