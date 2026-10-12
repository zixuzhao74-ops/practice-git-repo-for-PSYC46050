from IPython.display import display, Image
import pandas as pd
from pathlib import Path
import os

def random_img_selection(OUTPUT_DIR):
    df = pd.read_csv(OUTPUT_DIR / 'categorization_results.csv')
    img_file = df.loc[:, 'image_path']
    random_file = img_file.sample(n=30).tolist()
    print(random_file)
    
    img_root = Path.home() / 'Desktop'
    
    for img in random_file:
        img_path = img_root / img
        if img_path.is_file():
            try:
                display(Image(filename=str(img_path)))
            except Exception as e:
                print(f"❌ Could not display image: {img_path}")