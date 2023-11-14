import numpy as np
import cv2
import time
import functions as fn
from PIL import Image
import os

start_time = time.time()

# path = "C:\Users\HP\tubes-algeo2\dataset\0.jpg"
# image = cv2.imread("C:/Users/HP/tubes-algeo2/dataset/0.jpg")

def RGBtoHSV(path, re, H, S, V):
    image = Image.open(path)

    width, height = image.size
    new_size = (width//2, height//2)
    resized_image = image.resize(new_size)

    resized_image.save('compressed_image.jpg', optimize=True, quality=50)

    imageC = cv2.imread('compressed_image.jpg')

    # imageC = cv2.imread(path)

    print(len(imageC))

    # R = [[0 for i in range(re)] for j in range (re)]
    # G = [[0 for i in range(re)] for j in range (re)]
    # B = [[0 for i in range(re)] for j in range (re)]

    # # denorm
    # for i in range (re):
    #     for j in range (re):
    #         R[i][j] = imageC[i][j][2] / 255
    #         G[i][j] = imageC[i][j][1] / 255
    #         B[i][j] = imageC[i][j][0] / 255

    # image = np.resize(image, (256,256))
    R = [[0 for i in range(len(imageC[0]))] for j in range (len(imageC))]
    G = [[0 for i in range(len(imageC[0]))] for j in range (len(imageC))]
    B = [[0 for i in range(len(imageC[0]))] for j in range (len(imageC))]

    # denorm
    for i in range (len(imageC)):
        for j in range (len(imageC[0])):
            R[i][j] = imageC[i][j][2] / 255
            G[i][j] = imageC[i][j][1] / 255
            B[i][j] = imageC[i][j][0] / 255

    # resize
    R = np.resize(R,(re,re))
    G = np.resize(G,(re,re))
    B = np.resize(B,(re,re))

    # find cmax, cmin, delta
    Cmax = [[0 for i in range(re)] for j in range (re)]
    Cmin = [[0 for i in range(re)] for j in range (re)]
    delta = [[0 for i in range(re)] for j in range (re)]

    for i in range (re):
        for j in range (re):
            Cmax[i][j] = max(R[i][j],G[i][j],B[i][j])
            Cmin[i][j] = min(R[i][j],G[i][j],B[i][j])
            delta[i][j] = Cmax[i][j] - Cmin[i][j]

    # convert to hsv
    for i in range (re):
        for j in range (re):
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

def color(Ha, Sa, Va, path2):
    re = 200
    Hb = [[0 for i in range(re)] for j in range (re)]
    Sb = [[0 for i in range(re)] for j in range (re)]
    Vb = [[0 for i in range(re)] for j in range (re)]
    # RGBtoHSV(path1, re, Ha, Sa, Va)
    RGBtoHSV(path2, re, Hb, Sb, Vb)
    print("--- %s seconds ---" % (time.time() - start_time))

    Ha = np.array(Ha)
    Sa = np.array(Sa)
    Va = np.array(Va)

    Hb = np.array(Hb)
    Sb = np.array(Sb)
    Vb = np.array(Vb)

    re1 = re // 4
    re2 = re // 4 * 2
    re3 = re // 4 * 3
    re4 = re

    H = fn.cosinesimilarity(np.ravel(Ha[0:re1, 0:re1]), np.ravel(Hb[0:re1, 0:re1]))
    H += fn.cosinesimilarity(np.ravel(Ha[0:re1, re1:re2]), np.ravel(Hb[0:re1, re1:re2]))
    H += fn.cosinesimilarity(np.ravel(Ha[0:re1, re2:re3]), np.ravel(Hb[0:re1, re2:re3]))
    H += fn.cosinesimilarity(np.ravel(Ha[0:re1, re3:re4]), np.ravel(Hb[0:re1, re3:re4]))
    H += fn.cosinesimilarity(np.ravel(Ha[re1:re2, 0:re1]), np.ravel(Hb[re1:re2, 0:re1]))
    H += fn.cosinesimilarity(np.ravel(Ha[re1:re2, re1:re2]),np.ravel(Hb[re1:re2, re1:re2]))
    H += fn.cosinesimilarity(np.ravel(Ha[re1:re2, re2:re3]), np.ravel(Hb[re1:re2, re2:re3]))
    H += fn.cosinesimilarity(np.ravel(Ha[re1:re2, re3:re4]), np.ravel(Hb[re1:re2, re3:re4]))
    H += fn.cosinesimilarity(np.ravel(Ha[re2:re3, 0:re1]), np.ravel(Hb[re2:re3, 0:re1]))
    H += fn.cosinesimilarity(np.ravel(Ha[re2:re3, re1:re2]), np.ravel(Hb[re2:re3, re1:re2]))
    H += fn.cosinesimilarity(np.ravel(Ha[re2:re3, re2:re3]), np.ravel(Hb[re2:re3, re2:re3]))
    H += fn.cosinesimilarity(np.ravel(Ha[re2:re3, re3:re4]), np.ravel(Hb[re2:re3, re3:re4]))
    H += fn.cosinesimilarity(np.ravel(Ha[re3:re4, 0:re1]), np.ravel(Hb[re3:re4, 0:re1]))
    H += fn.cosinesimilarity(np.ravel(Ha[re3:re4, re1:re2]), np.ravel(Hb[re3:re4, re1:re2]))
    H += fn.cosinesimilarity(np.ravel(Ha[re3:re4, re2:re3]), np.ravel(Hb[re3:re4, re2:re3]))
    H += fn.cosinesimilarity(np.ravel(Ha[re3:re4, re3:re4]), np.ravel(Hb[re3:re4, re3:re4]))
    meanH = H / 16

    S = fn.cosinesimilarity(np.ravel(Sa[0:re1, 0:re1]), np.ravel(Sb[0:re1, 0:re1]))
    S += fn.cosinesimilarity(np.ravel(Sa[0:re1, re1:re2]), np.ravel(Sb[0:re1, re1:re2]))
    S += fn.cosinesimilarity(np.ravel(Sa[0:re1, re2:re3]), np.ravel(Sb[0:re1, re2:re3]))
    S += fn.cosinesimilarity(np.ravel(Sa[0:re1, re3:re4]), np.ravel(Sb[0:re1, re3:re4]))
    S += fn.cosinesimilarity(np.ravel(Sa[re1:re2, 0:re1]), np.ravel(Sb[re1:re2, 0:re1]))
    S += fn.cosinesimilarity(np.ravel(Sa[re1:re2, re1:re2]),np.ravel(Sb[re1:re2, re1:re2]))
    S += fn.cosinesimilarity(np.ravel(Sa[re1:re2, re2:re3]), np.ravel(Sb[re1:re2, re2:re3]))
    S += fn.cosinesimilarity(np.ravel(Sa[re1:re2, re3:re4]), np.ravel(Sb[re1:re2, re3:re4]))
    S += fn.cosinesimilarity(np.ravel(Sa[re2:re3, 0:re1]), np.ravel(Sb[re2:re3, 0:re1]))
    S += fn.cosinesimilarity(np.ravel(Sa[re2:re3, re1:re2]), np.ravel(Sb[re2:re3, re1:re2]))
    S += fn.cosinesimilarity(np.ravel(Sa[re2:re3, re2:re3]), np.ravel(Sb[re2:re3, re2:re3]))
    S += fn.cosinesimilarity(np.ravel(Sa[re2:re3, re3:re4]), np.ravel(Sb[re2:re3, re3:re4]))
    S += fn.cosinesimilarity(np.ravel(Sa[re3:re4, 0:re1]), np.ravel(Sb[re3:re4, 0:re1]))
    S += fn.cosinesimilarity(np.ravel(Sa[re3:re4, re1:re2]), np.ravel(Sb[re3:re4, re1:re2]))
    S += fn.cosinesimilarity(np.ravel(Sa[re3:re4, re2:re3]), np.ravel(Sb[re3:re4, re2:re3]))
    S += fn.cosinesimilarity(np.ravel(Sa[re3:re4, re3:re4]), np.ravel(Sb[re3:re4, re3:re4]))
    meanS = S / 16

    V = fn.cosinesimilarity(np.ravel(Va[0:re1, 0:re1]), np.ravel(Vb[0:re1, 0:re1]))
    V += fn.cosinesimilarity(np.ravel(Va[0:re1, re1:re2]), np.ravel(Vb[0:re1, re1:re2]))
    V += fn.cosinesimilarity(np.ravel(Va[0:re1, re2:re3]), np.ravel(Vb[0:re1, re2:re3]))
    V += fn.cosinesimilarity(np.ravel(Va[0:re1, re3:re4]), np.ravel(Vb[0:re1, re3:re4]))
    V += fn.cosinesimilarity(np.ravel(Va[re1:re2, 0:re1]), np.ravel(Vb[re1:re2, 0:re1]))
    V += fn.cosinesimilarity(np.ravel(Va[re1:re2, re1:re2]),np.ravel(Vb[re1:re2, re1:re2]))
    V += fn.cosinesimilarity(np.ravel(Va[re1:re2, re2:re3]), np.ravel(Vb[re1:re2, re2:re3]))
    V += fn.cosinesimilarity(np.ravel(Va[re1:re2, re3:re4]), np.ravel(Vb[re1:re2, re3:re4]))
    V += fn.cosinesimilarity(np.ravel(Va[re2:re3, 0:re1]), np.ravel(Vb[re2:re3, 0:re1]))
    V += fn.cosinesimilarity(np.ravel(Va[re2:re3, re1:re2]), np.ravel(Vb[re2:re3, re1:re2]))
    V += fn.cosinesimilarity(np.ravel(Va[re2:re3, re2:re3]), np.ravel(Vb[re2:re3, re2:re3]))
    V += fn.cosinesimilarity(np.ravel(Va[re2:re3, re3:re4]), np.ravel(Vb[re2:re3, re3:re4]))
    V += fn.cosinesimilarity(np.ravel(Va[re3:re4, 0:re1]), np.ravel(Vb[re3:re4, 0:re1]))
    V += fn.cosinesimilarity(np.ravel(Va[re3:re4, re1:re2]), np.ravel(Vb[re3:re4, re1:re2]))
    V += fn.cosinesimilarity(np.ravel(Va[re3:re4, re2:re3]), np.ravel(Vb[re3:re4, re2:re3]))
    V += fn.cosinesimilarity(np.ravel(Va[re3:re4, re3:re4]), np.ravel(Vb[re3:re4, re3:re4]))
    meanV = V / 16

    return (meanH + meanS + meanV) / 3

# path1 = "C:/Users/HP/tubes-algeo2/dataset/1.jpg"
# path2 = "C:/Users/HP/tubes-algeo2/dataset/2.jpg"
# path3 = "C:/Users/HP/tubes-algeo2/dataset/3.jpg"
# print(color(path1, path2))
# print(color(path1, path3))
    # def formula_H(arr, H):
    #     for i in range (len(H)):
    #         for j in range (len(H[0])):
    #             if (H[i][j] >= 316 and H[i][j] <= 360):
    #                 arr[0] += 1
    #             elif (H[i][j] >= 1 and H[i][j] < 26):
    #                 arr[1] += 1
    #             elif (H[i][j] >= 26 and H[i][j] < 41):
    #                 arr[2] += 1
    #             elif (H[i][j] >= 41 and H[i][j] < 121):
    #                 arr[3] += 1
    #             elif (H[i][j] >= 121 and H[i][j] < 191):
    #                 arr[4] += 1
    #             elif (H[i][j] >= 191 and H[i][j] < 271):
    #                 arr[5] += 1
    #             elif (H[i][j] >= 271 and H[i][j] < 295):
    #                 arr[6] += 1
    #             elif (H[i][j] >= 295 and H[i][j] < 316):
    #                 arr[7] += 1
                
    # def formula_S(arr, S):
    #     for i in range (len(S)):
    #         for j in range (len(S[0])):
    #             if (S[i][j] >= 0 and S[i][j] < 0.2):
    #                 arr[8] += 1
    #             elif (S[i][j] >= 0.2 and S[i][j] < 0.7):
    #                 arr[9] += 1
    #             elif (S[i][j] >= 0.7 and S[i][j] <= 1):
    #                 arr[10] += 1   
        
    # def formula_V(arr, V):
    #     for i in range (len(V)):
    #         for j in range (len(V[0])):
    #             if (V[i][j] >= 0 and V[i][j] < 0.2):
    #                 arr[11] += 1
    #             elif (V[i][j] >= 0.2 and V[i][j] < 0.7):
    #                 arr[12] += 1
    #             elif (V[i][j] >= 0.7 and V[i][j] <= 1):
    #                 arr[13] += 1    

    # array1 = [0 for i in range(60)]
    # a = np.concatenate(np.histogram(H1), np.histogram(S1), np.histogram(V1))
    # formula_S(array1, S1)
    # formula_V(array1, V1)

    # array2 = [0 for i in range(14)]
    # formula_H(array2, H2)
    # formula_S(array2, S2)
    # formula_V(array2, V2)

    # array3 = [0 for i in range(14)]
    # formula_H(array3, H3)
    # formula_S(array3, S3)
    # formula_V(array3, V3)

    # array4 = [0 for i in range(14)]
    # formula_H(array4, H4)
    # formula_S(array4, S4)
    # formula_V(array4, V4)

    # array5 = [0 for i in range(14)]
    # formula_H(array5, H5)
    # formula_S(array5, S5)
    # formula_V(array5, V5)

    # array6 = [0 for i in range(14)]
    # formula_H(array6, H6)
    # formula_S(array6, S6)
    # formula_V(array6, V6)

    # array7 = [0 for i in range(14)]
    # formula_H(array7, H7)
    # formula_S(array7, S7)
    # formula_V(array7, V7)

    # array8 = [0 for i in range(14)]
    # formula_H(array8, H8)
    # formula_S(array8, S8)
    # formula_V(array8, V8)

    # array9 = [0 for i in range(14)]
    # formula_H(array9, H9)
    # formula_S(array9, S9)
    # formula_V(array9, V9)

    # array = np.concatenate([array1, array2, array3, array4, array5, array6, array7, array8, array9])

    # return a
# 

# path1 = "C:/Users/HP/tubes-algeo2/dataset/9.jpg"
# a = color(path1)
# print(a)

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


            

    
