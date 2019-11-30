import sys,os
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2 
import numpy as np
import argparse
import random as rand

globals_h=0
globals_w=0
color_dict=dict()
def rotate_img(roi,roi_mask):
    
    degree=rand.randint(0,360)

    (h, w) = roi.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), degree, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    # perform the actual rotation and return the image
    return cv2.warpAffine(roi, M, (nW, nH)),cv2.warpAffine(roi_mask, M, (nW, nH))    

def read_color_from_file():
    global color_dict
    f=open("color.txt")
    color_dict=dict()
    for line in f:
        line_list=line.split(' ')

        color_index=line_list[0]
        color_information_temp=line_list[1]
            
        color_information=color_information_temp[0:-2]
        
        color_information_temp=color_information.split(',')

        color_information_tuple=(int(color_information_temp[0]),int(color_information_temp[1]),int(color_information_temp[2]))

        color_dict[color_index]=color_information_tuple


def set_color(item,color):
    if item not in color_dict:
        color_dict[item]=color

def read_color(item):
    global color_dict
    return color_dict[item]

def find_mask(label_dir,img_dir):
    global globals_h,globals_w
    img = cv2.imread(label_dir,cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ori=cv2.imread(img_dir,cv2.IMREAD_COLOR)
    globals_h,globals_w,_=ori.shape
    ret,thresh = cv2.threshold(gray,20,255,0)

    # cv2.namedWindow("kk",0)
    # cv2.resizeWindow("kk", 640, 480)

    # cv2.imshow("kk",thresh)
    # cv2.waitKey(0)
    contours,_=cv2.findContours(thresh,1,2)
    cnt=contours[0]

    x,y,w,h=cv2.boundingRect(cnt)
    #print("x :"+str(x)+"\n"+"y :"+str(y)+"\n"+"w :"+str(w)+"\n"+"h :"+str(h))
    #img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),15)
    #ori_test=cv2.rectangle(ori,(x,y),(x+w,y+h),(0,255,0),15)

    roi=ori[y:y+h, x:x+w]
    roi_mask=img[y:y+h, x:x+w]

    # cv2.imshow("kk",img)
    # cv2.waitKey(0)

    # cv2.imshow("kk",ori_test)
    # cv2.waitKey(0)

    # cv2.imshow("kk",roi)
    # cv2.waitKey(0)
    # cv2.imshow("kk",roi_mask)
    # cv2.waitKey(0)

    # cv2.imwrite("roi.jpg",roi)
    # cv2.imwrite("roi_mask.jpg",roi_mask)
    #print("label have been detected")
    
    roi,roi_mask=rotate_img(roi,roi_mask)
    

    return roi,roi_mask

def overlay(roi,roi_mask,img_dir,ground_truth_dir,item):

    global globals_h,globals_w
    # roi=cv2.imread("roi.jpg")
    # roi_mask=cv2.imread("roi_mask.jpg")

    w,h,_=roi.shape
    for i in range(w):
        for j in range(h):
                if not(roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20):
                    roi[i][j][0]=0
                    roi[i][j][1]=0
                    roi[i][j][2]=0

    # cv2.imshow("kk",roi_mask)
    # cv2.waitKey(0)

    # cv2.namedWindow("kk",0)
    # cv2.resizeWindow("kk", (640, 480))
    # cv2.imshow("kk",roi)
    # cv2.waitKey(0)

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
        h1=w//2+1
    else:
        h1=w//2
        
    process_key_x=place_x-w1
    process_key_y=place_y-h1

    #print("process_key_x"+str(process_key_x)+"\n"+"process_key_y"+str(process_key_y))

    '''import datetime
    x = datetime.datetime.now()
    i_want=str(x.month)+"_"+str(x.day)+"_"+str(x.hour)+"_"+str(x.minute)+"_"+str(x.second)'''
    for i in range(w):
        for j in range(h):
                if (roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20):
                    src[process_key_x+i][process_key_y+j][0]=roi[i][j][0]
                    src[process_key_x+i][process_key_y+j][1]=roi[i][j][1]
                    src[process_key_x+i][process_key_y+j][2]=roi[i][j][2]

    '''cv2.imwrite("src/src_"+i_want+".jpg",src)'''

    # src=cv2.resize(src,(800,640))
    # cv2.imshow("kk",src)
    # cv2.waitKey(0)
    if(ground_truth_dir=="0"):
        ground_truth = np.zeros((w_add,h_add,3), np.uint8)
        b,g,r=read_color(item)
        for i in range(w):
            for j in range(h):
                    if (roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20):
                        ground_truth[process_key_x+i][process_key_y+j][2]=r
                        ground_truth[process_key_x+i][process_key_y+j][1]=g
                        ground_truth[process_key_x+i][process_key_y+j][0]=b

    else :
        ground_truth=cv2.imread(ground_truth_dir)
        b,g,r=read_color(item)
        
        for i in range(w):
            for j in range(h):
                    if (roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20):
                        ground_truth[process_key_x+i][process_key_y+j][2]=r
                        ground_truth[process_key_x+i][process_key_y+j][1]=g
                        ground_truth[process_key_x+i][process_key_y+j][0]=b

    '''cv2.imwrite("ground_truth/ground_truth_"+i_want+".jpg",ground_truth)'''
    # ground_truth=cv2.resize(ground_truth,(800,640))

    # cv2.imshow("kk",ground_truth)
    # cv2.waitKey(0)
    #print("generate done\n")
    return src,ground_truth

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', type=int, default='5', help='Number of times generate')
    parser.add_argument('--num_each', type=str, default='0', help='Number of object in each frame')
    FLAGS = parser.parse_args()

    numbertimes=FLAGS.num
    num_each_frame=FLAGS.num_each
    num_each_frame=num_each_frame.split(',')
    
    data_dir=os.listdir("data/")   
    path_ground="background/"
    directory_background = os.fsencode(path_ground)
    filename_ground = os.listdir(directory_background)
    
    read_color_from_file()
    
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
                    # for lkk in range(int(num_frame)):
                    #     num_fold=rand.randint(0,len(data_dir)-1)
                    #     data_dir_want.append(data_dir[num_fold])
                    resultList=rand.sample(range(0,len(data_dir)),int(num_frame))
                    #print(resultList)
                    for lkk in resultList:
                        data_dir_want.append(data_dir[lkk])

                #print(data_dir_want)
                for i in (data_dir_want):
                    # b,g,r=rand.randint(0,255),rand.randint(0,255),rand.randint(0,255)
                    # set_color(i,(b,g,r))

                    path_img="data/"+i+"/img/"
                    path_label="data/"+i+"/label/"

                    directory_img = os.fsencode(path_img)
                    filename_img = os.listdir(directory_img)
                    index=rand.randint(0,len(filename_img)-1)
                    file_img=filename_img[index].decode("utf-8")
                    path_img=path_img + file_img
                    number=file_img[0:1]

                    path_label=path_label+number+".png"    


                    roi,roi_mask=find_mask(path_label,path_img)

                    if(times==0):
                        src,ground_truth = overlay(roi,roi_mask,path_ground,"0",i)
                    else:
                        src,ground_truth = overlay(roi,roi_mask,"temp/temp_img.jpg","temp/temp_label.jpg",i)
                    
                    if(times==len(data_dir_want)-1):
                        import datetime
                        x = datetime.datetime.now()
                        i_want=str(x.month)+"_"+str(x.day)+"_"+str(x.hour)+"_"+str(x.minute)+"_"+str(x.second)

                        cv2.imwrite("output/label/ground_truth_"+i_want+".jpg",ground_truth)
                        cv2.imwrite("output/src/src_"+i_want+".jpg",src)
                        print("generate done")
                    else:
                        cv2.imwrite("temp/temp_label.jpg",ground_truth)
                        cv2.imwrite("temp/temp_img.jpg",src)
                    times=times+1


    print("finish")



if __name__ == "__main__":
    main()
