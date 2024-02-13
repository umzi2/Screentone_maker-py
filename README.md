```py
import cv2
from utils.screentone import Screenton

if __name__ == "__main__":
    dot_size = 7
    screenton_img = Screenton(dot_size)
    img = cv2.imread("1_18000.png")
    sc_img = screenton_img.run(img)
    cv2.imwrite("1.png", sc_img)
```
