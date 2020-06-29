import sys,os
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2 
import numpy as np
import argparse
import random as rand
from PIL import Image 

globals_h=0
globals_w=0
item_dict=dict()
global_scale=1.0
global_times=0
global_background_multi=1.0
def consider_scale(mat_multi):
    global global_background_multi
    persentage=mat_multi/global_background_multi
    #print("--------------",persentage)
    if persentage > 0.1 :
        return 0.2
    elif persentage > 0.035 :
        return 0.55
    elif persentage<0.01:
        return 1.7
    else :
        return 0.7

def rotate_img(roi,roi_mask):
    global global_scale
    degree=rand.randint(0,360)

    (h, w) = roi.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), degree, consider_scale(h*w))
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
    return roi,roi_mask

def read_item_from_file():
    global item_dict
    f=open("item.txt")
    i=0
    for line in f:
        if '\n' in line :
            line = line[0:len(line)-1]
        item_dict[line]=i
        i=i+1
    print(item_dict)
# illllla=0
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

    # cv2.imshow("1",roi)
    # cv2.imshow("2",roi_mask)
    # cv2.waitKey(0)

    # cv2.imwrite("roi.jpg",roi)
    # cv2.imwrite("roi_mask.jpg",roi_mask)
    #print("label have been detected")


    roi,roi_mask=rotate_img(roi,roi_mask)

    gray = cv2.cvtColor(roi_mask, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,20,255,0)
    contours,_=cv2.findContours(thresh,1,2)
    cnt=contours[0]
    x,y,w,h=cv2.boundingRect(cnt)

    roi=roi[y:y+h, x:x+w]
    roi_mask=roi_mask[y:y+h, x:x+w]

    # cv2.imwrite("./output/test/"+str(illllla)+".jpg",roi_mask)
    # illllla+=1
    
    # cv2.imshow("a",roi)
    # cv2.imshow("b",roi_mask)
    # cv2.waitKey(0)
    return roi,roi_mask

def overlay(roi,roi_mask,img_dir,ground_truth_dir,item,centerxy_w_h):

    global globals_h,globals_w,global_times
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
    # if globals_h>src_h or globals_w>src_w :
    #     src=cv2.resize(src,(globals_w,globals_h))
    
    w_add,h_add,_=src.shape

    delete_length=max(w,h)

    # place_x=rand.randint(int(delete_length//2),w_add-int(delete_length//2))
    # place_y=rand.randint(int(delete_length//2),h_add-int(delete_length//2))

    place_x=rand.uniform(int(delete_length//2),w_add-int(delete_length//2))
    place_y=rand.uniform(int(delete_length//2),h_add-int(delete_length//2))

    if(w%2!=0):
        w1=w//2+1
    else:
        w1=w//2
        

    if(h%2!=0):
        h1=h//2+1
    else:
        h1=h//2
        
    process_key_x=int(place_x)-w1
    process_key_y=int(place_y)-h1

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
    global_times=global_times+1
    if(ground_truth_dir=="0"):
        ground_truth = np.zeros((w_add,h_add), np.uint8)
        #b,g,r=read_color(item)
        for i in range(w):
            for j in range(h):
                    if (roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20):
                        ground_truth[process_key_x+i][process_key_y+j]=global_times
        

    else :
        # print("global_times : ",global_times)
        ground_truth=cv2.imread(ground_truth_dir)
        #b,g,r=read_color(item)
        
        for i in range(w):
            for j in range(h):
                    if (roi_mask[i][j][2]!=0 and roi_mask[i][j][2]>20):
                        ground_truth[process_key_x+i][process_key_y+j]=global_times
    temp_centerxy_w_h=[]
    temp_centerxy_w_h.append(place_x)
    temp_centerxy_w_h.append(place_y)
    temp_centerxy_w_h.append(w)
    temp_centerxy_w_h.append(h)
    centerxy_w_h.append(temp_centerxy_w_h)
    
    '''cv2.imwrite("ground_truth/ground_truth_"+i_want+".jpg",ground_truth)'''
    # ground_truth=cv2.resize(ground_truth,(800,640))

    # cv2.imshow("kk",ground_truth)
    # cv2.waitKey(0)
    #print("generate done\n")
    return src,ground_truth,centerxy_w_h

def main():
    read_item_from_file()
    global global_times,global_scale,global_background_multi,item_dict
    i_want_index=0
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', type=int, default='5', help='Number of times generate')
    parser.add_argument('--num_each', type=str, default='0', help='Number of object in each frame')
    parser.add_argument('--scale', type=float, default='1.0', help='persentage of size change')
    FLAGS = parser.parse_args()

    numbertimes=FLAGS.num
    global_scale=FLAGS.scale
    num_each_frame=FLAGS.num_each
    num_each_frame=num_each_frame.split(',')
    
    data_dir=os.listdir("data/")   
    path_ground="background/"
    directory_background = os.fsencode(path_ground)
    filename_ground = os.listdir(directory_background)
    
    centerxy_w_h=list()
    
    for num_frame in num_each_frame:
        
        for each_filename_ground in filename_ground:
            path_ground="background/"
            file_ground=each_filename_ground.decode("utf-8")
            
            path_ground=path_ground + file_ground
            a=cv2.imread(path_ground)
            a_w,a_h,_=a.shape
            del a
            global_background_multi=a_w*a_h
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

                    temp_number=file_img.split('.')
                    number=temp_number[0]
                    path_label=path_label+number+".png"    
                    
                    roi,roi_mask=find_mask(path_label,path_img)

                    if(times==0):
                        src,ground_truth,centerxy_w_h = overlay(roi,roi_mask,path_ground,"0",i,centerxy_w_h)
                    else:
                        src,ground_truth,centerxy_w_h = overlay(roi,roi_mask,"temp/temp_img.png","temp/temp_label.png",i,centerxy_w_h)
                    
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


                        f = open("output/yaml/obj_"+str(i_want_index)+".yaml", "w")
                        f.write("label_names:\n")
                        f.write("- _background_\n")
                        for item_to_yaml in data_dir_want:
                            if item_to_yaml==data_dir_want[len(data_dir_want)-1]:
                                f.write("- "+item_to_yaml)
                            else :    
                                f.write("- "+item_to_yaml+"\n")

                        f = open("output/yolo_mark/obj_"+str(i_want_index)+".txt", "w")
                        iiiiii=0
                        for yolo_mark_simulator in data_dir_want:
                            f.write(str(item_dict[yolo_mark_simulator])+' ')
                            center_x=float("{:.6f}".format(float(centerxy_w_h[iiiiii][1]/a_h)))
                            center_y=float("{:.6f}".format(float(centerxy_w_h[iiiiii][0]/a_w)))
                            w_yolo=float("{:.6f}".format(float(centerxy_w_h[iiiiii][3]/a_h)))
                            h_yolo=float("{:.6f}".format(float(centerxy_w_h[iiiiii][2]/a_w)))
                            f.write(str(center_x)+' '+str(center_y)+' '+str(w_yolo)+' '+str(h_yolo))
                            f.write('\n')
                            iiiiii=iiiiii+1

                        #print(centerxy_w_h)
                        centerxy_w_h=list()
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