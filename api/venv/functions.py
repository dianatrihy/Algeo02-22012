def transpose(Matriks,ukuran):
    Matrikstemp = [[0 for i in range (ukuran)] for j in range (ukuran)]
    for baris in range (ukuran):
        for kolom in range (ukuran):
            Matrikstemp[baris][kolom] = Matriks[kolom][baris]
    return Matrikstemp

def RGBtoGREYSCALE(R,G,B):
    res = 0.29*R + 0.587*G + 0.114*B
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

def normalizedMat(symmetricMatrix):
    res = symmetricMatrix
    total = totalValue(symmetricMatrix)
    for j in range (256):
        for i in range (256):
            res[i][j] = symmetricMatrix[i][j] / total
    return res