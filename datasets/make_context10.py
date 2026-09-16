import os
import random
from pathlib import Path
import shutil
from tqdm import tqdm

def make_context10(root, out_context_root, context_ratio=0.1, seed=42):
    root = Path(root)

    out_context = Path(out_context_root)
    (out_context / "images").mkdir(parents=True, exist_ok=True)
    (out_context / "masks").mkdir(parents=True, exist_ok=True)


    jpgs = sorted([p for p in root.glob("*.jpg")])
    pngs = sorted([p for p in root.glob("*.png")])

   
    imgs = {p.stem: p for p in jpgs}
    masks = {p.stem: p for p in pngs}

  
    keys = sorted(list(set(imgs.keys()) & set(masks.keys())))
    print(f"Found {len(keys)} valid image-mask pairs.")

    # 10%
    random.seed(seed)
    n_context = int(len(keys) * context_ratio)
    context_set = set(random.sample(keys, n_context))

    print(f"Sampling {n_context} samples for context10 ...")

    for k in tqdm(context_set, desc="Copying to context"):
        img_src = imgs[k]
        mask_src = masks[k]

        img_dst = out_context / "images" / f"{k}.jpg"
        mask_dst = out_context / "masks" / f"{k}.png"

        shutil.copy(img_src, img_dst)
        shutil.copy(mask_src, mask_dst)

        img_src.unlink()
        mask_src.unlink()

    print(f"Done! Context saved at {out_context}")
    print(f"Remaining 90% kept in {root}")


if __name__ == "__main__":

    root = "'./train"

    out_context_root = "./context"

    make_context10(root, out_context_root)
