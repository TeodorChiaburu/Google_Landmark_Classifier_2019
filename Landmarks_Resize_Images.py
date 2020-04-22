""" Script to rescale images in a folder """

from PIL import Image
import os

# directories of the images to be rescaled
path = "./test/images/"
dirs = os.listdir( path )

# create new directorie for the folders of rescaled images
new_folder = "./test/images_resized/"
#for d in dirs:
#    new_path = os.path.join(new_folder, d)
#    try:
#        os.mkdir(new_path)
#    except OSError:
#        print ("Creation of the directory %s failed" % new_path)
#    else:
#        print ("Successfully created the directory %s " % new_path)

def resize(h, w):
    
    for item in dirs:
        
        # create new subfolder for each set of rescaled images
        new_path = os.path.join(new_folder, item)
        
        # current path of the image to be rescaled
        full_path = os.path.join(path, item)
        
        files = os.listdir(full_path)
        
        for file in files:
            
            file_path = full_path + '/' + file
            im = Image.open(file_path)
            imResize = im.resize((h, w), Image.ANTIALIAS)

            # input path to the new directory
            imResize.save(new_path + '/' + file, 'JPEG', quality = 90)
            print(file + ' resized and saved')
            
        
resize(300, 300)

