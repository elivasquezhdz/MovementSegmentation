import cv2
import os
import sys
import imutils


imgpath = sys.argv[1]#Source folder
namp = sys.argv[2] #Folder to write files

def movdet(imx,imy,ind):
	imc = cv2.imread(imx,0) #copy of the image to crop without boxes
	im0 = cv2.imread(imx,0) #Reads frame in gray
	im1 =cv2.imread(imy,0) #Reads frame in gray
	im1 = cv2.GaussianBlur(im1,(21,21),0)
	imD = cv2.absdiff(im0,im1)
	thr = cv2.threshold(imD,25,255, cv2.THRESH_BINARY)[1]
	thr = cv2.dilate(thr, None, iterations=2)
	(cnts, _) = cv2.findContours(thr.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	idx = 0
	for c in cnts:
		if cv2.contourArea(c) < 200:#min area, could be define as arg later
			continue
		(x,y,w,h) = cv2.boundingRect(c)
		cv2.rectangle(im0,(x,y),(x+w,y+h),(255,255,0),1)
		if(w>19 and h >20): #limit 20x20 boxes
			crop = imc[y:y+h,x:x+w]
			idx+=1
			cv2.imwrite('crop\\'+ "it" + str(ind) + '_' + str(idx) + '.jpg',crop)
		
def main():
	iters = 0
	lim0 = int(sys.argv[1])
	lim1 = int(sys.argv[2])
	for i in range(lim0,lim1):
		ima = imgpath + namp + str(i) + ".jpg"
		imb = imgpath  + namp + str(i+1) + ".jpg"
		movdet(ima,imb,iters)
		iters+=1
	print ("done with " + str(iters) + " images") 

main()
