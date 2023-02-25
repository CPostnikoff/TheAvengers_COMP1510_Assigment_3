from mindstorms import DistanceSensor, MSHub, Motor, MotorPair, ColorSensor, App

# Initialize the Distance Sensor.
hub = MSHub()
wall_detector = DistanceSensor('F')
# Measure the distance between the Distance Sensor and object in centimeters and inches.
dist_cm = wall_detector.get_distance_cm()
dist_inches = wall_detector.get_distance_inches()
# Print both results on the console.
print('cm:', dist_cm, 'inches:', dist_inches)
hub.speaker.play_sound("Damage")
if dist_cm > 10:
    hub.speaker.play_sound("Damage")
else:
    hub.speaker.play_sound("Celebrate")
