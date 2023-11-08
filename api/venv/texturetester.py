from PIL import Image
import numpy as np 
import cv2 
import os
import re
import functions as fn

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

def get_rgb_values_3x3(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")

    width, height = img.size
    section_width = width // 3
    section_height = height // 3

    rgb_sections = []

    for y in range(3):
        for x in range(3):
            # Define the coordinates for cropping each section
            left = x * section_width
            upper = y * section_height
            right = left + section_width
            lower = upper + section_height

            # Crop the image into 3x3 sections
            section = img.crop((left, upper, right, lower))

            # Get RGB values for the cropped section
            rgb_values = list(section.getdata())
            rgb_sections.append(rgb_values)

    return rgb_sections


greyscale = [[0,0,1],
             [1,2,3],
             [2,3,4]]
# 0 1 2
# 0 2 3
# 1 3 4
# print(greyscale)
# print(transpose(greyscale,3))

# menjumlahkan GLCM Mat dengan transposenya
# GLCM Mat harus matriks persegi!  
GLCM = [[1,1,0,0],
             [0,0,1,0],
             [0,0,0,2],
             [0,0,1,0]]



    
# print(normalizedMat(symmetricMat(GLCM,4),4))

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
            
            # # imgs.append(gray)
            # labels.append(normalize_label(os.path.splitext(filename)[0]))
            # descs.append(dataset_dir)

            # processedfiles += 1
            # print(f"Processedfiles{processedfiles}" )



# frameworkmat = [[0 for i in range (256)] for j in range (256)]


            # # Get the dimensions of the image
            # height, width, _ = image.shape

            # # Calculate the size of each grid cell
            # cell_height = height // 3
            # cell_width = width // 3
