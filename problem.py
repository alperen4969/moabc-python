import numpy as np
import gep_problem


def trgep(individual, import_data):
    problem_result = gep_problem.gep_objective_function(individual, import_data)
    return problem_result


def cf1(x, imported_data):  # import data sadece gep için gerekli
    # for zdt, biliyorum kötü
    # result = zdt1(x)
    # result = zdt3(x)
    # return result
    result = trgep(x, import_data=imported_data)
    y = result
    return y

    a = 1.0
    N = 10.0
    dim = x.size
    # dim, num = x.shape
    x = np.reshape(x, (dim, 1))
    num = 1
    Y = np.zeros((dim, 1))

    test = np.tile(x[0, :], (dim - 1, 1))
    # Y[1:3, :] = (x[1:dim, :] - np.tile(x[0, :], (dim - 1, 1)) ** (
    #             0.5 + 1.5 * (np.tile(np.arange(2, dim + 1), (1, 1)).T - 2.0) / (dim - 2.0))) ** 2

    testx = np.tile(x[0, :], (dim - 1, 1))
    test2 = np.tile(x[0, :], (dim-1, 1))
    test = np.tile(np.arange(2, dim + 1), (1, 1)).T - 2.0
    test_g = x[1:dim, :]
    step1 = x[1:dim, :] - np.tile(x[0, :], (dim - 1, 1))
    step2 = 0.5 + 1.5 * (np.tile(np.arange(2, dim + 1), (1, 1)).T - 2.0) / (dim - 2.0)
    # result = (step1 ** step2) ** 2
    result2 = np.power(step1, step2, dtype=complex)
    result3 = np.power(result2, 2, dtype=complex)
    result_oy = (x[1:dim, :] - np.tile(x[0, :], (dim - 1, 1)) ** (
                0.5 + 1.5 * (np.tile(np.arange(2, dim + 1), (1, 1)).T - 2.0) / (dim - 2.0))) ** 2
    # Y[1:3, :] = (step1 ** step2) ** 2
    Y[1:3, :] = result_oy

    tmp1_test = Y[2:dim:2, :]
    tmp1 = np.sum(Y[2:dim:2, :])  # odd index
    tmp2 = np.sum(Y[1:dim:2, :])  # even index

    y = np.zeros((2, num))
    lennn = len(range(3, dim, 2))
    y[0, :] = x[0, :] + 2.0 * tmp1 / 1  # len(range(3, dim, 2))
    y[1, :] = 1.0 - x[0, :] + 2.0 * tmp2 / 1  # len(range(2, dim, 2))

    c = y[0, :] + y[1, :] - a * np.abs(np.sin(N * np.pi * (y[0, :] - y[1, :] + 1.0))) - 1.0

    penalty = 10000 * np.maximum(-c, 0)
    y[0, :] += penalty
    y[1, :] += penalty

    return y


def zdt1(individual):  # zdt1
    dim = individual.size
    x = np.reshape(individual, (dim, 1))  # 3,1
    # dim = 3
    # dim = 30
    num = 1
    y = np.zeros((2, num))
    g = 1.0 + 9.0 * sum(individual[1:]) / (len(individual) - 1)
    f1 = individual[0]
    if not f1 >= 0:
        f1 = 0
    # print(f"{f1} ve {g}")
    f2 = g * (1 - np.sqrt(f1 / g))
    y[0, :] = f1
    y[1, :] = f2
    return y


def bnh(x):
    y = np.zeros((2, 1))  # num : 1
    f1 = 4 * x[:, 0] ** 2 + 4 * x[:, 1] ** 2
    f2 = (x[:, 0] - 5) ** 2 + (x[:, 1] - 5) ** 2
    g1 = (1 / 25) * ((x[:, 0] - 5) ** 2 + x[:, 1] ** 2 - 25)
    g2 = -1 / 7.7 * ((x[:, 0] - 8) ** 2 + (x[:, 1] + 3) ** 2 - 7.7)
    y[0, :] = f1 + g1
    y[1, :] = f2 + g2
    return y


def zdt3(x):
    dim = 30
    y = np.zeros((2, 1))  # num : 1
    g = 1 + 9 * np.sum(x[1:dim]) / (dim-1)
    y[0, :] = x[0]
    y[1, :] = g * (1 - np.sqrt(x[0] / g) - x[0] / g * np.sin(10 * np.pi * x[0]))
    return y


def main():
    # x = np.array((0.5, 0.7, 0.35))
    dfrx = (0.800068480224308, 0.431413827463545, 0.910647594429523)
    x = np.reshape(dfrx, (3, 1))
    # x = np.transpose(dfrx)
    # x = np.reshape(x, (3,1))
    # print(cf1_x(x))
    # print(cf1_for(x))
    # print(CF1_3(x))


if __name__ == "__main__":
    main()


