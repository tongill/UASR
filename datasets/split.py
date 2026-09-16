import os
import random
import shutil


root = ""        
out_root = ""  
# ============================

os.makedirs(out_root, exist_ok=True)

for d in ["ph2_train", "ph2_val", "ph2_test"]:
    os.makedirs(os.path.join(out_root, d), exist_ok=True)


random.seed(42)

all_pairs = []

def collect_from(split_name):
    folder = os.path.join(root, split_name)
    if not os.path.isdir(folder):
        print(f"[warning] : {folder}")
        return
    files = os.listdir(folder)
    jpgs = [f for f in files if f.lower().endswith(".jpg")]
    for jpg in jpgs:
        base = os.path.splitext(jpg)[0]    
        png = base + ".png"
        if png in files:
            jpg_path = os.path.join(folder, jpg)
            png_path = os.path.join(folder, png)
            all_pairs.append((split_name, jpg_path, png_path))
        else:
            print(f"[warning] {folder} {png}， {jpg}")

for s in ["ph2_train", "ph2_val", "ph2_test"]:
    collect_from(s)

total = len(all_pairs)
print(f"total {total}  (jpg+png)")


random.shuffle(all_pairs)


n_train = 80
n_val = 20
n_test = total - (n_train + n_val)  

print(f"train={n_train}, val={n_val}, test={n_test}")

train_pairs = all_pairs[:n_train]
val_pairs = all_pairs[n_train:n_train + n_val]
test_pairs = all_pairs[n_train + n_val:]


def copy_and_renumber(pairs, split_name):

    out_dir = os.path.join(out_root, split_name)
    pairs_sorted = sorted(pairs, key=lambda x: x[1])
    for new_id, (_, jpg_path, png_path) in enumerate(pairs_sorted, start=1):
        new_jpg = os.path.join(out_dir, f"{new_id}.jpg")
        new_png = os.path.join(out_dir, f"{new_id}.png")
        shutil.copy(jpg_path, new_jpg)
        shutil.copy(png_path, new_png)

copy_and_renumber(train_pairs, "ph2_train")
copy_and_renumber(val_pairs, "ph2_val")
copy_and_renumber(test_pairs, "ph2_test")

print("ok")
print(f"  ph2_train: {len(train_pairs)}  1~{len(train_pairs)}）")
print(f"  ph2_val:   {len(val_pairs)}  1~{len(val_pairs)}）")
print(f"  ph2_test:  {len(test_pairs)}  1~{len(test_pairs)}）")