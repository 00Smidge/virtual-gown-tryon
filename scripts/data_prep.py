import os
import torch
from PIL import Image
from torch.utils.data import Dataset
from scripts.img_to_tensor import img_to_tensor
from scripts.resize import resize


class SegmentationDataset(Dataset):
    def __init__(self, img_dir, mask_dir, transform=None):
        self.img_dir = img_dir
        self.mask_dir = mask_dir
        self.transform = transform
        self.imgs = os.listdir(img_dir)

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, idx) -> tuple[torch.Tensor, torch.Tensor]:
        img_path = os.path.join(self.img_dir, self.imgs[idx])
        mask_path = os.path.join(
            self.mask_dir, self.imgs[idx].replace(".jpg", "_mask.png")
        )

        image = Image.open(img_path).convert("RGB")
        mask = Image.open(mask_path).convert("L")

        image = resize(image, 5)
        mask = resize(mask, 5)

        image_tsr = img_to_tensor(image)
        mask_tsr = img_to_tensor(mask)

        return image_tsr, mask_tsr
