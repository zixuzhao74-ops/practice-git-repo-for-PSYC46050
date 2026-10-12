from IPython.display import display, Image
import pandas as pd
import os
OUTPUT_DIR = Path("Indoor_Outdoor_Images")
df = pd.read_csv(OUTPUT_DIR / 'categorization_results.csv')
img_file = df.loc[:, 'image_path']
random_file = img_file.sample(n=30).tolist()
print(random_file)
for img in random_file:
    if os.path.exists(img):
        try:
            display(Image(filename=img))
        except Exception as e:
            print(f"❌ Could not display image: {e}")