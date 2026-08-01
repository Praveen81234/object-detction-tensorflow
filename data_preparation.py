import os
import random
import shutil

def split_images(base_dir="data/images", train_dir="data/train", val_dir="data/val", split_ratio=0.8):
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    images = [f for f in os.listdir(base_dir) if f.endswith(".jpg") or f.endswith(".png")]
    random.shuffle(images)
    split_index = int(len(images) * split_ratio)
    train_images = images[:split_index]
    val_images = images[split_index:]

    for img in train_images:
        shutil.copy(os.path.join(base_dir, img), os.path.join(train_dir, img))
    for img in val_images:
        shutil.copy(os.path.join(base_dir, img), os.path.join(val_dir, img))

if __name__ == "__main__":
    split_images()