# Virtual Mouse

The virtual mouse system utilizes hand gesture recognition to control the mouse cursor, providing an intuitive and natural interaction with digital devices. The system employs computer vision and machine learning techniques, using OpenCV and MediaPipe libraries for hand detection and tracking. Autopy library is used to simulate mouse clicks and movements on the screen. The primary goal is to offer an alternative to traditional mouse devices, especially beneficial for individuals with disabilities or mobility impairments.

1.  Install the required libraries using pip install -r requirements.txt.
   
2.  Run the virtual_mouse.py script.

3.Use hand gestures to control the virtual mouse:
Move cursor by lifting index finger.
Left-click by lifting index and middle fingers.
Right-click by lifting all three fingers (index, middle, and ring).
Double-click by lifting index and middle fingers simultaneously.

Pycharm IDE.

OpenCV, MediaPipe, Autopy Python libraries.

![image](https://github.com/Aditi2018/virtual-mouse/assets/117904179/e9438904-9253-445b-8826-af5ae48ecc69)


![image](https://github.com/Aditi2018/virtual-mouse/assets/117904179/520b2f54-8298-4f6c-9166-d3064f73f266)
If the index finger is up and the middle finger is down, the code maps the position of the hand within the boundary box to the screen size and moves the cursor accordingly using the autopy.mouse.move() method. 

![image](https://github.com/Aditi2018/virtual-mouse/assets/117904179/d732436c-46b0-4645-bf2d-255d50481acb)
If both the index finger and middle finger are up, the code calculates the distance between the two fingers using the findDistance() method of the hand detector object. If the distance is less than 40 pixels, the code performs a left click using the autopy.mouse.toggle() method. If the distance is more than 40 pixels, the code releases the left click if it was previously clicked.


![Screenshot 2024-01-18 191604](https://github.com/Aditi2018/virtual-mouse/assets/117904179/90a3cf88-31dd-497c-b38e-55e334bccd82)
If both the forefinger and middle finger are up again, the code performs a double-click using the autopy.mouse.click() method.

Finally, the code calculates the frame rate, displays it on the screen, and shows the video frame with the detected hand and cursor movement using the cv2.imshow() method. The code also waits for the user to press the 'q' key to exit the program using the cv2.waitKey() method.




