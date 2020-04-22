#import tensorflow as tf
#from tensorflow.keras.preprocessing.image import ImageDataGenerator 
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Conv2D, MaxPooling2D
#from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
#from tensorflow.keras import backend as k
#from tensorflow.keras.preprocessing import image
#from tensorflow.keras.optimizers import SGD

#from sklearn.preprocessing import StandardScaler
#from sklearn.model_selection import train_test_split
#
#import cv2
#import matplotlib.pyplot as plt
#
#import time
import numpy as np 
import pandas as pd 
import urllib.request
import os


train = pd.read_csv('train/train.csv')
print(len(train))
#trainAttribution = pd.read_csv('train/train_attribution.csv')
#print(len(trainAttribution))
trainLabelToCategory = pd.read_csv('train/train_label_to_category.csv')
print(len(trainLabelToCategory))

# landmark ids:
# 47378  - Eiffel Tower
# 150591 - Atomium
# 174715 - Machu Picchu
# 192921 - Grand Canyon
# 77124  - Great Wall of China
# 94287  - Great Barrier Reef
# 55350  - Sydney Opera
# 156969 - Sphinx of Giza
# 64325  - Great Pyramid of Giza
# 23370  - Sphinx of Memphis
# 138617 - Burj al Arab
# 163459 - Burj Khalifa
# 65146  - Brandenburg Gate Potsdam
# 170670 - Brandenburg Gate Berlin
# 160782 - Water of Girvan
# 10775  - Delta do Parnaiba
# 1924   - Niagara Falls
# 128008 - Castle of Palma
# 2220   - Westminster Abbey
# 40981  - Basilica of the Sacred Heart Brussels
x_ = [40981]

# helpful for later join with the categories
#x_unique = train['landmark_id'].unique()
#x_ = []
#count_classes = 0
#print(len(x_unique))
#nr_landmarks = 12 # number of landmarks we wish to train on
#min_train_img = 1000 # minimum number of train pics available for one landmark
#
#for i in range ( len( x_unique ) ):
#    
#    # for 12 classes with enough pics first
#    if( count_classes < nr_landmarks ):
#        
#        if( len( train[ train['landmark_id'] == x_unique[i] ]  ) > min_train_img ):
#            print('i = ', i)
#
#            count_classes += 1
#            x_.append( train['landmark_id'][i] )
#            
#            print('count_classes ', count_classes)                    
#    else:
#        break
#    
#print("------------------------------------------")    
#print(x_)


# create 12 folders with landmarkID x_ as name and insert 20 pictures
# x_= [138982, 192931, 38921, 149068, 63840, 28327, 113056, 66803, 160782, 49565, 157643, 129727] 
# containts more than 1000 pictures

# classes
category = []
nb_img = 0 # counter for total number of images over all classes
np_train = np.array(train)
pics_per_class = 100

for i in range ( len ( x_ ) ):
      
    try:        
        # cut the cat name
        print('start download img for class ', i+1) 
        y = trainLabelToCategory[trainLabelToCategory['landmark_id'] == x_[i]]['category'].str.split(':').str[2].values[0]
        category.append(y)
        
        path = 'C:\\Users\\teo_c\\OneDrive\\Documents\\Beuth\\Master\\3. Semester\\Images\\Landmarks\\train\\images\\' + y
        os.mkdir(path)   
        print("directory created")
        
        nr_img = 0 # counter for pics to store per class
        for j in range ( len ( np_train ) ):
            
            if (np_train[j, 2] == x_[i]): # compare landmark_id
                
                # test with 100 pics for each class first
                if( nr_img < pics_per_class ):

                    nr_img = nr_img + 1
                    nb_img = nb_img + 1

                    # comprare landmarkID
                    try:
                        urllib.request.urlretrieve(np_train[j, 1], path + "\\" + str(np_train[j, 0]) + '.jpg')
                        print('download... ' + str(nb_img))    
                    except:
                        print('download failed')
                else:
                    break
       
                
        print(x_[i],  y)
        print(20 * '*')                    
    

    except OSError:
        print ("Creation of the directory %s failed" % path)
        

    
print(category)        
print('img download completed') 


