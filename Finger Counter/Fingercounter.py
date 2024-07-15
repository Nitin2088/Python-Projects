import cv2
import time
import os
import mediapipe as mp

wCam, hCam = 640, 550

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderpath = "Fingerimages"
myList = os.listdir(folderpath)
print(myList)
overlayList = []

for impath in myList:
    image = cv2.imread(f'{folderpath}/{impath}')
    overlayList.append(image)
print(len(overlayList))

pTime = 0

# Initialize mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.75)
mp_draw = mp.solutions.drawing_utils

# Finger tip landmarks
tipIds = [4, 8, 12, 16, 20]

def find_position(img, hand_landmarks, draw=True):
    lm_list = []
    if hand_landmarks:
        my_hand = hand_landmarks[0]
        for id, lm in enumerate(my_hand.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append([id, cx, cy])
            if draw:
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    return lm_list

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm_list = find_position(img, results.multi_hand_landmarks, draw=False)
            
            if lm_list:
                fingers = []

                # Thumb
                if lm_list[tipIds[0]][1] > lm_list[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Other 4 fingers
                for id in range(1, 5):
                    if lm_list[tipIds[id]][2] < lm_list[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                
                total_fingers = fingers.count(1)
                if total_fingers <= len(overlayList):
                    h, w, c = overlayList[total_fingers].shape
                    img[0:h, 0:w] = overlayList[total_fingers]

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
