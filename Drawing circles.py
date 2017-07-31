import cv2
from numpy import arange as range #renaming arange as range to increase readability and speed
from math import radians,cos,sin

def draw_circle(h,v,r):
    x=[]
    y=[]
    for i in range(0,360):
        x.append(h+r*cos(radians(i)))
        y.append(v+r*sin(radians(i)))
    return (x,y)

camera1 = cv2.VideoCapture(0)
l1 = draw_circle(100,100,100)[0]
l2 = draw_circle(100,100,100)[1]
p=360
subtrahend=180 #subrahend can't be a float as it is used in indexing. Maximum value: 180, Minimum value: 1
p+=subtrahend
while True:
    frame = camera1.read()[1]
    for x in range(len(l1)-p):
        cv2.line(frame,(int(l1[x]),int(l2[x])),(int(l1[x+1]),int(l2[x+1])),(255,0,0),2)
    cv2.imshow('view',frame)
    p-=subtrahend #the speed at which the circle is created is dependant on the subtrahend, the lower the integer value, the faster it is made
    if p == 0:
        p=360
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera1.release()
cv2.destroyAllWindows()
