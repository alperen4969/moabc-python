import numpy as np


def x_boundary(name, dim, imported_data):  # name can be removed because it's not necessary for CF1
    if name == "CF1":
        range_boundary = np.ones((dim, 2))  # 3x2 matrix for CF1
        range_boundary[:, 0] = 0
    else:
        ub_excel = (imported_data["capfactor"] * 8760 * imported_data['cap'])
        ub_excel = ub_excel.reshape(176)

        range_boundary = np.zeros((dim, 2))
        range_boundary[:, 1] = np.inf
        # range_boundary[176:, 1] = imported_data["ub"][176:]
        # range_boundary[:176, 1] = ub_excel

    return range_boundary  # GEP için kullanılmıyor aslında, refactor lazım
