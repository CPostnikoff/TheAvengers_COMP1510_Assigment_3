from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

## Create your objects here.

# initialize hub so we can use the hub.motion_sensor
hub = MSHub()

## Write your program here.

# Beep to ensure the robot has actually started the program
hub.speaker.beep()

# We'll use these variables to track the total distance travelled in 2D from inital position
y_sum = 0
x_sum = 0

# every time we make a movement, record the distance travelled in both the x and y direction
distance_y += distance * math.cos(hub.motion_sensor.get_yaw_angle())
distance_x += distance * math.sin(hub.motion_sensor.get_yaw_angle())

# determine the total distance from starting point to destination
return_distance = math.sqrt((y_sum ** 2) + (x_sum ** 2))

# now to handle the direction of return
# we will use final distance travelled to determine the angle of return
distance_triangle_angle = math.tan(y_sum / x_sum)
desired_yaw = 360 - (90 + distance_triangle_angle)

while hub.motion_sensor.get_yaw_angle() != desired_yaw:
    # move the robot
    #
    #
    #
    #

if hub.motion_sensor.get_yaw_angle() == desired_yaw:
    # activate motors, with distance = return_distance, units, 0, 100 speed) 
    #
    #
    #
 
