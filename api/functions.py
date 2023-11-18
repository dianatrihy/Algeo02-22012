import math
import numpy as np 

# Transpose matriks tapi ga kepake
def transpose(Matriks,ukuran):
    Matrikstemp = np.zeros(ukuran)
    for baris in range (ukuran):
        for kolom in range (ukuran):
            Matrikstemp[baris][kolom] = Matriks[kolom][baris]
    return Matrikstemp

# cosine similarity function
# Parameter: vector1 dan vector2
def cosinesimilarity(vector1,vector2):
    result = 0
    for i in range (len(vector1)):
        result+=vector1[i]*vector2[i]
    return result/(np.linalg.norm(vector1)*np.linalg.norm(vector2))

# Return panjang sebuah vektor
def vectorlen(vectorarr):
    result = 0
    for i in range (len(vectorarr)):
        result+=vectorarr[i]*vectorarr[i]
    return math.sqrt(result)

# Konversi RGB ke greyscale
# Ga kepake though
def RGBtoGREYSCALE(R,G,B):
    res = (0.29*R + 0.587*G + 0.114*B)
    return res

# Menghitung symmetric matrix
# Gakepake juga
def symmetricMat(GLCMMat,ukuran):
    elmttotal = 0
    res = GLCMMat
    trans = transpose(GLCMMat,ukuran)
    for j in range (ukuran):
        for i in range (ukuran):
            res[i][j] = GLCMMat[i][j] + trans[i][j]
            elmttotal += res[i][j]
    return res

# Mengembalikan nilai total semua elemen pada sebuah matriks
def totalValue(symmetricMatrix):
    elmttotal = 0
    for j in range (256):
        for i in range (256):
            elmttotal += symmetricMatrix[i][j]
    return elmttotal

# Perhitungan contrast, homogeneity, dan entropy
# Mengembalikan tuple nilai ketiganya 
def vectorcosine(cooccurence):
    homogeneity = 0
    entropy = 0
    contrast =0
    for i in range (len(cooccurence)):
        for j in range (len(cooccurence)):
            homogeneity += cooccurence[i][j]/(1+((i-j)*(i-j)))
            contrast += cooccurence[i][j] * (i-j)*(i-j)
            if((cooccurence[i][j])>0):
                # print(cooccurence[i][j])
                entropy += cooccurence[i][j] * math.log(cooccurence[i][j],10)
    new_vector = (homogeneity,(-1)*entropy,contrast)
    return new_vector

def sort_dictionary(dictionary_arr, key, ascending):
    def sort_key(dictionary):
        return dictionary[key]

    return sorted(dictionary_arr, key=sort_key, reverse=not(ascending))