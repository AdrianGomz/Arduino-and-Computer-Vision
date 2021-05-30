import cv2
import time
import Hand_Traking_Module as htm
import time
import math
import pyfirmata
import time
ard=pyfirmata.Arduino("COM15")
# d digital 9 number s signal
servo_motor=ard.get_pin('d:9:s')
servoControl='len'
servo_motor.write(180)

withdCam,heigtCam=540,380

camera=cv2.VideoCapture(0)
camera.set(3,withdCam)
camera.set(4,heigtCam)
hand=htm.findHands(detection_confidence=0.9)

ptime=0
sendTime=0    
baseVal=100/6
    




while True:
    confirm, img=camera.read()
    img=hand.drawHands(img)
    lmList=hand.handPoints(img,draw=False)


    current_time=time.time()
    fps=1/(current_time-ptime)
    ptime=current_time
    if len(lmList)!=0:
        x_thumb,y_thumb=lmList[4][1], lmList[4][2]  
        x_index,y_index=lmList[8][1], lmList[8][2]   


        cv2.circle(img,(x_thumb,y_thumb),10,(255,255,0),cv2.FILLED)
        cv2.circle(img,(x_index,y_index),10,(255,255,0),cv2.FILLED)
        cv2.line(img,(x_thumb,y_thumb),(x_index,y_index),(255,255,0),4)

        ang=math.atan2((y_thumb-y_index),(x_thumb-x_index))*180/math.pi
        per=math.sqrt((y_index-y_thumb)**2+(x_index-x_thumb)**2)*4/5
        if servoControl=='ang':
            if ang>180:
                pMot=180
            elif ang<0:
                pMot=0
            else:
                pMot=ang
            
            servo_motor.write(pMot)
        if servoControl=='len':
            if per>=100:
                pMot=100*180/100
            else:
                pMot=per*180/100
            servo_motor.write(pMot)

        if per>baseVal:
            ard.digital[3].write(1)
        else:
            ard.digital[3].write(0)
        if per>baseVal*2:
            ard.digital[4].write(1)
        else:
            ard.digital[4].write(0)
        if per>baseVal*3:
            ard.digital[5].write(1)
        else:
            ard.digital[5].write(0)
        if per>baseVal*4:
            ard.digital[6].write(1)
        else:
            ard.digital[6].write(0)
        if per>baseVal*5:
            ard.digital[7].write(1)
        else:
            ard.digital[7].write(0)
        if per>baseVal*6:
            per==100
            ard.digital[8].write(1)
        else:
            ard.digital[8].write(0)

        
            
        sendTime=current_time
        

    ptime=current_time
    cv2.putText(img,f'FPS:{int(fps)}',(10,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,250,0),2)
    if len(lmList)!=0:
        cv2.putText(img,f'Per:{int(per)}%',(10,60), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,250,0),2)
        cv2.putText(img,f'Ang:{int(pMot)}',(10,90), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,250,0),2)

    cv2.imshow("Camara", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    

