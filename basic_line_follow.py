from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
# Movement definitions
hub = MSHub()
distance_sensor = DistanceSensor('F')
motor_pair_front = MotorPair('A', 'B')
motor_pair_back = MotorPair('C', 'D')
motor_pair_left = MotorPair('B', 'C')
motor_pair_right = MotorPair('A', 'D')
motor_front_left = Motor("A")
motor_front_right = Motor("B")
motor_back_left = Motor("C")
motor_back_right = Motor("D")
distance_sensor.light_up_all(100)
## Write your program here.

print(distance_sensor.get_distance_cm())

def convert_distance_to_time(distance):
    desired_run_time = float(distance / 43)
    return desired_run_time

# This makes Gelo walk in the specified direction for the specified number of seconds.
def move_straight_for_seconds(seconds):
    motor_front_left.start(speed=-100)
    motor_front_right.start(speed=100)
    motor_back_left.start(speed=-100)
    motor_back_right.start(speed=100)
    wait_for_seconds(seconds)
    motor_front_left.stop()
    motor_front_right.stop()
    motor_back_left.stop()
    motor_back_right.stop()

def move_back_for_seconds(seconds):
    motor_front_left.start(speed=100)
    motor_front_right.start(speed=-100)
    motor_back_left.start(speed=100)
    motor_back_right.start(speed=-100)
    wait_for_seconds(seconds)
    motor_front_left.stop()
    motor_front_right.stop()
    motor_back_left.stop()
    motor_back_right.stop()


def turn_left_for_seconds(seconds):
    motor_front_left.start(speed=100)
    motor_front_right.start(speed=100)
    motor_back_left.start(speed=100)
    motor_back_right.start(speed=100)
    wait_for_seconds(seconds)
    motor_front_left.stop()
    motor_front_right.stop()
    motor_back_left.stop()
    motor_back_right.stop()


def turn_right_for_seconds(seconds):
    motor_front_left.start(speed=-100)
    motor_front_right.start(speed=-100)
    motor_back_left.start(speed=-100)
    motor_back_right.start(speed=-100)
    wait_for_seconds(seconds)
    motor_front_left.stop()
    motor_front_right.stop()
    motor_back_left.stop()
    motor_back_right.stop()
#End Movement functions


# Create your objects here.
hub = MSHub()
color_sensor = ColorSensor("E")

# Write your program here.
hub.speaker.beep()

while True:
    current_color = color_sensor.get_color()

    wait_for_seconds(1)

    while current_color == 'black':
        move_straight_for_seconds(1)
        wait_for_seconds(0.25)
        current_color = color_sensor.get_color()

    while current_color != 'black':
        hub.motion_sensor.reset_yaw_angle()

        while hub.motion_sensor.get_yaw_angle() > -90 and color_sensor.get_color() != 'black':
            turn_left_for_seconds(0.5)
            wait_for_seconds(0.25)

        while hub.motion_sensor.get_yaw_angle() < 90 and color_sensor.get_color() != 'black':
            turn_right_for_seconds(0.25)
            wait_for_seconds(0.25)

        current_color = color_sensor.get_color()

hub.speaker.beep()
hub.speaker.doom-eternal-soundtrack
