# virtual-mouse

Software Requirements
Pycharm IDE.
OpenCV : (Open Source Computer Vision) is a popular open-source computer vision and machine learning software library. It is used to develop real-time computer vision applications, including image and video processing, object detection and recognition, and deep learning-based face recognition.
Mediapipe : MediaPipe is an open-source framework developed by Google that provides customizable and reusable building blocks for developers and researchers to create cross-platform, real-time perception pipelines. It offers solutions for various tasks such as object detection, face detection and tracking, hand tracking
Autopy : It is a Python library for automation of GUI interactions with a computer, such as mouse and keyboard control, window manipulation, and screen captures.
An Windows10 operating system that is compatible with the gesture recognition software and camera driver.

![image](https://github.com/Aditi2018/virtual-mouse/assets/117904179/520b2f54-8298-4f6c-9166-d3064f73f266)
If the index finger is up and the middle finger is down, the code maps the position of the hand within the boundary box to the screen size and moves the cursor accordingly using the autopy.mouse.move() method. 

![image](https://github.com/Aditi2018/virtual-mouse/assets/117904179/d732436c-46b0-4645-bf2d-255d50481acb)
If both the index finger and middle finger are up, the code calculates the distance between the two fingers using the findDistance() method of the hand detector object. If the distance is less than 40 pixels, the code performs a left click using the autopy.mouse.toggle() method. If the distance is more than 40 pixels, the code releases the left click if it was previously clicked.


![Screenshot 2024-01-18 191604](https://github.com/Aditi2018/virtual-mouse/assets/117904179/90a3cf88-31dd-497c-b38e-55e334bccd82)
If both the forefinger and middle finger are up again, the code performs a double-click using the autopy.mouse.click() method.

Finally, the code calculates the frame rate, displays it on the screen, and shows the video frame with the detected hand and cursor movement using the cv2.imshow() method. The code also waits for the user to press the 'q' key to exit the program using the cv2.waitKey() method.




