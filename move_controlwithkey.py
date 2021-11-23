from djitellopy import Tello

import cv2

tello = Tello()

tello.connect()

stream = cv2.imread('./tello_img.jpg')
cv2.imshow('tello image', stream)

# move control with keyboard
while True:
    key = cv2.waitKey(1)
    if key == ord('t'):
        tello.takeoff()
    elif key == ord('u'):
        tello.move_up(20)
    elif key == ord('f'):
        tello.move_forward(20)
    elif key == ord('c'):
        tello.rotate_clockwise(90)
    elif key == ord('b'):
        tello.move_back(20)
    elif key == ord('l'):
        tello.land()
    elif key == ord('q'):
        break

pass