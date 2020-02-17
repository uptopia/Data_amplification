import sys,os
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2 
import numpy as np
import argparse
import random as rand
from PIL import Image 

globals_h=0
globals_w=0
color_dict=dict()
global_times=0
global_scale=1.0
def rotate_img(roi,roi_mask,roi_mask_realywant):
    
    degree=rand.randint(0,360)
    (h, w) = roi.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), degree, global_scale)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    # perform the actual rotation and return the image
    roi =cv2.warpAffine(roi, M, (nW, nH))
    roi_mask=cv2.warpAffine(roi_mask, M, (nW, nH))  
    roi_mask_realywant=cv2.warpAffine(roi_mask_realywant, M, (nW, nH))
    return roi,roi_mask,roi_mask_realywant

def find_mask(label_dir,img_dir,realywant_dir):
    global globals_h,globals_w
    img = cv2.imread(label_dir,cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ori=cv2.imread(img_dir,cv2.IMREAD_COLOR)
    realywant=cv2.imread(realywant_dir,cv2.IMREAD_COLOR)

    globals_h,globals_w,_=ori.shape

    ret,thresh = cv2.threshold(gray,20,255,0)
    contours,_=cv2.findContours(thresh,1,2)
    cnt=contours[0]
    x,y,w,h=cv2.boundingRect(cnt)
    
    roi=ori[y:y+h, x:x+w]
    roi_mask=img[y:y+h, x:x+w]
    roi_mask_realywant=realywant[y:y+h, x:x+w]
    
    
    roi,roi_mask,roi_mask_realywant=rotate_img(roi,roi_mask,roi_mask_realywant)

    # cv2.imshow("a",roi)
    # cv2.imshow("b",roi_mask)
    # cv2.imshow("c",roi_mask_realywant)
    # cv2.waitKey(0)
    return roi,roi_mask,roi_mask_realywant

def overlay(roi,roi_mask,img_dir,ground_truth_dir,item,check,visualize_Mat):

    global globals_h,globals_w,global_times
    

    w,h,_=roi.shape
    for i in range(w):
        for j in range(h):
                if not(roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20):
                    roi[i][j][0]=0
                    roi[i][j][1]=0
                    roi[i][j][2]=0


    src=cv2.imread(img_dir)
    src_h,src_w,_=src.shape
    if globals_h>src_h or globals_w>src_w :
        src=cv2.resize(src,(globals_w,globals_h))
    
    w_add,h_add,_=src.shape

    delete_length=max(w,h)

    place_x=rand.randint(min(delete_length,(w_add-delete_length)),max(delete_length,(w_add-delete_length)))
    place_y=rand.randint(min(delete_length,(h_add-delete_length)),max(delete_length,(h_add-delete_length)))

    if(w%2!=0):
        w1=w//2+1
    else:
        w1=w//2
        

    if(h%2!=0):
        h1=h//2+1
    else:
        h1=h//2
        
    process_key_x=place_x-w1
    process_key_y=place_y-h1

    if(ground_truth_dir=="0"):
        for i in range(w):
            for j in range(h):
                    if (roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20):
                        src[process_key_x+i][process_key_y+j][0]=roi[i][j][0]
                        src[process_key_x+i][process_key_y+j][1]=roi[i][j][1]
                        src[process_key_x+i][process_key_y+j][2]=roi[i][j][2]
    else:
        for i in range(w):
            for j in range(h):
                    if (roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20):
                        src[process_key_x+i][process_key_y+j][0]=roi[i][j][0]
                        src[process_key_x+i][process_key_y+j][1]=roi[i][j][1]
                        src[process_key_x+i][process_key_y+j][2]=roi[i][j][2]

                        visualize_Mat[process_key_x+i][process_key_y+j][0]=roi[i][j][0]
                        visualize_Mat[process_key_x+i][process_key_y+j][1]=roi[i][j][1]
                        visualize_Mat[process_key_x+i][process_key_y+j][2]=roi[i][j][2]

        
    global_times=global_times+1

    if(ground_truth_dir=="0"):
        ground_truth = np.zeros((w_add,h_add), np.uint8)
        visualize_Mat=src.copy()
        #b,g,r=read_color(item)

        for i in range(w):
            for j in range(h):
                    if (roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20 and check[i][j][2]>20):
                        ground_truth[process_key_x+i][process_key_y+j]=global_times
                        visualize_Mat[process_key_x+i][process_key_y+j][0]=200
        

    else :
        ground_truth=cv2.imread(ground_truth_dir)
        #b,g,r=read_color(item)

        for i in range(w):
            for j in range(h):
                    if (roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20 and check[i][j][2]>20):
                        ground_truth[process_key_x+i][process_key_y+j]=global_times
                        visualize_Mat[process_key_x+i][process_key_y+j][0]=200
    
    
    return src,ground_truth,visualize_Mat

def main():
    global global_times,global_scale
    i_want_index=0
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', type=int, default='5', help='Number of times generate')
    parser.add_argument('--num_each', type=str, default='0', help='Number of object in each frame')
    parser.add_argument('--scale', type=float, default='1.0', help='persentage of size change')
    FLAGS = parser.parse_args()

    numbertimes=FLAGS.num
    num_each_frame=FLAGS.num_each
    num_each_frame=num_each_frame.split(',')
    
    global_scale=FLAGS.scale

    data_dir=os.listdir("data/")   
    path_ground="background/"
    directory_background = os.fsencode(path_ground)
    filename_ground = os.listdir(directory_background)
    
    for num_frame in num_each_frame:
        for each_filename_ground in filename_ground:
            path_ground="background/"
            file_ground=each_filename_ground.decode("utf-8")
            
            path_ground=path_ground + file_ground
            
            for ll in range(numbertimes):
                times=0
                data_dir_want=list()
                if num_frame==str(0):
                    
                    data_dir_want=data_dir
                elif int(num_frame) == len(data_dir):
                    data_dir_want=data_dir
                else:
                    resultList=list()
                    resultList=rand.sample(range(0,len(data_dir)),int(num_frame))
                    for lkk in resultList:
                        data_dir_want.append(data_dir[lkk])
                
                for i in (data_dir_want):
                    
                    path_img="data/"+i+"/img/"
                    path_label="data/"+i+"/label/"
                    path_label_realywant="data/"+i+"/label_realywant/"

                    directory_img = os.fsencode(path_img)
                    filename_img = os.listdir(directory_img)
                    index=rand.randint(0,len(filename_img)-1)
                    file_img=filename_img[index].decode("utf-8")

                    path_img=path_img + file_img

                    temp_number=file_img.split('.')
                    number=temp_number[0]
                    path_label=path_label+number+".png"
                    path_label_realywant=path_label_realywant+number+".png"    
                    
                    roi,roi_mask,roi_mask_realywant=find_mask(path_label,path_img,path_label_realywant)

                    if(times==0):
                        src,ground_truth,visualize_Mat = overlay(roi,roi_mask,path_ground,"0",i,roi_mask_realywant,roi)
                    else:
                        src,ground_truth,visualize_Mat = overlay(roi,roi_mask,"temp/temp_img.png","temp/temp_label.png",i,roi_mask_realywant,visualize_Mat)
                    
                    if(times==len(data_dir_want)-1):
                        # import datetime
                        # x = datetime.datetime.now()
                        # i_want=str(x.month)+"_"+str(x.day)+"_"+str(x.hour)+"_"+str(x.minute)+"_"+str(x.second)
                        
                        ### opencv save photo
                        # ground_truth = cv2.cvtColor(ground_truth, cv2.COLOR_BGR2GRAY)
                        # cv2.imwrite("output/label/obj_"+str(i_want_index)+".png",ground_truth)
                        # cv2.imwrite("output/src/obj_"+str(i_want_index)+".png",src)
                        
                        ### PIL save photo
                        PIL_ground_truth = Image.fromarray(cv2.cvtColor(ground_truth,cv2.COLOR_BGR2RGB))
                        PIL_src = Image.fromarray(cv2.cvtColor(src,cv2.COLOR_BGR2RGB))
                        if PIL_ground_truth.mode!='P':
                            PIL_ground_truth=PIL_ground_truth.convert('L')
                        PIL_ground_truth.save("output/label/obj_"+str(i_want_index)+".png")

                        PIL_src.save("output/src/obj_"+str(i_want_index)+".png")

                        cv2.imwrite("output/visualize/obj_"+str(i_want_index)+".png",visualize_Mat)

                        f = open("output/yaml/obj_"+str(i_want_index)+".yaml", "w")
                        f.write("label_names:\n")
                        f.write("- _background_\n")
                        for item_to_yaml in data_dir_want:
                            if item_to_yaml==data_dir_want[len(data_dir_want)-1]:
                                f.write("- "+item_to_yaml)
                            else :    
                                f.write("- "+item_to_yaml+"\n")

                        i_want_index+=1
                        print("generate done")
                        global_times=0
                    else:
                        cv2.imwrite("temp/temp_label.png",ground_truth)
                        cv2.imwrite("temp/temp_img.png",src)
                    times=times+1


    print("finish")



if __name__ == "__main__":
    main()
