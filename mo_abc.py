import numpy as np
import init as init
import determine_domination
import pui_nbhd
import population
import send_onlooker_bees
import send_employed_bees
import send_scout_bees
import create_grid
import find_grid_index
import update_archive
import x_boundary
import plot_costs
import import_excel

n_var = 352  # 352 for GEP, 30 for ZDT1, 3 for CF1
var_size = [1, n_var]
n_pop = 100  # 56(sadece initial pop) ya da 84,  50 for ZDT1, ABC, bunu 2'ye bölüyor, 28'lik init kullanılıyor TRGEP için şu an
n_archive = 100
food_number = round(n_pop/2)
n_employed_bee = food_number
n_onlooker_bee = food_number
epsilon = .001  # TODO: .001 şeklinde CF1
alpha = 0.1
max_trial = 100  # 100 for ZDT1?
max_iter = 500

empty_food = {
    "position": [],
    "cost": [],
    "trial": 0,
    "is_dominated": False,
    "grid_index": [],
    "grid_subindex": []
}

imported_data = import_excel.import_excel()
imported_data["max_trial"] = max_trial
x_range = x_boundary.x_boundary("TRGEP", n_var, imported_data)  # "CF1"
# foods = np.reshape(empty_food, (food_number, 0))
foods = np.tile(empty_food, food_number)  # kullanılmıyor
# extra_foods = np.tile(empty_food, 28)  # kullanılmıyor
# foods = init.init(foods, x_range, imported_data)  # for cf1
foods = init.pop_from_exist(foods, imported_data)  # for GEP
# foods = population.init_eps()  # for EPS
# foods = init.init_gep(foods, imported_data)  # for GEP, args: x_range
# foods = init.init_gep(foods, imported_data)  # multi hive denemesi
# extra_foods = init.init_gep(foods, imported_data)  # for GEP, args: x_range  # multi hive denemesi
# foods = determine_domination.determine_domination(foods)
# debug1 = [food["is_dominated"] for food in foods]
# [pop[i]["mean"] for i in range(len(pop))]
# archive = foods[not [for i in foods["is_dominated"]]]
# archive = [food for food in foods if not food["is_dominated"]]
# grid = create_grid.create_grid(archive, epsilon, alpha)

# for i in range(len(archive)):
#     archive[i] = find_grid_index.find_grid_index(archive[i], grid)
foods = np.array(foods)
foods, F = determine_domination.non_dominated_sorting(foods)
foods = determine_domination.calc_crowding_distance(foods, F)
archive = foods[F[0]]

# extra_foods = np.array(extra_foods)
# extra_foods, F_extra = determine_domination.non_dominated_sorting(extra_foods)
# extra_foods = determine_domination.calc_crowding_distance(extra_foods, F_extra)
# extra_archive = extra_foods[F_extra[0]]
# plot_costs.plot_costs(foods, archive, imported_data)

'''  LOOP  '''
for gen in range(0, max_iter):
    # bir süre dursun GEP için, commented
    foods = send_scout_bees.send_scout_bees(x_range, foods, max_trial, imported_data)
    # extra_foods = send_scout_bees.send_scout_bees(x_range, extra_foods, max_trial, imported_data)
    # sometimes, commented for determitistic debugging
    foods = send_employed_bees.send_employed_bees(x_range, foods, archive, imported_data)
    # extra_foods = send_scout_bees.send_scout_bees(x_range, extra_foods, max_trial, imported_data)
    # foods = determine_domination.determine_domination(foods)
    # foods, F = determine_domination.non_dominated_sorting(foods)
    # foods = send_scout_bees.send_scout_bees(x_range, foods, max_trial, imported_data)
    foods = send_onlooker_bees.send_onlooker_bees(x_range, foods, imported_data, cost_func=None)
    # extra_foods = send_scout_bees.send_scout_bees(x_range, extra_foods, max_trial, imported_data)
    # foods = determine_domination.determine_domination(foods)
    # foods, F = determine_domination.sort_population(foods)
    # archive = update_archive.update_archive(archive, foods, epsilon, alpha)
    # plot_costs.plot_costs(foods, archive, imported_data)

    foods, F = determine_domination.non_dominated_sorting(foods)
    # foods = pui_nbhd.pui_nbhd(foods)
    # foods = pui_nbhd.pui_nbhd_v2(foods)
    # foods = pui_nbhd.pui_nbhd(foods, opt)
    foods = determine_domination.calc_crowding_distance(foods, F)
    archive, _ = determine_domination.sort_population(archive)
    foods = np.array(foods)
    archive = foods[F[0]]

    # foods = np.concatenate((foods, archive))
    # foods, F = determine_domination.sort_population(foods)
    # foods, F = determine_domination.truncate_population(foods, F)
    # foods = np.array(foods)
    # archive = foods[F[0]]

    # extra_foods, F_extra = determine_domination.non_dominated_sorting(extra_foods)
    # extra_foods = determine_domination.calc_crowding_distance(extra_foods, F_extra)
    # extra_foods, F_extra = determine_domination.sort_population(extra_foods)
    # extra_archive, _ = determine_domination.sort_population(extra_archive)
    # extra_foods = np.array(extra_foods)
    # extra_archive = extra_foods[F_extra[0]]
    # archive = update_archive.update_archive(archive, foods, epsilon, alpha)

    # ratio_colonies = len(archive) + 1 / len(extra_archive) +1
    # whole_archive = np.concatenate((archive, extra_archive))
    # whole_foods = np.concatenate((foods, extra_foods))
    # whole_archive, F_whole = determine_domination.non_dominated_sorting(whole_archive)
    # whole_archive = determine_domination.calc_crowding_distance(whole_archive, F_whole)
    # whole_foods, F_whole = determine_domination.sort_population(whole_foods)
    # whole_archive, _ = determine_domination.sort_population(whole_archive)
    # whole_foods = np.array(whole_foods)
    # whole_archive = whole_foods[F_whole[0]]
    # extra_archive = whole_archive
    # plot_costs.plot_costs(foods, archive, imported_data)
    # bundan sonrası experimental, (öncesi değil zaten)
    # combinepop = foods
    # foods, F = determine_domination.sort_population(combinepop)
    # results = np.array([foods[i]["cost"] for i in F[0]])
    # foods, F = determine_domination.truncate_population(foods, F)

    # TODO: print for stats
    # print(f"{gen}")
    print(f'Iteration = {gen}, Number of Archive Members = {len(archive)}')

plot_costs.plot_costs(foods, archive, imported_data)
