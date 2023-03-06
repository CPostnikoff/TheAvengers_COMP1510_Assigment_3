from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

## Create your objects here.

# initialize hub so we can use the hub.motion_sensor
hub = MSHub()
color_sensor = ColorSensor('E')
distance_sensor = DistanceSensor('F')
motor_pair = MotorPair("C", "D")
motor_left = Motor("C")
motor_right = Motor("D")
motor_arm = Motor("A")
distance_sensor.light_up_all(100)
## Write your program here.

print(distance_sensor.get_distance_cm())

# these are quakers movement commands, editied for 2 wheels
def move_straight_for_seconds(seconds):
    motor_pair.start(0, 40)
    timer = Timer()
    
    while color_sensor.get_color() == "green" and timer.now() != seconds and not motion_sensor.get_distance_cm():
        current_color = color_sensor.get_color()
        current_distance_scan = motion_sensor.get_distance_cm()

    current_color = color_sensor.get_color()
    current_distance_scan = motion_sensor.get_distance_cm()

    print(current_color)

    if current_color != "green":
        motor_pair.stop()
        move_from_boundry(seconds)
        return

    if current_distance_scan:
        motor_pair.stop()
        return


def move_from_boundry(seconds):
    motor_pair.start(0, -40)
    wait_for_seconds(seconds)
    motor_pair.stop
    turn_right_for_seconds(2)


def move_back_for_seconds(seconds):
    motor_pair.start(0, -40)
    timer = Timer()
    while color_sensor.get_color() == "green" and timer.now() != seconds:
        current_color = color_sensor.get_color()
    motor_pair.stop()


def turn_left_for_seconds(seconds):
    motor_pair.start(-100, 40)
    timer = Timer()
    while color_sensor.get_color() == "green" and timer.now() != seconds:
        current_color = color_sensor.get_color()
    motor_pair.stop()


def turn_right_for_seconds(seconds):
    motor_pair.start(100, 40)
    timer = Timer()
    while color_sensor.get_color() == "green" and timer.now() != seconds:
        current_color = color_sensor.get_color()
    motor_pair.stop()


def turn_until_detection_or_360():
    hub.motion_sensor.reset_yaw_angle()
    motor_pair.start(100, 10)
    current_turn = 0
    distance_reading
    is_close = math.isclose(current_turn, 0, abs_tol = 9)
    while not is_close:
        distance_reading = distance_sensor.get_distance_cm()
        current_turn = hub.motion_sensor.get_yaw_angle()
        if current_turn < 0:
            is_close = math.isclose(negative_turn, 0, abs_tol = 9)
    motor_pair.stop()


def check_for_red_ball():
    distance_reading = distance_sensor.get_distance_cm()
    if distance_reading != None and distance_reading >= 5:
        distance_to_move = distance_reading - 4
        motor_pair.move(distance_to_move, "cm", 0, 10)
    else:
        return


def catch_ball():
    motor_arm.run_for_degrees(-120,100)


check_for_red_ball()

# Task Program:
# while True

