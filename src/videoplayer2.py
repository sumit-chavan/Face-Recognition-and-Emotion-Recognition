import cv2
import numpy as np
import time

def vpl(start):
  cap = cv2.VideoCapture('1.mp4')
  if (cap.isOpened()== False): 
    print("Error opening video stream or file")

  cap.set(1,float(start)- 200)
  cnt=int(0)
  while(cap.isOpened()):
    
    ret, frame = cap.read()
    
    if ret == True:
      cv2.imshow('Media Player',frame)
      cnt=cnt+1
   
      if cnt==300:
        break

      if cv2.waitKey(25) & 0xFF == ord('q'):
        break

     
    else: 
      break
   

  cap.release()
  cv2.destroyAllWindows()
  time.sleep(1) 
