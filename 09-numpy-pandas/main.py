import numpy as np
from numpy import linalg

if __name__ == '__main__':
    m1 = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
    m2 = np.array([1, -2, 0])
    solution = linalg.solve(m1, m2)
    print('x = {}, y = {}, z = {}'.format(round(solution[0], 3),
                                          round(solution[1], 3),
                                          round(solution[2], 3)))
    print(np.allclose(np.dot(m1, solution),m2))