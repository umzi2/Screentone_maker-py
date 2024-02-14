import numpy as np
import random
from .dot import generetedot
from .image import int2float, float2int


class Screenton:
    def __init__(self, dot_size: int):
        dot, dot_inv = generetedot(dot_size)

        self.dot_size = dot_size
        self.dot = dot
        self.dot_inv = dot_inv

    def run(self, img: np.ndarray, rx=0, ry=0):
        try:
            img = int2float(img)
            dot_size = self.dot_size
            dot = self.dot
            dit_inv = self.dot_inv

            ly, lx = np.indices(img.shape)
            row = ly // dot_size
            column = lx // dot_size
            is_inverted = (row + column) % 2 == 1
            i = (lx + rx) % dot_size
            j = (ly + ry) % dot_size

            scr = np.select([is_inverted, ~is_inverted], [dit_inv[i, j], dot[i, j]])

            img[img < scr] = 0
            img[img >= scr] = 1

            return float2int(img)

        except RuntimeError as e:
            print(f"[FAILED] {e}")

