"""
Hand Tracing Module
By: Murtaza Hassan
Youtube: http://www.youtube.com/c/MurtazasWorkshopRoboticsandAI
Website: https://www.computervision.zone
"""

import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(1)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
# Fingercounter.py
# import cv2
# import time
# import os
# import HandTrackingModule as htm

# wCam, hCam = 640, 480

# cap = cv2.VideoCapture(1)
# cap.set(3, wCam)
# cap.set(4, hCam)

# folderPath = "FingerImages"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList = []
# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     # print(f'{folderPath}/{imPath}')
#     overlayList.append(image)

# print(len(overlayList))
# pTime = 0

# detector = htm.handDetector(detectionCon=0.75)

# tipIds = [4, 8, 12, 16, 20]

# while True:
#     success, img = cap.read()
#     img = detector.findHands(img)
#     lmList = detector.findPosition(img, draw=False)
#     # print(lmList)

#     if len(lmList) != 0:
#         fingers = []

#         # Thumb
#         if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
#             fingers.append(1)
#         else:
#             fingers.append(0)

#         # 4 Fingers
#         for id in range(1, 5):
#             if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
#                 fingers.append(1)
#             else:
#                 fingers.append(0)

#         # print(fingers)
#         totalFingers = fingers.count(1)
#         print(totalFingers)

#         h, w, c = overlayList[totalFingers - 1].shape
#         img[0:h, 0:w] = overlayList[totalFingers - 1]

#         cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
#         cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
#                     10, (255, 0, 0), 25)

#     cTime = time.time()
#     fps = 1 / (cTime - pTime)
#     pTime = cTime

#     cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
#                 3, (255, 0, 0), 3)

#     cv2.imshow("Image", img)
#     cv2.waitKey(1)