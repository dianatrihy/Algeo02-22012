# from PIL import Image
import color
import os
import time
import functions as fn
from directory import get_upload_dir

def searchcolor(path_image):
    path_dataset = get_upload_dir()
    start_time = time.time()
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
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(path_dataset, filename)
            similarity = color.color(Ha, Sa, Va, img_path)
            if(similarity >= 0.6):
                final.append({"filename": filename, "similarity": similarity})
    
    return {"files": fn.sort_dictionary(final, "similarity", False), "time": time.time() - start_time}