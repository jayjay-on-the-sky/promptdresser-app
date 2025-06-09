import os
import argparse
import subprocess

# === 1. Argument parser ===
parser = argparse.ArgumentParser(description="Run virtual try-on with PromptDresser (VITON-HD)")
parser.add_argument("--person", type=str, required=True, help="Name of person image (in data/test_fine/image/)")
parser.add_argument("--cloth", type=str, required=True, help="Name of cloth image (in data/test_fine/cloth/)")
parser.add_argument("--save_name", type=str, default="VITONHD", help="Name of result folder/output")

args = parser.parse_args()

# === 2. Paths ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "configs/VITONHD.yaml")
CHECKPOINT_PATH = os.path.join(BASE_DIR, "checkpoints/VITONHD/model/pytorch_model.bin")

# Input paths
person_img = os.path.join(BASE_DIR, "data/test_fine/image", args.person)
cloth_img = os.path.join(BASE_DIR, "data/test_fine/cloth", args.cloth)
pairs_txt = os.path.join(BASE_DIR, "data/test_fine/test_pairs.txt")

# === 3. Sanity checks ===
if not os.path.exists(CHECKPOINT_PATH):
    raise FileNotFoundError("❌ Missing checkpoint: " + CHECKPOINT_PATH)

if not os.path.exists(person_img):
    raise FileNotFoundError("❌ Missing person image: " + person_img)

if not os.path.exists(cloth_img):
    raise FileNotFoundError("❌ Missing cloth image: " + cloth_img)

# === 4. Create mask folders if not exist ===
folders = ["cloth-mask", "image-densepose", "image-parse", "openpose-img"]
for folder in folders:
    path = os.path.join(BASE_DIR, "data/test_fine", folder)
    os.makedirs(path, exist_ok=True)

# === 5. Update test_pairs.txt ===
with open(pairs_txt, "w") as f:
    f.write(f"{args.person} {args.cloth}\n")

# === 6. Run inference ===
print(f"🚀 Running try-on: {args.person} with {args.cloth}")
subprocess.run([
    "python", "inference.py",
    "--config_p", CONFIG_PATH,
    "--pretrained_unet_path", CHECKPOINT_PATH,
    "--save_name", args.save_name
])
