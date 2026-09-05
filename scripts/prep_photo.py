import sys
from pathlib import Path
from PIL import Image, ImageEnhance
import cv2, numpy as np

def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python scripts/prep_photo.py hero.png')
    src=Path(sys.argv[1]); out=Path('source-prepped.png')
    if not src.exists(): raise SystemExit(f'Input not found: {src}')
    img=Image.open(src).convert('RGBA')
    try:
        from rembg import remove
        img=remove(img)
    except ImportError:
        print('rembg not installed; keeping original background.')
    rgb=np.array(img.convert('RGB'))
    lab=cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)
    l,a,b=cv2.split(lab); l=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8)).apply(l)
    enhanced=cv2.cvtColor(cv2.merge((l,a,b)), cv2.COLOR_LAB2RGB)
    alpha=np.array(img.getchannel('A'))
    img=Image.fromarray(np.dstack((enhanced,alpha)).astype(np.uint8),'RGBA')
    bbox=img.getbbox()
    if bbox: img=img.crop(bbox)
    img.thumbnail((900,900), Image.Resampling.LANCZOS)
    img.save(out)
    print(out)
if __name__=='__main__': main()
