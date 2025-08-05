from icrawler.builtin import BingImageCrawler
import os

# Step 1: Ask for inputs
keyword = input("🔍 What unsafe image do you want? (e.g., 'man bleeding', 'gun violence'): ").strip()
num = int(input("📸 How many images do you want? (e.g., 150): "))
folder = input("📁 Enter full path where you want to download images:\n(Eg: C:\\Users\\YourName\\Desktop\\my_folder)\n👉 ").strip()

# Step 2: Create folder if it doesn't exist
os.makedirs(folder, exist_ok=True)

# Step 3: Crawl and download images
crawler = BingImageCrawler(storage={"root_dir": folder})
crawler.crawl(keyword=keyword, max_num=num)

print(f"\n✅ Downloaded {num} images for '{keyword}' into folder:\n{folder}")
