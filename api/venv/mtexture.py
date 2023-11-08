from PIL import Image
import numpy as np 
import cv2
import os
import time
import functions as fn
import texture as tex
start_time = time.time()


# membaca image inputan untuk dibandingkan
# mainimage = "C:/Users/Asus/Pictures/Smiling cat.jpg"
mainimage = "C:/Users/Asus/Documents/Thea/SMT3/TubesAlgeo2/Algeo02-22012/perforated/perforated_0105.jpg"
mimage = cv2.imread(mainimage)
len_row = len(mimage)
len_col = len(mimage[0])
mgreyscale = tex.konversigray(mimage)
mcooccurence = tex.createcooccurence(mgreyscale)
mtoople = fn.vectorcosine(mcooccurence) 
print(mtoople)


# baca semua image di dataset
dataset_dir = "C:/Users/Asus/Documents/Thea/SMT3/TubesAlgeo2/Algeo02-22012/perforated"
processedfiles = 0
final = []
# Check if the dataset directory exists
if os.path.exists(dataset_dir) and os.path.isdir(dataset_dir):
    image_files = os.listdir(dataset_dir)
    
    for filename in image_files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(dataset_dir, filename)
            image = cv2.imread(img_path)
            len_row = len(image)
            len_col = len(image[0])
            greyscale = tex.konversigray(image)
            cooccurence = tex.createcooccurence(greyscale)
            toople = fn.vectorcosine(cooccurence) 
            # print(toople)
            # final.append(fn.cosinesimilarity(mtoople,toople))
            print(fn.cosinesimilarity(mtoople,toople))
            processedfiles += 1
            # print(f"Processedfiles{processedfiles}" )
final.sort()
print(final)
print("--- %s seconds ---" % (time.time() - start_time))