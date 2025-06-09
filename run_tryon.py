import os
import subprocess

# Đường dẫn tới checkpoint VITONHD (nhớ tải file pytorch_model.bin vào đúng chỗ)
config_path = "./configs/VITONHD.yaml"
checkpoint_path = "./checkpoints/VITONHD/model/pytorch_model.bin"

# Kiểm tra file checkpoint
if not os.path.exists(checkpoint_path):
    print("⚠️ Không tìm thấy checkpoint! Hãy chắc chắn bạn đã tải VITONHD model vào:")
    print("→", checkpoint_path)
    exit(1)

# Chạy inference
print("🚀 Đang chạy Virtual Try-On với VITON-HD...")
subprocess.run([
    "python", "inference.py",
    "--config_p", config_path,
    "--pretrained_unet_path", checkpoint_path,
    "--save_name", "VITONHD"
])
