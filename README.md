# PromptDresser Virtual Try-On (VITON-HD)

This is a simplified wrapper for PromptDresser (https://github.com/rlawjdghek/PromptDresser) to try image-based virtual try-on with lingerie or any apparel.

## Setup

```bash
conda create -n promptdresser python=3.10
conda activate promptdresser
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r environment.txt
