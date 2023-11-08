import numpy as np
import cv2
import functions as fn
import time
import io
from PIL import Image
start_time = time.time()
path = "C:/Users/Asus/Pictures/Smiling cat.jpg"
# path = "C:/Users/Asus/Documents/Thea/SMT3/TubesAlgeo2/Algeo02-22012/dataset/0.jpg"
image = cv2.imread(path)

len_row = len(image)
len_col = len(image[0])

def konversigray(image):
    greyscale = [[0 for i in range(len(image))] for j in range (len(image))]
    for i in range (len(image)):
        for j in range (len(image)):
            R = image[i][j][2]
            G = image[i][j][1]
            B = image[i][j][0]
            greyscale[i][j] = round(0.29*R + 0.587*G + 0.114*B)
    greyscale = np.resize(greyscale,(256,256))
    return greyscale

# membuat framework matrix
def createcooccurence(greyscale):
    cooccurence = [[0 for i in range(256)] for j in range (256)]
    for i in range (256):
        for j in range(255):
            cooccurence[(greyscale[i][j])-1][(greyscale[i][j+1])-1]+=1
    # proses perhitungan cooccurence
    cooccurence = cooccurence + np.transpose(cooccurence)   #no error proof
    cooccurence = cooccurence/fn.totalValue(cooccurence)   #no error proof harusnya, untuk normalized matrix
    return cooccurence

tester = [[1,1,0,0],[0,0,1,0],[0,0,0,2],[0,0,1,0]]

# with np.printoptions(threshold=np.inf):
#     print(cooccurence)
#     # print(fn.totalValue(tester))
#     print("\n")
#     # print(np.transpose(tester))


# print(fn.vectorcosine(cooccurence))


print("--- %s seconds ---" % (time.time() - start_time))