from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
color = ColorSensor("E")

# Write your program here.
hub.speaker.play_sound("Damage")
amount_red = color.get_red()
if amount_red != None:
    hub.speaker.play_sound("Damage")
else:
    hub.speaker.play_sound("Celebrate")


