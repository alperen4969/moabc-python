import numpy as np


def var_limit(var, lb, ub, imported_data):
    # var = np.array(var[0])
    # var = np.array(var)
    # if np.any(var[176:, 0] < lb[176:]):
    if np.any(var[:, 0] < lb):
        # change_pos = np.where(var[0, 176:] > ub[176:])  # [1]
        change_pos = np.where(var[:, 0] < lb)  # [1]
        change_pos = np.array(change_pos)
        # change_pos += 176
        change_pos = np.vstack(change_pos)
        var[change_pos, 0] = lb[change_pos]

    if np.any(var[176:, 0] > ub[176:]):
        change_pos = np.where(var[176:, 0] > ub[176:])  # [1]
        change_pos = np.array(change_pos)
        change_pos += 176
        change_pos = np.vstack(change_pos)
        var[change_pos, 0] = ub[change_pos]
        # var[change_pos] = ub[change_pos]

    # ub_excel = (imported_data["capfactor"] * 8760)
    ub_excel = (imported_data["capfactor"] * 8760 * imported_data['cap'])  # cap=xmax
    ub_excel = ub_excel.reshape(176)
    # if np.any(var[:176, 0] > ub_excel):
    #     change_pos = np.where(var[:176, 0] > ub_excel)
    #     change_pos = np.array(change_pos)
    #     change_pos = np.vstack(change_pos)
    #     var[change_pos, 0] = ub_excel[change_pos]
    return var
