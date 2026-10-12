import os, shutil
from PIL import Image

src = Image.open("icon-512.png").convert("RGBA")
res = "android/app/src/main/res"
sizes = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}

for d, px in sizes.items():
    folder = f"{res}/mipmap-{d}"
    os.makedirs(folder, exist_ok=True)
    im = src.resize((px, px), Image.LANCZOS)
    for name in ("ic_launcher.png", "ic_launcher_round.png", "ic_launcher_foreground.png"):
        im.save(f"{folder}/{name}")

# remove the default adaptive icon so our logo is used as is
shutil.rmtree(f"{res}/mipmap-anydpi-v26", ignore_errors=True)
print("icons done")
