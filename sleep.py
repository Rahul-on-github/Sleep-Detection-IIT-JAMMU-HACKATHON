import cv2
import time
import requests
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml') 
cap = cv2.VideoCapture(0)

i=0
while 1: 
  
    
    ret, img = cap.read() 
  
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  
    for (x,y,w,h) in faces:
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
  
        
        eyes = eye_cascade.detectMultiScale(roi_gray) 
        if len(eyes)==0:
            
                print("eyes are closed{0}".format(i))
                i=i+1
                font = cv2.FONT_HERSHEY_SIMPLEX   
            
               # time.sleep(1)
                if i>30:
                    cv2.putText(img, "Sleepy", (x,y), font, 1, (0,0,255), 2)   
                    r =requests.get('http://www.iotclouddata.com/22log/134/iot22.php?A=' + str("Person X is sleepy"))
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

   
      
    cv2.imshow('img',img)
  
    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
  
# Close the window
cap.release()
  
# De-allocate any associated memory usage
cv2.destroyAllWindows() 