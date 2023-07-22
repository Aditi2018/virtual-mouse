import cv2
import numpy as np
import time
import HandTracking as ht
import autopy  # Install using "pip install autopy"
import autopy.mouse

### Variables Declaration
pTime = 0  # Used to calculate frame rate
width = 640  # Width of Camera
height = 480  # Height of Camera
frameR = 100  # Frame Rate
smoothening = 8  # Smoothening Factor
prev_x, prev_y = 0, 0  # Previous coordinates
curr_x, curr_y = 0, 0  # Current coordinates

cap = cv2.VideoCapture(0)  # Getting video feed from the webcams
cap.set(3, width)  # Adjusting size
cap.set(4, height)

detector = ht.handDetector(maxHands=1)  # Detecting one hand at max
screen_width, screen_height = autopy.screen.size()  # Getting the screen size

# Variables for click and scroll
left_click = False
right_click = False
scroll_up = False
scroll_down = False

while True:
    success, img = cap.read()
    img = detector.findHands(img)  # Finding the hand
    lmlist, bbox = detector.findPosition(img)  # Getting position of hand

    if len(lmlist) != 0:
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]

        fingers = detector.fingersUp()  # Checking if fingers are upwards
        cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255),
                      2)  # Creating boundary box
        if fingers[1] == 1 and fingers[2] == 0:  # If fore finger is up and middle finger is down
            x3 = np.interp(x1, (frameR, width - frameR), (0, screen_width))
            y3 = np.interp(y1, (frameR, height - frameR), (0, screen_height))

            curr_x = prev_x + (x3 - prev_x) / smoothening
            curr_y = prev_y + (y3 - prev_y) / smoothening

            autopy.mouse.move(screen_width - curr_x, curr_y)  # Moving the cursor
            cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
            prev_x, prev_y = curr_x, curr_y

        if fingers[1] == 1 and fingers[2] == 1:  # If both fore finger and middle finger is up
            length, img, line_info = detector.findDistance(8, 12, img)
            if length < 40:  # If distance between the two fingers is less than 40 pixels, perform a left click
                if not left_click:
                    autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
                    left_click = True
                    cv2.circle(img, (line_info[4], line_info[5]), 15, (0, 255, 0), cv2.FILLED)
            else:
                if left_click:
                    autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)
                    left_click = False

        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:  # If index, middle and ring finger are up
            length, img, line_info = detector.findDistance(8, 12, img)
            if length < 40:  # If distance between the two fingers is less than 40 pixels, perform a right click
                if not right_click:
                    autopy.mouse.toggle(autopy.mouse.Button.RIGHT, True)
                    right_click = True
                    cv2.circle(img, (line_info[4], line_info[5]), 15, (0, 255, 0), cv2.FILLED)
            else:
                if right_click:
                    autopy.mouse.toggle(autopy.mouse.Button.RIGHT, False)
                    right_click = False

        if fingers[1] == 2 and fingers[2] == 2:  # If both fore finger and middle finger are up, perform a double click
            autopy.mouse.click(autopy.mouse.Button.LEFT, 2)
            cv2.circle(img, (x1, y1), 15, (0, 255, 255), cv2.FILLED)
        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[
            4] == 1:  # If all fingers are up
            length, img, line_info = detector.findDistance(8, 12, img)
            if length > 60:  # If distance between the two fingers is greater than 60 pixels, perform a scroll
                autopy.mouse.scroll(0, int(length / 20))
    cTime = time.time()  # Current time
    fps = 1 / (cTime - pTime)  # Frame rate calculation

    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()