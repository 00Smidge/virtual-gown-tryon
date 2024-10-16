import cv2
import numpy as np
from PIL import Image


# Set this up to automate image resizing
def resize():
    img_loc = "./abandoned_bus.jpeg"
    img_pillow = Image.open(img_loc)
    new_img_size = (img_pillow.size[0] // 10, img_pillow.size[1] // 10)
    img_resize = img_pillow.resize(new_img_size)

    img_cv = np.array(img_resize)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

    cv2.imshow("Resized Img:", img_cv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
