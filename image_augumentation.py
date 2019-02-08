# Import the os module, for the os.walk function
import os
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib.colors import LogNorm
import numpy as np
from PIL import Image
from PIL import ImageFilter

# Set the directory you want to start from
source_images= 'D:\my-exp\AI\object_detection\source_images'
augumented_images_dir = 'D:\my-exp\AI\object_detection\\augumented_images\\'
count = 0
# map having label and frequency of object to plot the histogram of objects and their frequency
class_dectionary = {}
# map having object's directoty path as key and thier label as value
data_dectionary = {}

# list of class to plot the graph
class_list = []
# list of object frequencies for all labels
frequenct_list = []

for dirName, subdirList, fileList in os.walk(source_images):
    if len(fileList) > 0:
        for single_file in fileList:
                original_image_path = dirName + '\\' +single_file
                augumented_images_dir = augumented_images_dir + single_file[:single_file.rfind('.')]+'_#####' + single_file[single_file.rfind('.'):]
                print(original_image_path)
                print(augumented_images_dir)
                
                original_image = Image.open(original_image_path)
                
                image_list=[]
                rotate_image_45=original_image.rotate(45)
                rotate_image_90=original_image.rotate(90)
                rotate_image_135=original_image.rotate(135)
                rotate_image_180=original_image.rotate(180)
                rotate_image_225=original_image.rotate(225)
                rotate_image_270=original_image.rotate(270)
                rotate_image_315=original_image.rotate(315)
                transpose_image_flip_left_right = original_image.transpose(Image.FLIP_LEFT_RIGHT)
                transpose_image_flip_top_bottom = original_image.transpose(Image.FLIP_TOP_BOTTOM)
                transpose_image_transpose = original_image.transpose(Image.TRANSPOSE)
                filter_imagefilter_blur = original_image.filter(ImageFilter.BLUR)
                filter_imagefilter_sharpen = original_image.filter(ImageFilter.SHARPEN)
                filter_imagefilter_smooth = original_image.filter(ImageFilter.SMOOTH)
                
                image_list.append(original_image)
                image_list.append(rotate_image_45)
                image_list.append(rotate_image_90)
                image_list.append(rotate_image_135)
                image_list.append(rotate_image_180)
                image_list.append(rotate_image_225)
                image_list.append(rotate_image_270)
                image_list.append(rotate_image_315)
                image_list.append(transpose_image_flip_left_right)
                image_list.append(transpose_image_flip_top_bottom)
                image_list.append(transpose_image_transpose)
                image_list.append(filter_imagefilter_blur)
                image_list.append(filter_imagefilter_sharpen)
                image_list.append(filter_imagefilter_smooth)


                original_image.save(augumented_images_dir.replace('#####','original_image'))
                rotate_image_45.save(augumented_images_dir.replace('#####','rotate_image_45'))
                rotate_image_90.save(augumented_images_dir.replace('#####','rotate_image_90'))
                rotate_image_135.save(augumented_images_dir.replace('#####','rotate_image_135'))
                rotate_image_180.save(augumented_images_dir.replace('#####','rotate_image_180'))
                rotate_image_225.save(augumented_images_dir.replace('#####','rotate_image_225'))
                rotate_image_270.save(augumented_images_dir.replace('#####','rotate_image_270'))
                rotate_image_315.save(augumented_images_dir.replace('#####','rotate_image_315'))
                transpose_image_flip_left_right.save(augumented_images_dir.replace('#####','transpose_image_flip_left_right'))
                transpose_image_flip_top_bottom.save(augumented_images_dir.replace('#####','transpose_image_flip_top_bottom'))
                transpose_image_transpose.save(augumented_images_dir.replace('#####','transpose_image_transpose'))
                filter_imagefilter_blur.save(augumented_images_dir.replace('#####','filter_imagefilter_blur'))
                filter_imagefilter_sharpen.save(augumented_images_dir.replace('#####','filter_imagefilter_sharpen'))
                filter_imagefilter_smooth.save(augumented_images_dir.replace('#####','filter_imagefilter_smooth'))

                

for dirName, subdirList, fileList in os.walk(source_images):
    if len(fileList) > 0:
        for single_file in fileList:
            data_dectionary[dirName + '\\' +
                            single_file] = dirName[dirName.rfind('\\')+1:]
        class_dectionary[dirName[dirName.rfind('\\')+1:]] = len(fileList)

for x in class_dectionary.items():
    key = x[0]
    val = x[1]
    class_list.append(key)
    frequenct_list.append(val)
    print("class ", key, ' is having', val, ' items')

for x in data_dectionary.items():
    print("file ", x[0], ' is having', x[1], ' lebel')

""" style.use('ggplot')
plt.bar(class_list, frequenct_list, align='center')
plt.title('Epic Info')
plt.ylabel('Frequency')
plt.xlabel('Class')
plt.show() """
######################################################################################

w=10
h=10
fig=plt.figure(figsize=(8, 8))
columns = 5
rows = 3
for i in range(1, len(image_list) +1):
    ax = fig.add_subplot(rows, columns, i)
    ax.set_title("hiii")
    plt.imshow(image_list[i-1])
plt.show()
