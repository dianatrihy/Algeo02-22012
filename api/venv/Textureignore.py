import numpy as np 
import cv2 
import os
import re

# -------------------- Utility function ------------------------
def normalize_label(str_):
    str_ = str_.replace(" ", "")
    str_ = str_.translate(str_.maketrans("","", "()"))
    str_ = str_.split("_")
    return ''.join(str_[:2])

def normalize_desc(folder, sub_folder):
    text = folder + " - " + sub_folder 
    text = re.sub(r'\d+', '', text)
    text = text.replace(".", "")
    text = text.strip()
    return text

# baris = 3
# kolom = 4
# Matriks1 = [[0 for i in range (baris)] for j in range (kolom)]
# for kolom in range (n):
#     for baris in range (n):
#         Matriks1[baris][kolom] = int(input())
# def transpose(Matriks,brs,kol):
#     idxbaris = 0
#     while idxbaris<
#     for baris in range (brs):
#         idxkolom = 0
#         for kolom in range (kol):
#             if ()
#             idxkolom = idxkolom + 1
#         idxbaris = idxbaris + 1

def RGBtoGREYSCALE(R,G,B):
    res = 0.29*R + 0.587*G + 0.114*B
    return res


# -------------------- Load Dataset ------------------------
 
dataset_dir = "C:/Users/Asus/Documents/Thea/SMT3/TubesAlgeo2/Algeo02-22012/dataset1"

imgs = [] #list image matrix 
labels = []
descs = []
# for folder in os.listdir(dataset_dir):
#     for sub_folder in os.listdir(os.path.join(dataset_dir, folder)):
#         sub_folder_files = os.listdir(os.path.join(dataset_dir, folder, sub_folder))
#         len_sub_folder = len(sub_folder_files) - 1

# define variables for checking progress
processedfiles = 0
# Check if the dataset directory exists
if os.path.exists(dataset_dir) and os.path.isdir(dataset_dir):
    image_files = os.listdir(dataset_dir)
    
    for filename in image_files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(dataset_dir, filename)
            img = cv2.imread(img_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # h, w = gray.shape
            # ymin, ymax, xmin, xmax = h//2, h*2//2, w//2, w*2//2
            # crop = gray[ymin:ymax, xmin:xmax]
            # resize = cv2.resize(crop, (0,0), fx=0.5, fy=0.5)
            
            imgs.append(gray)
            labels.append(normalize_label(os.path.splitext(filename)[0]))
            descs.append(dataset_dir)

            processedfiles += 1
            print(f"Processedfiles{processedfiles}" )


# preview the image, show that it works.
# cv2.imshow("test img", imgs[0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# Matrix greyscale

# greyscale = [[0 for i in range (3) ] for j in range (3)]
# print(processedfiles)
# for i in range (processedfiles):
#     height, width, _ = image[].shape

#             # # Get the dimensions of the image
#             # height, width, _ = image.shape

#             # # Calculate the size of each grid cell
#             # cell_height = height // 3
#             # cell_width = width // 3
