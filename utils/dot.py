import numpy as np
import math


def generetedot(dot_size) -> (np.ndarray, np.ndarray):
    dot_inv = np.zeros((dot_size, dot_size)).astype("float32")
    point = (dot_size / 2 + 0.1, dot_size / 2 + 0.15)
    step = ((1. - 0.5) / (dot_size ** 2 - 1))
    for i in range(dot_size):
        for d in range(dot_size):
            a = math.sqrt((i - point[0]) ** 2 + (d - point[1]) ** 2)
            dot_inv[i, d] = a

    coordinates_and_values = [(i, j, dot_inv[i, j]) for i in range(dot_inv.shape[0]) for j in
                              range(dot_inv.shape[1])]
    sorted_coordinates_and_values = sorted(coordinates_and_values, key=lambda x: x[2], reverse=True)
    n = 0

    for i, j, value in sorted_coordinates_and_values:
        s = 0.5 - (step * n)
        dot_inv[i, j] = s
        n += 1

    dot = np.copy(dot_inv) * (-1) + 1

    return dot, dot_inv + .003
