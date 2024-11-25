import numpy as np
import cv2
import serial
import time
COLOUR=0

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x,'utf-8'))
    
    data = arduino.readline()
    return data

webcam=cv2.VideoCapture(0)

while(1):
    _, imageFrame=webcam.read();

    hsvFrame=cv2.cvtColor(imageFrame,cv2.COLOR_BGR2HSV)

    #DEFINING COLOR RANGE
    #RED
    red_lower=np.array([0, 100, 20],np.uint8)
    red_upper=np.array([10, 255, 255],np.uint8)
    #WHITE
    white_lower = np.array([0,0,168],np.uint8)
    white_upper = np.array([172,111,255],np.uint8)
    #BLUE
    blue_lower = np.array([100,50,50],np.uint8)
    blue_upper = np.array([130,255,255],np.uint8)
    #YELLOW
    yellow_lower = np.array([25,93,0],np.uint8)
    yellow_upper = np.array([45,255,255],np.uint8)
    #GREEN
    green_lower = np.array([65,60,60],np.uint8)
    green_upper = np.array([80,255,255],np.uint8)    
    #ORANGE
    orange_lower = np.array([10, 100, 20],np.uint8)
    orange_upper = np.array([25, 255, 255],np.uint8)

    
    red_mask=cv2.inRange(hsvFrame,red_lower,red_upper)
    white_mask=cv2.inRange(hsvFrame,white_lower,white_upper)
    blue_mask=cv2.inRange(hsvFrame,blue_lower,blue_upper)
    yellow_mask=cv2.inRange(hsvFrame,yellow_lower,yellow_upper)
    green_mask=cv2.inRange(hsvFrame,green_lower,green_upper)
    orange_mask=cv2.inRange(hsvFrame,orange_lower,orange_upper)
    
    kernel=np.ones((5,5),"uint8")
    red_mask=cv2.dilate(red_mask,kernel)
    blue_mask=cv2.dilate(blue_mask,kernel)
    white_mask=cv2.dilate(white_mask,kernel)
    yellow_mask=cv2.dilate(yellow_mask,kernel)
    green_mask=cv2.dilate(green_mask,kernel)
    orange_mask=cv2.dilate(orange_mask,kernel)

    contours,hierarchy=cv2.findContours(white_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if(area>20000):
            x,y,w,h=cv2.boundingRect(contour)
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(255,255,255),2)
            cv2.putText(imageFrame,"White Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,255,255))
            COLOUR=0
    cv2.imshow("DETECTED",imageFrame)
    
    contours,hierarchy=cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if(area>20000):
            x,y,w,h=cv2.boundingRect(contour)
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(imageFrame,"Red Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255))
            COLOUR=1
    cv2.imshow("DETECTED",imageFrame)

    contours,hierarchy=cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if(area>20000):
            x,y,w,h=cv2.boundingRect(contour)
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(imageFrame,"Blue Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))
            COLOUR=2
    cv2.imshow("DETECTED",imageFrame)

    

    contours,hierarchy=cv2.findContours(yellow_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if(area>20000):
            x,y,w,h=cv2.boundingRect(contour)
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.putText(imageFrame,"Yellow Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,255))
            COLOUR=4
    cv2.imshow("DETECTED",imageFrame)

    contours,hierarchy=cv2.findContours(green_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if(area>20000):
            x,y,w,h=cv2.boundingRect(contour)
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imageFrame,"Green Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0))
            COLOUR=3
    cv2.imshow("DETECTED",imageFrame)

    contours,hierarchy=cv2.findContours(orange_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if(area>20000):
            x,y,w,h=cv2.boundingRect(contour)
            imageFrame=cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(0,128,255),2)
            cv2.putText(imageFrame,"Orange Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,128,255))
            COLOUR=5
    cv2.imshow("DETECTED",imageFrame)
       
    if cv2.waitKey(10) &0xFF==ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break

    value = write_read(str(COLOUR))
    if value==b'0':
        print('White')
    elif value==b'1':
        print('Red')
    elif value==b'2':
        print('Blue')
    elif value==b'3':
        print('Green')
    elif value==b'4':
        print('Yellow')
    elif value==b'5':
        print('Orange')
    else:
        print('Invalid')
        print(value)
            
        
