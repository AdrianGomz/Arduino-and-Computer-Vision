import cv2
import mediapipe as mp



class findHands():
    def __init__(self,static_mode=False,max_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.static_mode=static_mode
        self.max_hands=max_hands
        self.detection_confidence=detection_confidence
        self.tracking_confidence=tracking_confidence

        self.hands_ms=mp.solutions.hands
        self.hand_object=mp.solutions.hands.Hands(self.static_mode,self.max_hands,self.detection_confidence,self.tracking_confidence)
        self.mpDraw=mp.solutions.drawing_utils
    
    def drawHands(self,frame,draw=True):

        imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.processed_image=self.hand_object.process(imgRGB)


        # If we detect a hand we will draw the lines and points for each and detected
        if self.processed_image.multi_hand_landmarks:
            for hand_in_image in self.processed_image.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, hand_in_image, self.hands_ms.HAND_CONNECTIONS)
        return frame


    def handPoints(self, frame, handNo=0, draw=True):
        landmark_list=[]
        if self.processed_image.multi_hand_landmarks:
            hand=self.processed_image.multi_hand_landmarks[handNo]
            for id, landmark in enumerate(hand.landmark):
                    height, width, color= frame.shape
                    Px, Py=int(landmark.x*width),int(landmark.y*height)
                    landmark_list.append([id,Px,Py])
        return landmark_list

def main():
    cap=cv2.VideoCapture(0)
    detector=findHands()

    while True:
        suc, frame=cap.read()

        frame=detector.drawHands(frame)
        lmList=detector.handPoints(frame)
        if len(lmList)!=0:
            print(lmList[4])
        cv2.imshow('Webcam',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__=='__main__':
    main()