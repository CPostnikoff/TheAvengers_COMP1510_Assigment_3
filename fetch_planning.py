from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

## Create your objects here.

# initialize hub so we can use the hub.motion_sensor
hub = MSHub()
distance_sensor = DistanceSensor('D')
motor_pair = MotorPair('A', 'B')
## Write your program here.

# Beep to ensure the robot has actually started the program
hub.speaker.beep()

# We'll use these variables to track the total distance travelled in 2D from inital position
sum_y = 0
sum_x = 0
hub.motion_sensor.reset_yaw_angle()


# motor_pair.move(2, 'cm', 100, 25)

# def rotate_right():
#     motor_pair.move(10, 'cm', 100, 25)
#     wait_for_seconds(1)

print(distance_sensor.get_distance_cm())

while distance_sensor.get_distance_cm() == None or distance_sensor.get_distance_cm() > 50:
    motor_pair.move(2, 'cm', 100, 25)
    wait_for_seconds(0.5)
    distance_to_ball = distance_sensor.get_distance_cm()
    continue

hub.speaker.play_sound("Celebrate")

motor_pair.move(distance_to_ball, 'cm', 0, 25)

# while distance_sensor.get_distance_cm() > 75:
#     rotate_right()

# distance_to_ball = distance_sensor.get_distance_cm()
# motor_pair.move(distance_to_ball/3, 'cm', 0, 25)

# while distance_sensor.get_distance_cm() > 75:
#     rotate_right()

# distance_to_ball = distance_sensor.get_distance_cm()
# motor_pair.move(distance_to_ball/2, 'cm', 0, 25)

# while distance_sensor.get_distance_cm() > 75:
#     rotate_right()

# distance_to_ball = distance_sensor.get_distance_cm()
# motor_pair.move(distance_to_ball/1, 'cm', 0, 25)


# every time we make a movement, record the distance travelled in both the x and y direction
sum_y += distance_to_ball * math.cos(hub.motion_sensor.get_yaw_angle())
sum_x += distance_to_ball * math.sin(hub.motion_sensor.get_yaw_angle())

# determine the total distance from starting point to destination
return_distance = math.sqrt((sum_y ** 2) + (sum_x ** 2))

# now to handle the direction of return
# we will use final distance travelled to determine the angle of return
desired_yaw = math.tan(sum_y / sum_x) * 180 / 3.1415926

print(desired_yaw)

while hub.motion_sensor.get_yaw_angle() != desired_yaw:
    motor_pair.move(2, 'cm', -100, 25)
    wait_for_seconds(1)
    print(hub.motion_sensor.get_yaw_angle())
    if math.isclose(hub.motion_sensor.get_yaw_angle(), desired_yaw, rel_tol = 1e-9, abs_tol = 10):
        motor_pair.move(return_distance, "cm", 0, 25)
        break

# while hub.motion_sensor.get_yaw_angle() != desired_yaw:
    # move the robot
    #
    #
    #
    #

# if hub.motion_sensor.get_yaw_angle() == desired_yaw:
    # activate motors, with distance = return_distance, units, 0, 100 speed)
    #
    #
    #
