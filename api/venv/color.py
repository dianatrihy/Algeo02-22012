import numpy as np
import cv2
import time
import functions as fn

start_time = time.time()

# path = "C:\Users\HP\tubes-algeo2\dataset\0.jpg"
image = cv2.imread("C:/Users/Asus/Documents/Thea/SMT3/TubesAlgeo2/Algeo02-22012/perforated/white.jpg")

R = [[0 for i in range(len(image[0]))] for j in range (len(image))]
G = [[0 for i in range(len(image[0]))] for j in range (len(image))]
B = [[0 for i in range(len(image[0]))] for j in range (len(image))]

# denorm
for i in range (len(image)):
    for j in range (len(image[0])):
        R[i][j] = image[i][j][2] / 255
        G[i][j] = image[i][j][1] / 255
        B[i][j] = image[i][j][0] / 255

# resize
R = np.resize(R,(256,256))
G = np.resize(G,(256,256))
B = np.resize(B,(256,256))

# find cmax, cmin, delta
Cmax = [[0 for i in range(256)] for j in range (256)]
Cmin = [[0 for i in range(256)] for j in range (256)]
delta = [[0 for i in range(256)] for j in range (256)]

for i in range (256):
    for j in range (256):
        Cmax[i][j] = max(R[i][j],G[i][j],B[i][j])
        Cmin[i][j] = min(R[i][j],G[i][j],B[i][j])
        delta[i][j] = Cmax[i][j] - Cmin[i][j]

# convert to hsv
H = [[0 for i in range(256)] for j in range (256)]
S = [[0 for i in range(256)] for j in range (256)]
V = [[0 for i in range(256)] for j in range (256)]

for i in range (256):
    for j in range (256):
        if (delta[i][j] == 0):
            H[i][j] = 0
        elif (Cmax[i][j] == R[i][j]):
            H[i][j] = 60 * (((G[i][j]-B[i][j])/delta[i][j]) % 6)
        elif (Cmax[i][j] == G[i][j]):
            H[i][j] = 60 * (((B[i][j]-R[i][j])/delta[i][j]) + 2)
        elif (Cmax[i][j] == B[i][j]):
            H[i][j] = 60 * (((R[i][j]-G[i][j])/delta[i][j]) + 4)
        
        if (Cmax[i][j] == 0):
            S[i][j] = 0
        else:
            S[i][j] = delta[i][j]/Cmax[i][j]
        
        V[i][j] = Cmax[i][j]

# slicing into 3x3
H = np.array(H)
S = np.array(S)
V = np.array(V)

H1 = H[0:85, 0:85]
S1 = S[0:85, 0:85]
V1 = V[0:85, 0:85]

H2 = H[0:85, 85:170]
S2 = S[0:85, 85:170]
V2 = V[0:85, 85:170]

H3 = H[0:85, 170:256]
S3 = S[0:85, 170:256]
V3 = V[0:85, 170:256]

H4 = H[85:170, 0:85]
S4 = S[85:170, 0:85]
V4 = V[85:170, 0:85]

H5 = H[85:170, 85:170]
S5 = S[85:170, 85:170]
V5 = V[85:170, 85:170]

H6 = H[85:170, 170:256]
S6 = S[85:170, 170:256]
V6 = V[85:170, 170:256]

H7 = H[170:256, 0:85]
S7 = S[170:256, 0:85]
V7 = V[170:256, 0:85]

H8 = H[170:256, 85:170]
S8 = S[170:256, 85:170]
V8 = V[170:256, 85:170]

H9 = H[170:256, 170:256]
S9 = S[170:256, 170:256]
V9 = V[170:256, 170:256]

def formula_H(arr, H):
    for i in range (len(H)):
        for j in range (len(H[0])):
            if (H[i][j] >= 316 and H[i][j] <= 360):
                arr[0] += 1
            elif (H[i][j] >= 1 and H[i][j] < 26):
                arr[1] += 1
            elif (H[i][j] >= 26 and H[i][j] < 41):
                arr[2] += 1
            elif (H[i][j] >= 41 and H[i][j] < 121):
                arr[3] += 1
            elif (H[i][j] >= 121 and H[i][j] < 191):
                arr[4] += 1
            elif (H[i][j] >= 191 and H[i][j] < 271):
                arr[5] += 1
            elif (H[i][j] >= 271 and H[i][j] < 295):
                arr[6] += 1
            elif (H[i][j] >= 295 and H[i][j] < 316):
                arr[7] += 1
            
def formula_S(arr, S):
    for i in range (len(S)):
        for j in range (len(S[0])):
            if (S[i][j] >= 0 and S[i][j] < 0.2):
                arr[8] += 1
            elif (S[i][j] >= 0.2 and S[i][j] < 0.7):
                arr[9] += 1
            elif (S[i][j] >= 0.7 and S[i][j] <= 1):
                arr[10] += 1   
    
def formula_V(arr, V):
    for i in range (len(V)):
        for j in range (len(V[0])):
            if (V[i][j] >= 0 and V[i][j] < 0.2):
                arr[11] += 1
            elif (V[i][j] >= 0.2 and V[i][j] < 0.7):
                arr[12] += 1
            elif (V[i][j] >= 0.7 and V[i][j] <= 1):
                arr[13] += 1    

array1 = [0 for i in range(14)]
formula_H(array1, H1)
formula_S(array1, S1)
formula_V(array1, V1)

array2 = [0 for i in range(14)]
formula_H(array2, H2)
formula_S(array2, S2)
formula_V(array2, V2)

array3 = [0 for i in range(14)]
formula_H(array3, H3)
formula_S(array3, S3)
formula_V(array3, V3)

array4 = [0 for i in range(14)]
formula_H(array4, H4)
formula_S(array4, S4)
formula_V(array4, V4)

array5 = [0 for i in range(14)]
formula_H(array5, H5)
formula_S(array5, S5)
formula_V(array5, V5)

array6 = [0 for i in range(14)]
formula_H(array6, H6)
formula_S(array6, S6)
formula_V(array6, V6)

array7 = [0 for i in range(14)]
formula_H(array7, H7)
formula_S(array7, S7)
formula_V(array7, V7)

array8 = [0 for i in range(14)]
formula_H(array8, H8)
formula_S(array8, S8)
formula_V(array8, V8)

array9 = [0 for i in range(14)]
formula_H(array9, H9)
formula_S(array9, S9)
formula_V(array9, V9)

array = np.concatenate([array1, array2, array3, array4, array5, array6, array7, array8, array9])

print(array)

print("--- %s seconds ---" % (time.time() - start_time))





# array = np.array([[1,2,3,4,5,6,7],
#                         [1,2,3,4,5,6,7],
#                         [1,2,3,4,5,6,7],
#                         [1,2,3,4,5,6,7]])

# array1 = array[0:2, 0:2]
# array2 = array[0:2, 2:4]
# array3 = array[0:2, 4:7]

# print(array1)
# print(array2)
# print(array3)


            

    
