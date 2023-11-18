import cv2
import os
import time
import numpy as np
import functions as fn
from directory import get_upload_dir

def konversigray(image):
    greyscale = [[0 for i in range(len(image[0]))] for j in range (len(image))]
    for i in range (len(image)):
        for j in range (len(image[0])):
            R = image[i][j][2]
            G = image[i][j][1]
            B = image[i][j][0]
            greyscale[i][j] = round(0.29*R + 0.587*G + 0.114*B)
    greyscale = np.resize(greyscale,(256,256))
    return greyscale

# membuat framework matrix
def createcooccurence(greyscale):
    # print(greyscale)
    cooccurence = [[0 for i in range(256)] for j in range (256)]
    for i in range (256):
        for j in range(255):
            cooccurence[(greyscale[i][j])][(greyscale[i][j+1])]+=1
    # proses perhitungan cooccurence
    cooccurence = cooccurence + np.transpose(cooccurence)   #no error proof
    cooccurence = cooccurence/fn.totalValue(cooccurence)   #no error proof harusnya, untuk normalized matrix
    return cooccurence




def searchtexture(image):
    dataset_dir = get_upload_dir()
    start_time = time.time()

    # membaca image inputan untuk dibandingkan
    mimage = cv2.imdecode(image, 1)
    len_row = len(mimage)
    len_col = len(mimage[0])
    mgreyscale = konversigray(mimage)
    # print(mgreyscale)
    mcooccurence = createcooccurence(mgreyscale)
    mtoople = fn.vectorcosine(mcooccurence) 

    # create a final array to store the results
    final = []

    if not(os.path.exists(dataset_dir) and os.path.isdir(dataset_dir)):
        return {"success": False, "error": "Path doesn't exist"}

    # Check if the dataset directory exists
    image_files = os.listdir(dataset_dir)
    
    for filename in image_files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(dataset_dir, filename)
            image = cv2.imread(img_path)
            
            greyscale = konversigray(image)
            cooccurence = createcooccurence(greyscale)
            toople = fn.vectorcosine(cooccurence) 
            # print(toople)
            # final.append(fn.cosinesimilarity(mtoople,toople))
            similarity = fn.cosinesimilarity(mtoople,toople)
            if(similarity >= 0.6):
                final.append({"filename": filename, "similarity": similarity})
    
    return {"files": fn.sort_dictionary(final, "similarity", False), "time": time.time() - start_time}
