from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

import zipfile


face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
# the rest is up to you!
print("This is for Mark")
images_dir = {}
name_lst = [] 

def unzip_images(zip_name):  
    zf = zipfile.ZipFile(zip_name)
    for each in zf.infolist():
        images_dir[each.filename] = [Image.open(zf.open(each.filename))]
        name_lst.append(each.filename)
           

unzip_images('readonly/small_img.zip')
    
for name in name_list:
    img = images_dir[name][0]
        
    images_dir[name].append(pytesseract.image_to_string(img).replace('-\n',''))
        
    if 'Mark' in images_dir[name][1]: 
        print('Results found in file',name)
            
        try:
            faces = (face_cascade.detectMultiScale(np.array(img),1.35,4)).tolist()
            images_dir[name].append(faces)
            faces_in_each = []
            for x,y,w,h in images_dir[name][2]:
                faces_in_each.append(img.crop((x,y,x+w,y+h)))
                
            board = Image.new(img.mode, (640,128*int(np.ceil(len(faces_in_each)/5))))
            x = 0
            y = 0

            for face in faces_in_each:
                face.thumbnail((128,128))
                board.paste(face, (x, y))
                if x+128 == board.width:
                    x=0
                    y=y+128
                else:
                    x=x+128
                        
            display(board)
        except:
            print('But there were no faces in that file!')
