import numpy as np
import determine_domination
import create_grid
import find_grid_index
import delete_arc_member


def update_archive(archive, foods, epsilon, alpha):
    nondom_food = [food for food in foods if not food["is_dominated"]]
    archive = np.concatenate((archive, nondom_food))
    archive = determine_domination.determine_domination(archive)
    archive = [arc for arc in archive if not arc["is_dominated"]]
    # grid = create_grid.create_grid(archive, epsilon, alpha)
    # for i in range(0, len(archive)):
    #     archive[i] = find_grid_index.find_grid_index(archive[i], grid)
    archive = delete_arc_member.delete_arc_member(archive)

    return archive

