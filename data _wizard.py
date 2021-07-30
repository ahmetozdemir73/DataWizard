# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 13:45:21 2021

@author: Ahmet
"""

import cv2 
import os
import time


global count_folder


class dataWizard:
    def __init__(self,path,cam,camBrightness=200):
        self.path=path
        self.cam=cam
        self.camBrightness=camBrightness
        

    def saveData(self,w,h,per,grayImage=False,showImage=True,minBlur=300):
        global count_folder
        count_folder=0
        while os.path.exists( self.path+ str(count_folder)):
            count_folder += 1
        os.makedirs(self.path + str(count_folder))
        
        cap = cv2.VideoCapture(self.cam)
        cap.set(3, 640)
        cap.set(4, 480)
        cap.set(10,self.camBrightness)
        
        count=0
        countSave=0
        
        while True:
            t, img = cap.read()
            img = cv2.resize(img,(w,h))
            if grayImage:
                img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            
            blur = cv2.Laplacian(img, cv2.CV_64F).var()
            if count % per ==0 and blur > minBlur:
                nowTime = time.time()
                cv2.imwrite(self.path + str(count_folder) +
                        '/' + str(countSave)+"_"+ 
                        str(int(blur))+"_"+
                        str(nowTime)+".png", img)
                countSave+=1
            count += 1
        
            if showImage:
                cv2.imshow("Frame", img)
        
            if cv2.waitKey(1) & 0xFF == 27: # press ESC to stop
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
        
        
        
if __name__ == "__main__": 
    
    myPath = 'data/images'
    x=dataWizard(myPath,0)        
    x.saveData(360,240,10)
        
        
        
        
        










