import numpy as np

population = []

for m in range(0, 5):
    population.append({
        'mean': np.zeros((2, 1)),
        'variance': np.zeros((2, 1)),
        'cons': np.zeros((4, 1)),
        'infr': np.zeros(1),
        'capacity': 0,
        'rank': 0,
        'pui': 0,
        'pref': 0,
        'feasibility': 0,
        'distance': 0,
        'np_sets': np.empty((1, 1)),
        'sp': np.empty((1, 1)),
        'np': 0,
        'nbhd': 0,
        'twins': 0,
        'n_viol': 0,
        'parent': 0,
        'viol_sum': 0,
    })

population = np.array(population)

print("debug")
