from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
distance_sensor = DistanceSensor("D")
color_sensor = ColorSensor("C")
motor_pair = MotorPair('A', 'B')

# Write your program here.
hub.speaker.beep()

while True:
    current_color = color_sensor.get_color()
    
    wait_for_seconds(1)
    while current_color == 'black':
        motor_pair.move(2, 'cm', 0, 10)
        current_color = color_sensor.get_color()
    while current_color != 'black':
        motor_pair.move(15, 'degrees', -100, 10)
        wait_for_seconds(0.25)
        current_color = color_sensor.get_color()

hub.speaker.beep()
