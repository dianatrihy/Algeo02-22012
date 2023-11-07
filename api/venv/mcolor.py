import numpy as np
import cv2
import os
import functions
import math

path = "C:/Users/Asus/Documents/Thea/SMT3/TubesAlgeo2/Algeo02-22012/dataset/73.jpg"
image = cv2.imread(path)
print(image)
B,G,R = cv2.split(image)
# cv2.imshow("Blue",B)
# cv2.waitKey(0)
# cv2.imshow("Green",G)
# cv2.waitKey(0)
# cv2.imshow("Red",R)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print("WARNA BIRU")
print(B)
print("WARNA HIJAU")
print(G)
print("WARNA MERAH")
print(R)


def vectorlen(vectorarr):
    result = 0
    for i in range (len(vectorarr)):
        result+=vectorarr[i]*vectorarr[i]
    return math.sqrt(result)

def cosinesimilarity(vector1,vector2):
    result = 0
    for i in range (len(vector1)):
        result+=vector1[i]*vector2[i]
    return result/(vectorlen(vector1)*vectorlen(vector2))
    

print("\n Normalisasi matriks RGB\n")
matB = B/255
matG = G/255
matR = R/255

# Cmax = np.max(matB,matG,matR)
# print(Cmax)
print("\nMatriks CMAX\n")
Cmax = np.maximum.reduce([matG,matB,matR])
print(Cmax)
print("\nMatriks CMIN\n")
Cmin = np.minimum.reduce([matG,matB,matR])
print(Cmin)

print("\nMatriks Delta\n")
Subtract = np.subtract(Cmax,Cmin)
print(Subtract)

len_row = len(Subtract)
len_col = len(Subtract[0])

matH = np.zeros((len_row, len_col))
matS = np.zeros((len_row, len_col))
for i in range (len_row):
    for j in range (len_col):
        if (Subtract[i][j]==0):
            matH[i][j] = 0
        elif (Cmax[i][j]==matR[i][j]):
            matH[i][j] = 60*(((matG[i][j]-matB[i][j])/Subtract[i][j])%6)
        elif ((Cmax[i][j])==matG[i][j]):
            matH[i][j] = 60*(((matB[i][j]-matR[i][j])/Subtract[i][j])+2)
        elif ((Cmax[i][j])==matG[i][j]):
            matH[i][j] = 60*(((matR[i][j]-matG[i][j])/Subtract[i][j])+4)
        if (Cmax[i][j]==0):
            matS[i][j] = 0
        elif (Cmax[i][j]!=0):
            matS[i][j] = Subtract[i][j]/Cmax[i][j]
matV = Cmax

print("\nMatriks H\n")
print(matH)
print("\nMatriks S\n")
print(matS)
print("\nMatriks V\n")
print(matV)

veclanjar = []


print(np.shape(matB))
print(np.shape(B))