import numpy as np

from .dot import generetedot
from .image import int2float, float2int


class Screenton:
    def __init__(self, dot_size: int):
        dot, dot_inv = generetedot(dot_size)

        self.dot_size = dot_size
        self.dot = dot
        self.dot_inv = dot_inv

    def run(self, img: np.ndarray):
        try:

            img = int2float(img)
            dot_size = self.dot_size
            dot = self.dot
            dit_inv = self.dot_inv
            for ly in range(img.shape[0]):
                for lx in range(img.shape[1]):
                    row = ly // dot_size
                    column = lx // dot_size
                    is_inverted = (row + column) % 2 == 1
                    i = lx % dot_size
                    j = ly % dot_size

                    scr = dot
                    if is_inverted:
                        scr = dit_inv
                    if img[ly, lx] < scr[i, j]:
                        img[ly, lx] = 0
                    else:
                        img[ly, lx] = 1
            return float2int(img)
        except RuntimeError as e:
            return print(f"[FAILED] {e}")
