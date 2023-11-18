import numpy as np
import cv2
import functions as fn
import time
import io
from PIL import Image
start_time = time.time()
path = "C:/Users/Asus/Pictures/Smiling cat.jpg"

# path = "C:/Users/Asus/Documents/Thea/SMT3/TubesAlgeo2/Algeo02-22012/perforated/perforated_0003.jpg"
image = cv2.imread(path)

len_row = len(image)
len_col = len(image[0])
print(len_row)
print(len_col)
greyscale = [[0 for i in range(len(image))] for j in range (len(image))]
for i in range (len(image)):
    for j in range (len(image)):
        R = image[i][j][2]
        G = image[i][j][1]
        B = image[i][j][0]
        image[i][j] = round(0.29*R + 0.587*G + 0.114*B)
image = np.resize(image,(256,256))
# image = Image.fromarray(image)
# greyscale = io.BytesIO()
# image.save(greyscale,format='JPEG',optimize=True,quality = 50)


# grey = [[0 for i in range(len(image))] for j in range (len(image))]
# for i in range (len(image)):
#     for j in range (len(image)):
#         R = image[i][j][2]
#         G = image[i][j][1]
#         B = image[i][j][0]
#         grey[i][j] = round(0.29*R + 0.587*G + 0.114*B)
# grey = np.resize(grey,(256,256))
# grey = Image.fromarray(grey)
# greyscale = io.BytesIO()
# grey.save(greyscale,format='JPEG',quality = 50)
# greyscale = np.array(Image.open(greyscale))

# cv2.imshow("test img", imgs[0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# greyscale udh proof benar

# print("\nMatriks cooccur\n")

# membuat framework matrix
cooccurence = [[0 for i in range(256)] for j in range (256)]
for i in range (256):
    for j in range(255):
        # print("test")
        cooccurence[(greyscale[i][j])-1][(greyscale[i][j+1])-1]+=1
# proses perhitungan cooccurence
cooccurence = cooccurence + np.transpose(cooccurence)   #no error proof
cooccurence = cooccurence/fn.totalValue(cooccurence)   #no error proof harusnya, untuk normalized matrix

tester = [[1,1,0,0],[0,0,1,0],[0,0,0,2],[0,0,1,0]]

# with np.printoptions(threshold=np.inf):
#     print(cooccurence)
#     # print(fn.totalValue(tester))
#     print("\n")
#     # print(np.transpose(tester))


print(fn.vectorcosine(cooccurence))


print("--- %s seconds ---" % (time.time() - start_time))