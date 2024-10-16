import os
ls = os.listdir("dataset/train/S");
for name in ls:
    os.rename(f"dataset/train/S/{name}", f"dataset/train/S/image_{name.split(".")[0]}.jpg")