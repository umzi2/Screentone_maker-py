import numpy as np


def int2float(int_array) -> np.ndarray:
    if int_array.ndim != 2:
        int_array = rgb_to_gray(int_array)
    float_array = np.array(int_array).astype(np.float32) / 255
    return float_array


def float2int(float_array) -> np.ndarray:
    int_array = (float_array * 255).astype(np.uint8)
    return int_array


def rgb_to_gray(img_rgb) -> np.ndarray:
    return np.dot(img_rgb[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
