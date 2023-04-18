#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

gripper_motor = Motor(Port.A)

elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])

base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

touch_sensor = TouchSensor(Port.S1)

def closegrip():  
    ev3.screen.print("CLOSE GRIP")
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0) 

def elbowup():
    ev3.screen.print("ELBOW UP")
    elbow_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=50)
    elbow_motor.reset_angle(90) 

def opengrip():
    ev3.screen.print("OPEN GRIP")
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0) 
    gripper_motor.run_target(200, -90)

def elbowdown():
    ev3.screen.print("ELBOW DOWN")
    elbow_motor.run_until_stalled(-50, then=Stop.COAST, duty_limit=50)

def pickup():
    ev3.screen.print("PICK UP")

    pickupposition(90)    
    elbowup()
    opengrip()
    elbowdown()
    closegrip()
    elbowup()
    ev3.speaker.beep()

def pickupposition(position):

    elbowup()
    base_motor.run_target(60, position)

def setbaseposition():
    ev3.screen.print("SETTING BASE POSITION...")

    elbowup()

    base_motor.run(-100)
    while not touch_sensor.pressed():
        pass
    base_motor.stop()
    wait(1000)
    base_motor.reset_angle(0)

    ev3.screen.print("BASE POSITION FOUND")


elbow_motor.control.limits(speed=120, acceleration=120)
base_motor.control.limits(speed=120, acceleration=120)


setbaseposition()

pickup()

ev3.speaker.beep()


