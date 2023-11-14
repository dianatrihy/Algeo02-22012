# from PIL import Image
import color
import numpy as np 
import cv2
import os
import time
import functions as fn
# import texture as tex
start_time = time.time()


# membaca image inputan untuk dibandingkan
path_image = "C:/Users/HP/tubes-algeo2/dataset/0.jpg"
path_dataset = "C:/Users/HP/tubes-algeo2/dataset"

def searchcolor(path_image, path_dataset):
    re = 200
    Ha = [[0 for i in range(re)] for j in range (re)]
    Sa = [[0 for i in range(re)] for j in range (re)]
    Va = [[0 for i in range(re)] for j in range (re)]
    color.RGBtoHSV(path_image, re, Ha, Sa, Va)

    # Check if the dataset directory exists
    if not(os.path.exists(path_dataset) and os.path.isdir(path_dataset)):
        return {"success": False, "error": "Path doesn't exist"}
    
    # create a final array to store the results
    final = []
    processedfiles = 0

    image_files = os.listdir(path_dataset)
    for filename in image_files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')) and (processedfiles < 20):
            img_path = os.path.join(path_dataset, filename)
            similarity = color.color(Ha, Sa, Va, img_path)
            if(similarity >= 0.6):
                final.append({"filename": filename, "similarity": similarity})
            processedfiles += 1
    
    return {"files": fn.sort_dictionary(final, "similarity", False), "time": time.time() - start_time}

print(searchcolor(path_image, path_dataset))



# # baca semua image di dataset
# dataset_dir = "C:/Users/HP/tubes-algeo2/dataset"
# processedfiles = 0
# final = []
# # Check if the dataset directory exists
# if not(os.path.exists(dataset_dir) and os.path.isdir(dataset_dir)):
#     return {"success": False, "error": "Path doesn't exist"}

    
# for filename in image_files:
#     if (filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')) and (processedfiles < 20)):
#         img_path = os.path.join(dataset_dir, filename)
#             # image = cv2.imread(img_path)
#         similarity = color.color(Ha, Sa, Va, img_path)
#             # final.append(fn.cosinesimilarity(mtoople,toople))
#         print(processedfiles, filename)
#         if(similarity >= 0.6):
#             final.append({"filename": filename, "similarity": similarity})
#         processedfiles += 1
#             # print(f"Processedfiles{processedfiles}" )
# {"files": fn.sort_dictionary(final, "similarity", False), "time": time.time() - start_time}
# # final.sort()
# print(final)

# # path1 = "C:/Users/HP/tubes-algeo2/dataset/9.jpg"
# # path2 = "C:/Users/HP/tubes-algeo2/dataset/10.jpg"
# # array1 = color.color(path1)
# # array2 = color.color(image)
# # result = fn.cosinesimilarity(array1,array2)

# # print(result)

# print("--- %s seconds ---" % (time.time() - start_time))