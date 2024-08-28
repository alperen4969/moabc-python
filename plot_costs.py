import matplotlib.pyplot as plt
import numpy as np
import init
import problem


def plot_costs(pop, archive, imported_data):
    pop_costs = np.array([indv["cost"] for indv in pop])
    plt.scatter(pop_costs[:, 0, 0], pop_costs[:, 1, 0], c="red", s=20)  # scatter : plot
    # plt.scatter(pop_costs[:, 0, 0], pop_costs[:, 1, 0], 'bo', s=4)  # scatter : plot

    rep_costs = np.array([indv["cost"] for indv in archive])
    # plt.scatter(rep_costs[0, :], rep_costs[1, :], 'm*', s=4)
    # plt.scatter(rep_costs[0, :], rep_costs[1, :], c="purple", s=20, alpha=0.9)
    plt.scatter(rep_costs[:, 0, 0], rep_costs[:, 1, 0], c="blue", s=5, alpha=1)

    # temp_pop = np.zeros(28)
    # existed_pop_initial = init.pop_from_exist(temp_pop, imported_data)
    # resut_exist = [problem.cf1(indiv["position"], imported_data) for indiv in existed_pop_initial]
    # all_initial_pop = np.array([resut_exist[i] for i in range(len(temp_pop))])
    # plt.scatter(all_initial_pop[:, 0], all_initial_pop[:, 1], c="purple", s=15, alpha=0.3)

    plt.xlabel('1st Objective - Cost')
    plt.ylabel('2nd Objective - Emission')

    plt.show()
