from hogwarts import quidditch
from gpiozero import MotionSensor

ms1 = MotionSensor(4)
ms2 = MotionSensor(17)

def find_snitch():
    if ms1.motion_detected or if ms2.motion_detected:
        return True

def foo():