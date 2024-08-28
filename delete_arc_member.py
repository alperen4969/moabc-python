import numpy as np


def delete_arc_member(archive):
    archive = np.array(archive)
    GI = np.array([indv["grid_index"] for indv in archive])
    OC = np.unique(GI)  # TODO: ??
    N = np.zeros(np.size(OC))
    for k in range(0, len(OC)):
        test_search = np.where(GI == OC[k])
        N[k] = len(np.where(GI == OC[k])[0])  # numel TODO

    for k in range(0, len(OC)):
        if N[k] > 1:
            GI = np.array([indv["grid_index"] for indv in archive])
            OC = np.unique(GI)
            # SCM = np.where(GI == OC[k])  # [1]
            SCM = GI == OC[k]
            index = left_corner(archive, SCM)
            SCM[index] = 0
            archive = np.delete(archive, SCM)
    return archive


def left_corner(archive, SCM):
    index = None
    SCM = np.array(SCM)
    points = np.where(SCM == 1)   # bu 1?
    members = archive[points]
    temp = np.inf
    for i in range(0, len(members)):
        cost = abs(members[i]["cost"][0])
        if temp > cost:
            temp = cost
            index = i

    listx = np.where(SCM == 1)[0]
    index = listx[index]

    return index
