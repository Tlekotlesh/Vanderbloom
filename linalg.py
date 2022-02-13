from numpy.linalg import norm
from numpy import array
from numpy.linalg import solve as solve_out_of_the_box

ab = array([
    [72,55,88,92,41, 5],
    [18,67,29,66,12, 6],
    [39,79,60,84,82, 7],
    [59,38,91,88,89, 8],
    [24,13,12,88,32, 9]
], dtype=float)

a = array([
    [72,55,88,92,41],
    [18,67,29,66,12],
    [39,79,60,84,82],
    [59,38,91,88,89],
    [24,13,12,88,32]
], dtype=float)

b = array([5, 6, 7, 8, 9], dtype=float)


def vector_gauss(ab):
    ab = ab.copy()
    d = len(ab)  # размер по старшему измерению

    # прямой
    for i in range(d):
        ab[i] = ab[i] / ab[i, i]
        for j in range(i + 1, d):
            ab[j] = ab[j] - ab[i] * ab[j, i]

    # обратный
    for i in range(d - 1, 0, -1):
        for j in range(d - 1, -1, -1):
            if i - 1 != j:
                ab[i - 1, d] -= ab[j, d] * ab[i - 1, j]

    x = ab[:, -1]  # Последний столбец
    return x


solution = vector_gauss(ab)
oob_solution = solve_out_of_the_box(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution - oob_solution, ord=1))
