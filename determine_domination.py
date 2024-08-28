import dominates as dominates
import numpy as np


def determine_domination(pop):
    # print("/")
    # print("/")
    n_pop = len(pop)  # must equal to 10
    for i in range(0, n_pop):
        pop[i]["is_dominated"] = False

    for i in range(0, n_pop - 1):
        for j in range(i+1, n_pop):
            if dominates.dominates(pop[i], pop[j]):
                pop[j]["is_dominated"] = True
                # pop[j]["trial"] = pop[j]["trial"] + 1

            if dominates.dominates(pop[j], pop[i]):
                pop[i]["is_dominated"] = True
                # pop[i]["trial"] = pop[i]["trial"] + 1
    # for i in (1, 3, 5):  # for debugging
    #     pop[i]["is_dominated"] = False
    return pop


def non_dominated_sorting(pop):  # for archive
    pop_size = len(pop)
    domination_set = [[] for _ in range(pop_size)]
    dominated_count = [0 for _ in range(pop_size)]
    F = [[]]
    for i in range(pop_size):
        for j in range(i + 1, pop_size):
            # if i dominates j
            if dominates.dominates(pop[i], pop[j]):
                domination_set[i].append(j)
                dominated_count[j] += 1
            # if j dominates i
            elif dominates.dominates(pop[j], pop[i]):
                domination_set[j].append(i)
                dominated_count[i] += 1
        # If i is not dominated at all
        if dominated_count[i] == 0:
            pop[i]['rank'] = 0
            F[0].append(i)
    # Pareto Counter
    k = 0
    while True:
        Q = []
        for i in F[k]:
            for j in domination_set[i]:
                dominated_count[j] -= 1
                if dominated_count[j] == 0:
                    pop[j]['rank'] = k + 1
                    Q.append(j)
        if not Q:
            break
        F.append(Q)
        k += 1
    return pop, F


def sort_population(pop):  # for archive
    # pop = sorted(pop, key=lambda x: (x["trial"]))  # "rank"
    pop = sorted(pop, key=lambda x: (x['rank'], -x['crowding_distance']))
    max_rank = pop[-1]['rank']
    F = []
    for r in range(max_rank + 1):
        F.append([i for i in range(len(pop)) if pop[i]['rank'] == r])
    return pop, F


def truncate_population(pop, F):
    pop_size = 50  # int(len(pop))
    if len(pop) <= pop_size:
        return pop, F
    pop = pop[:pop_size]
    for k in range(len(F)):
        F[k] = [i for i in F[k] if i < pop_size]
    return pop, F


def calc_crowding_distance(foods, F):
    pareto_count = len(F)
    n_obj = len(foods[0]["cost"])
    for k in range(pareto_count):
        costs = np.array([np.reshape(foods[i]["cost"],2) for i in F[k]])
        n = len(F[k])
        d = np.zeros((n, n_obj))
        for j in range(n_obj):
            idx = np.argsort(costs[:, j])
            d[idx[0], j] = np.inf
            d[idx[-1], j] = np.inf
            for i in range(1, n - 1):
                d[idx[i], j] = costs[idx[i + 1], j] - costs[idx[i - 1], j]
                debug1 = costs[idx[-1], j]
                debug2 = costs[idx[0], j]
                debug3 = d[idx[i], j]
                d[idx[i], j] /= costs[idx[-1], j] - costs[idx[0], j]
        for i in range(n):
            temp = sum(d[i, :])
            foods[F[k][i]]['crowding_distance'] = sum(d[i, :])
    # pop = punish_twins(pop)
    return foods
