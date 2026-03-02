import os
import cv2
import math
import mediapipe as mp

os.environ['LC_ALL'] = 'C'
os.environ['LANG'] = 'C.UTF-8'

mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_mesh
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
face_mesh = mp_face.FaceMesh(min_detection_confidence=0.5)

assets = {
    "index": cv2.imread('maymun.png'),
    "think": cv2.imread('maymun2.png'),
    "tongue": cv2.imread('dil.png'),
    "nah": cv2.imread('nah.png')
}

cap = cv2.VideoCapture(0)
IMG_SIZE = 200

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    hand_res = hands.process(rgb_frame)
    face_res = face_mesh.process(rgb_frame)

    display_img = None
    mouth_ptr = None

    if face_res.multi_face_landmarks:
        for face_lms in face_res.multi_face_landmarks:
            up, low = face_lms.landmark[13], face_lms.landmark[14]
            mouth_ptr = up
            if abs(up.y - low.y) > 0.008:
                display_img = assets["tongue"]

    if hand_res.multi_hand_landmarks:
        for hand_lms in hand_res.multi_hand_landmarks:
            lms = hand_lms.landmark

            idx_open = lms[8].y < lms[6].y
            others_open = [lms[12].y < lms[10].y, lms[16].y < lms[14].y, lms[20].y < lms[18].y]

            if mouth_ptr:
                dist = math.sqrt((lms[8].x * w - mouth_ptr.x * w) ** 2 + (lms[8].y * h - mouth_ptr.y * h) ** 2)
                if dist < 65:
                    display_img = assets["think"]

            if display_img is None and idx_open and not any(others_open):
                display_img = assets["index"]

            if display_img is None and not idx_open and not any(others_open):
                if abs(lms[4].x - lms[8].x) < 0.07:
                    display_img = assets["nah"]

    if display_img is not None:
        try:
            res = cv2.resize(display_img, (IMG_SIZE, IMG_SIZE))
            frame[20:20 + IMG_SIZE, -IMG_SIZE - 20:-20] = res
        except:
            pass

    cv2.imshow("Monkey Interactive Project", frame)
    if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]: break

cap.release()
cv2.destroyAllWindows()