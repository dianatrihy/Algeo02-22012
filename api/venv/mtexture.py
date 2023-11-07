import numpy as np
import cv2
import os
import functions as fn
import time
start_time = time.time()

path = "C:/Users/Asus/Documents/Thea/SMT3/TubesAlgeo2/Algeo02-22012/dataset/73.jpg"
image = cv2.imread(path)
B,G,R = cv2.split(image)
len_row = len(image)
len_col = len(image[0])
greyscale = np.zeros((len_row, len_col))
for i in range (len_row):
    for j in range (len_col):
        greyscale[i][j] = fn.RGBtoGREYSCALE(R[i][j],G[i][j],B[i][j])
image = np.resize(image,(256,256))
# print(greyscale)
cooccurence = np.zeros((256, 256))
print("\nMatriks cooccur\n")

for i in range (len_row-1):
    for j in range(len_col-1):
        cooccurence[round(greyscale[i][j])][round(greyscale[i][j+1])]+=1

cooccurence = cooccurence + np.transpose(cooccurence)
cooccurence = fn.normalizedMat(cooccurence)

print("--- %s seconds ---" % (time.time() - start_time))