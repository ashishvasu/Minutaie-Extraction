import cv2
import fingerprint_feature_extractor
import os
import skimage
import math
import csv


if __name__ == '__main__':
    input_dir='C:\\Users\\ASHISH\\Desktop\\input\\'
    output_dir='C:\\Users\\ASHISH\\Desktop\\output\\'
    output1_dir='C:\\Users\\ASHISH\\Desktop\\output1\\'

    count=1
    count1=0
    count2=1
    pi=22/7
    for image in os.listdir(input_dir):
        X=[]
        Y=[]
        Z=0
        Z1=0
        Z2=0
        img = cv2.imread(f'{input_dir}/{image}', 0)				# read the input image --> You can enhance the fingerprint image using the "fingerprint_enhancer" library
        #(x,y)=img.shape
        #print(x," ",y)
        FeaturesTerminations, FeaturesBifurcations,X,Y = fingerprint_feature_extractor.extract_minutiae_features(img, showResult=True)
        # write content of X and Y in new file
        X_sort=[]
        Y_sort=[]
        X_sort=X
        Y_sort=Y
        X_sort.sort()
        Y_sort.sort()
        X_min=X[0]
        X_max=X[len(X)-1]
        Y_min=Y[0]
        Y_max=Y[len(Y)-1]
        x=(X_max-X_min)
        y=(Y_max-Y_min)
        output_filename = f'{count}.txt'
        count+=1
        output_path = output_dir + output_filename
        output_file = open(output_path, "w")
        # write X and Y in output path
        for i in range(len(X)):
            cur_x = X[i]
            cur_y = Y[i]
            #print(f'{cur_x} {cur_y}')
            # write cur_x cur_y endl
            output_file.write(f'{cur_x} {cur_y}\n')
        output_file.close()
        p=((X_max-X_min)/9)
        q=((Y_max-Y_min)/9)
        q=max(p,q)
        p=max(p,q)
        print(p," ",q)
        count1+=1
        output1_filename = f'{count1}.csv'
        output1_path = output1_dir + output1_filename
        output1_file = open(output1_path, "w")
        for i in range(len(X)):
            for j in range(0,91):
                X1=(float)((X[i]-(x/2))*math.cos((pi/180)*j))-((Y[i]-(y/2))*math.sin((pi/180)*j))+x/2
                Y1=(float)((X[i]-(x/2))*math.sin((pi/180)*j))+((Y[i]-(y/2))*math.cos((pi/180)*j))+y/2
                X1=X1-X_min
                Y1=Y1-Y_min
                if int(X1/p) == 0:
                    if int(Y1/q)==0:
                        Z=0
                    if int(Y1/q)==1:
                        Z=1
                    if int(Y1/q)==2:
                        Z=2
                    if int(Y1/q)==3:
                        Z=3
                    if int(Y1/q)==4:
                        Z=4
                    if int(Y1/q)==5:
                        Z=5
                    if int(Y1/q)==6:
                        Z=6
                    if int(Y1/q)==7:
                        Z=7
                    if int(Y1/q)>=8:
                        Z=8
                    if int(Y1/q)<0 and int(Y1/q)>9:
                        Z=None
                if int(X1/p) == 1:
                    #print("z[i]=1")
                    if int(Y1/q)==0:
                        Z=10
                    if int(Y1/q)==1:
                        Z=11
                    if int(Y1/q)==2:
                        Z=12
                    if int(Y1/q)==3:
                        Z=13
                    if int(Y1/q)==4:
                        Z=14
                    if int(Y1/q)==5:
                        Z=15
                    if int(Y1/q)==6:
                        Z=16
                    if int(Y1/q)==7:
                        Z=17
                    if int(Y1/q)>=8:
                        Z=18
                    if int(Y1/q)<0 and int(Y1/q)>9:
                        Z=None
                if int(X1/p) == 2:
                    if int(Y1/q)==0:
                        Z=20
                    if int(Y1/q)==1:
                        Z=21
                    if int(Y1/q)==2:
                        Z=22
                    if int(Y1/q)==3:
                        Z=23
                    if int(Y1/q)==4:
                        Z=24
                    if int(Y1/q)==5:
                        Z=25
                    if int(Y1/q)==6:
                        Z=26
                    if int(Y1/q)==7:
                        Z=27
                    if int(Y1/q)>=8:
                        Z=28
                    if int(Y1/q)<0 and int(Y1/q)>9:
                        Z=None
                if int(X1/p) == 3:
                    if int(Y1/q)==0:
                        Z=30
                    if int(Y1/q)==1:
                        Z=31
                    if int(Y1/q)==2:
                        Z=32
                    if int(Y1/q)==3:
                        Z=33
                    if int(Y1/q)==4:
                        Z=34
                    if int(Y1/q)==5:
                        Z=35
                    if int(Y[i]/q)==6:
                        Z=36
                    if int(Y1/q)==7:
                        Z=37
                    if int(Y1/q)>=8:
                        Z=38
                    if int(Y1/q)<0 and int(Y1/q)>9:
                        Z=None
                if int(X1/p) == 4:
                    if int(Y1/q)==0:
                        Z=40
                    if int(Y1/q)==1:
                        Z=41
                    if int(Y1/q)==2:
                        Z=42
                    if int(Y1/q)==3:
                        Z=43
                    if int(Y1/q)==4:
                        Z=44
                    if int(Y1/q)==5:
                        Z=45
                    if int(Y1/q)==6:
                        Z=46
                    if int(Y1/q)==7:
                        Z=47
                    if int(Y1/q)>=8:
                        Z=48
                    if int(Y1/q)<0 and int(Y1/q)>9:
                        Z=None
                if int(X1/p) == 5:
                    if int(Y1/q)==0:
                        Z=50
                    if int(Y1/q)==1:
                        Z=51
                    if int(Y1/q)==2:
                        Z=52
                    if int(Y1/q)==3:
                        Z=53
                    if int(Y1/q)==4:
                        Z=54
                    if int(Y1/q)==5:
                        Z=55
                    if int(Y1/q)==6:
                        Z=56
                    if int(Y1/q)==7:
                        Z=57
                    if int(Y1/q)>=8:
                        Z=58
                    if int(Y1/q)<0 and int(Y1/q)>9:
                        Z=None
                if int(X1/p) == 6:
                    if int(Y1/q)==0:
                        Z=60
                    if int(Y1/q)==1:
                        Z=61
                    if int(Y1/q)==2:
                        Z=62
                    if int(Y1/q)==3:
                        Z=63
                    if int(Y1/q)==4:
                        Z=64
                    if int(Y1/q)==5:
                        Z=65
                    if int(Y1/q)==6:
                        Z=66
                    if int(Y1/q)==7:
                        Z=67
                    if int(Y1/q)>=8:
                        Z=68
                    if int(Y1/q)<0 and int(Y1/q)>9:
                        Z=None
                if int(X1/p) == 7:
                    if int(Y1/q)==0:
                        Z=70
                    if int(Y1/q)==1:
                        Z=71
                    if int(Y1/q)==2:
                        Z=72
                    if int(Y1/q)==3:
                        Z=73
                    if int(Y1/q)==4:
                        Z=74
                    if int(Y1/q)==5:
                        Z=75
                    if int(Y[i]/q)==6:
                        Z=76
                    if int(Y1/q)==7:
                        Z=77
                    if int(Y1/q)>=8:
                        Z=78
                    if int(Y1/q)<0 and int(Y1/q)>9:
                        Z=None
                if int(X1/p )>=8:
                    if int(Y1/q)==0:
                        Z=80
                    if int(Y1/q)==1:
                        Z=81
                    if int(Y1/q)==2:
                        Z=82
                    if int(Y1/q)==3:
                        Z=83
                    if int(Y1/q)==4:
                        Z=84
                    if int(Y1/q)==5:
                        Z=85
                    if int(Y1/q)==6:
                        Z=86
                    if int(Y1/q)==7:
                        Z=87
                    if int(Y1/q)>=8:
                        Z=88
                    if int(Y1/q)<0 and int(Y1/q)>9:
                        Z=None
                if int(X1/p)<0 and int(X1/p) > 9:
                    Z=-1
                p1=(x/5)
                q1=(y/5)
                print(p," ",q)
                if int(X1/p1) == 0:
                    if int(Y1/q1)==0:
                        Z1=0
                    if int(Y1/q1)==1:
                        Z1=1
                    if int(Y1/q1)==2:
                        Z1=2
                    if int(Y1/q1)==3:
                        Z1=3
                    if int(Y1/q1)>=4:
                        Z1=4
                    if int(Y1/q1)<0 and int(Y1/q1)>5:
                        Z1=None
                if int(X1/p1) == 1:
                    #print("z[i]=1")
                    if int(Y1/q1)==0:
                        Z1=10
                    if int(Y1/q1)==1:
                        Z1=11
                    if int(Y1/q1)==2:
                        Z1=12
                    if int(Y1/q1)==3:
                        Z1=13
                    if int(Y1/q1)>=4:
                        Z1=14
                    if int(Y1/q1)<0 and int(Y1/q1)>5:
                        Z1=None
                if int(X1/p1) == 2:
                    if int(Y1/q1)==0:
                        Z1=20
                    if int(Y[i]/q1)==1:
                        Z1=21
                    if int(Y1/q1)==2:
                        Z1=22
                    if int(Y1/q1)==3:
                        Z1=23
                    if int(Y1/q1)>=4:
                        Z1=24
                    if int(Y1/q1)<0 and int(Y1/q1)>5:
                        Z1=None
                if int(X1/p1) == 3:
                    if int(Y1/q1)==0:
                        Z1=30
                    if int(Y1/q1)==1:
                        Z1=31
                    if int(Y1/q1)==2:
                        Z1=32
                    if int(Y1/q1)==3:
                        Z1=33
                    if int(Y1/q1)>=4:
                        Z1=34
                    if int(Y1/q1)<0 and int(Y1/q1)>5:
                        Z1=None
                if int(X1/p1) >= 4:
                    if int(Y1/q1)==0:
                        Z1=40
                    if int(Y1/q1)==1:
                        Z1=41
                    if int(Y1/q1)==2:
                        Z1=42
                    if int(Y1/q1)==3:
                        Z1=43
                    if int(Y1/q1)>=4:
                        Z1=44
                    if int(Y1/q1)<0 and int(Y1/q1)>5:
                        Z1=None
                if int(X1/p1)<0 and int(X1/p1) > 5:
                    Z1=-1
                p2=(x/3)
                q2=(y/3)
                if int(X1/p2) == 0:
                    if int(Y1/q2)==0:
                        Z2=0
                    if int(Y1/q2)==1:
                        Z2=1
                    if int(Y1/q2)>=2:
                        Z2=2
                    if int(Y1/q1)<0 and int(Y1/q2)>3:
                        Z2=None
                if int(X1/p2) == 1:
                    #print("z[i]=1")
                    if int(Y1/q2)==0:
                        Z2=10
                    if int(Y1/q2)==1:
                        Z2=11
                    if int(Y1/q2)>=2:
                        Z2=12
                    if int(Y1/q2)<0 and int(Y1/q2)>3:
                        Z2=None
                if int(X1/p2) >= 2:
                    if int(Y1/q2)==0:
                        Z2=20
                    if int(Y1/q2)==1:
                        Z2=21
                    if int(Y1/q2)>=2:
                        Z2=22
                    if int(Y1/q2)<0 and int(Y1/q2)>3:
                        Z2=None
                if int(X1/p2)<0 and int(X1/p2) > 3:
                    Z2=-1

        
                # write X and Y in output path
                #print(len(X)," ",len(Z1))
                cur_x = X[i]
                cur_y = Y[i]
                cur_z = Z
                cur_z1=Z1
                cur_z2=Z2
                #print(f'{cur_x} {cur_y}')
                # write cur_x cur_y endl
                if j==0:
                    output1_file.write(f'{cur_x},{cur_y},{cur_z},{cur_z1},{cur_z2}')
                else:
                    output1_file.write(f',{cur_z},{cur_z1},{cur_z2}')
            output1_file.write(f'\n')
        output1_file.close()
        X.clear()
        Y.clear()
