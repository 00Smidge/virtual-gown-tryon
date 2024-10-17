import torch
import numpy as np


def img_to_tensor(image):
    img_arr = np.array(image)  # Convert to NumPy array
    img_tsr = (
        torch.from_numpy(img_arr).permute(2, 0, 1).float() / 255.0
    )  # Normalize and reorder dimensions
    return img_tsr
