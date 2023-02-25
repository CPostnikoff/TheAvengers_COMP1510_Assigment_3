from mindstorms import DistanceSensor

# Initialize the Distance Sensor.
wall_detector = DistanceSensor('F')

# Measure the distance between the Distance Sensor and object in centimeters and inches.
dist_cm = wall_detector.get_distance_cm()
dist_inches = wall_detector.get_distance_inches()
# Print both results on the console.
print('cm:', dist_cm, 'inches:', dist_inches)
