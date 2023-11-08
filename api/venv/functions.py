import math 

def transpose(Matriks,ukuran):
    Matrikstemp = [[0 for i in range (ukuran)] for j in range (ukuran)]
    for baris in range (ukuran):
        for kolom in range (ukuran):
            Matrikstemp[baris][kolom] = Matriks[kolom][baris]
    return Matrikstemp

def cosinesimilarity(vector1,vector2):
    result = 0
    for i in range (len(vector1)):
        result+=vector1[i]*vector2[i]
    return result/(vectorlen(vector1)*vectorlen(vector2))

def vectorlen(vectorarr):
    result = 0
    for i in range (len(vectorarr)):
        result+=vectorarr[i]*vectorarr[i]
    return math.sqrt(result)

def RGBtoGREYSCALE(R,G,B):
    res = (0.29*R + 0.587*G + 0.114*B)
    return res

def symmetricMat(GLCMMat,ukuran):
    elmttotal = 0
    res = GLCMMat
    trans = transpose(GLCMMat,ukuran)
    for j in range (ukuran):
        for i in range (ukuran):
            res[i][j] = GLCMMat[i][j] + trans[i][j]
            elmttotal += res[i][j]
    return res

def totalValue(symmetricMatrix):
    elmttotal = 0
    for j in range (256):
        for i in range (256):
            elmttotal += symmetricMatrix[i][j]
    return elmttotal

# def normalizedMat(symmetricMatrix):
#     res = symmetricMatrix
#     total = totalValue(symmetricMatrix)
#     for j in range (4):
#         for i in range (4):
#             res[i][j] = symmetricMatrix[i][j] / total
#     return res

# perhitungan contrast, homogeneity, dan entropy
def vectorcosine(cooccurence):
    homogeneity = 0
    entropy = 0
    contrast =0
    for i in range (len(cooccurence)):
        for j in range (len(cooccurence)-1):
            homogeneity += cooccurence[i][j]/(1+((i-j)*(i-j)))
            contrast += cooccurence[i][j] * (i-j)*(i-j)
            if((cooccurence[i][j])>0):
                # print(cooccurence[i][j])
                entropy += cooccurence[i][j] * math.log(cooccurence[i][j],10)
    new_vector = (homogeneity,-entropy,contrast)
    return new_vector