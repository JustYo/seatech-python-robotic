"""My controller"""

import sys
from enum import Enum

from controller import Motor, PositionSensor, Robot


class Wheels(Enum):
    """Enumerate wheels"""

    FLL_WHEEL = 1
    FLR_WHEEL = 2
    FRL_WHEEL = 3
    FRR_WHEEL = 4
    BLL_WHEEL = 5
    BLR_WHEEL = 6
    BRL_WHEEL = 7
    BRR_WHEEL = 8


TIME_STEP = 16

# PR2 constants
MAX_WHEEL_SPEED = 3.0  # maximum velocity for the wheels [rad / s]
WHEELS_DISTANCE = 0.4492  # distance between 2 caster wheels [m]
SUB_WHEELS_DISTANCE = 0.098  # distance between 2 sub wheels of a caster wheel [m]
WHEEL_RADIUS = 0.08  # wheel radius

# function to check if a  is almost equal to another
TOLERANCE = 0.05  # arbitrary value


class MyRobot:
    """An object which configure my robot"""

    robot = Robot()
    wide_stereo_l_stereo_camera_sensor = robot.getDevice(
        "wide_stereo_l_stereo_camera_sensor"
    )
    wide_stereo_r_stereo_camera_sensor = robot.getDevice(
        "wide_stereo_r_stereo_camera_sensor"
    )
    high_def_sensor = robot.getDevice("high_def_sensor")
    r_forearm_cam_sensor = robot.getDevice("r_forearm_cam_sensor")
    l_forearm_cam_sensor = robot.getDevice("l_forearm_cam_sensor")
    laser_tilt = robot.getDevice("laser_tilt")
    base_laser = robot.getDevice("base_laser")
    wheel_motors = []
    wheel_sensors = []

    def almost_equal(self, a, b):
        """Equal comparaison"""
        return a < b + TOLERANCE and a > b - TOLERANCE

        # Simpler step function

    def step(self):
        """Throw step error"""
        if self.robot.step(TIME_STEP) == -1:
            sys.exit()

    def initialize_devices(self):
        """Initialise all the devices for wheels"""
        self.wheel_motors[Wheels(Enum).FLL_WHEEL] = self.robot.getDevice(
            "fl_caster_l_wheel_joint"
        )
        self.wheel_motors[Wheels(Enum).FLR_WHEEL] = self.robot.getDevice(
            "fl_caster_r_wheel_joint"
        )
        self.wheel_motors[Wheels(Enum).FRL_WHEEL] = self.robot.getDevice(
            "fr_caster_l_wheel_joint"
        )
        self.wheel_motors[Wheels(Enum).FRR_WHEEL] = self.robot.getDevice(
            "fr_caster_r_wheel_joint"
        )
        self.wheel_motors[Wheels(Enum).BLL_WHEEL] = self.robot.getDevice(
            "bl_caster_l_wheel_joint"
        )
        self.wheel_motors[Wheels(Enum).BLR_WHEEL] = self.robot.getDevice(
            "bl_caster_r_wheel_joint"
        )
        self.wheel_motors[Wheels(Enum).BRL_WHEEL] = self.robot.getDevice(
            "br_caster_l_wheel_joint"
        )
        self.wheel_motors[Wheels(Enum).BRR_WHEEL] = self.robot.getDevice(
            "br_caster_r_wheel_joint"
        )

        for i in range(1, 8):
            self.wheel_sensors[i] = Motor(self.wheel_motors[i])

    def enable_devices(self):
        """Enable devices initialized in the class"""
        for i in range(1, 8):
            PositionSensor(self.wheel_sensors[i], TIME_STEP)
            # init the motors for speed control
            Motor.setPosition(self.wheel_motors[i], 10)
            Motor.setVelocity(self.wheel_motors[i], 0.0)

    def set_wheels_speeds(self, fll, flr, frl, frr, bll, blr, brl, brr):
        """Set velocity of 8 wheels"""
        Motor.setVelocity(self.wheel_motors[Wheels(Enum).FLL_WHEEL], fll)
        Motor.setVelocity(self.wheel_motors[Wheels(Enum).FLR_WHEEL], flr)
        Motor.setVelocity(self.wheel_motors[Wheels(Enum).FRL_WHEEL], frl)
        Motor.setVelocity(self.wheel_motors[Wheels(Enum).FRR_WHEEL], frr)
        Motor.setVelocity(self.wheel_motors[Wheels(Enum).BLL_WHEEL], bll)
        Motor.setVelocity(self.wheel_motors[Wheels(Enum).BLR_WHEEL], blr)
        Motor.setVelocity(self.wheel_motors[Wheels(Enum).BRL_WHEEL], brl)
        Motor.setVelocity(self.wheel_motors[Wheels(Enum).BRR_WHEEL], brr)

    def set_wheels_speed(self, speed):
        """Set the combined speed"""
        self.set_wheels_speeds(speed, speed, speed, speed, speed, speed, speed, speed)

    def stop_wheels(self):
        """Stop the wheels"""
        self.set_wheels_speeds(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def enable_passive_wheels(self, enable: bool):
        """Enable the torques"""
        torques = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        if enable:
            for i in range(1, 8):
                Motor.available_torque(0.0)
        else:
            for i in range(1, 8):
                Motor.available_torque(torques[i])

    def robot_go_forward(self, distance):
        """Function to tell the distance for the robot"""
        max_wheel_speed = max_wheel_speed = (
            MAX_WHEEL_SPEED if distance > 0 else -MAX_WHEEL_SPEED
        )
        self.set_wheels_speed(max_wheel_speed)
