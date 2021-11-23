from djitellopy import Tello

tello = Tello()

tello.connect()

tello.takeoff()

# tello move
tello.move_up(50)
tello.move_forward(100)
tello.rotate_clockwise(360)
tello.move_back(70)

tello.land()

pass