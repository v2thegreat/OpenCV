import cv2
camera1 = cv2.VideoCapture(0)
y=60
while True:
    frame=camera1.read()[1]
    cv2.line(frame,(50,50),(50,y),(255,0,0),2)
    y+=5
    cv2.imshow('view',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
camera1.release()
cv2.destroyAllWindows()
