from torch.utils.data import DataLoader
from scripts.data_prep import SegmentationDataset


dataset = SegmentationDataset(img_dir="dataset/images", mask_dir="dataset/masks")
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)
