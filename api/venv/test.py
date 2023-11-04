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

def print_progress(val, val_len, folder, sub_folder, filename, bar_size=10):
    progr = "#"*round((val)*bar_size/val_len) + " "*round((val_len - (val))*bar_size/val_len)
    if val == 0:
        print("", end = "\n")
    else:
        print("[%s] folder : %s/%s/ ----> file : %s" % (progr, folder, sub_folder, filename), end="\r")
        

# -------------------- Load Dataset ------------------------
 
dataset_dir = "C:/Users/Asus/Documents/Thea/SMT3/TubesAlgeo2/Algeo02-22012/dataset1"

imgs = [] #list image matrix 
labels = []
descs = []
# for folder in os.listdir(dataset_dir):
#     for sub_folder in os.listdir(os.path.join(dataset_dir, folder)):
#         sub_folder_files = os.listdir(os.path.join(dataset_dir, folder, sub_folder))
#         len_sub_folder = len(sub_folder_files) - 1

# Check if the dataset directory exists
processedfiles = 0
totalfiles = 0
if os.path.exists(dataset_dir) and os.path.isdir(dataset_dir):
    image_files = os.listdir(dataset_dir)
    
    for filename in image_files:
        # Check if the file is an image (e.g., checking for file extensions like .jpg, .png, etc.)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(dataset_dir, filename)
            img = cv2.imread(img_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            h, w = gray.shape
            ymin, ymax, xmin, xmax = h//2, h*2//2, w//2, w*2//2
            crop = gray[ymin:ymax, xmin:xmax]
            resize = cv2.resize(crop, (0,0), fx=0.5, fy=0.5)
            
            imgs.append(resize)
            labels.append(normalize_label(os.path.splitext(filename)[0]))
            descs.append(dataset_dir)  # Change this according to your requirement

            # Update and print progress
            processedfiles += 1
            # print("Processedfiles" + processedfiles)
            print(f"Processedfiles{processedfiles}" )
            # print_progress(processedfiles, totalfiles, '', '', filename)  # No folder or sub_folder info available


cv2.imshow("test img", imgs[0])

cv2.waitKey(0)
cv2.destroyAllWindows()