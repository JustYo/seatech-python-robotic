"""My controller"""

from math import fabs, inf
import sys

from controller import Motor, PositionSensor, Robot


TIME_STEP = 16

# PR2 constants
MAX_WHEEL_SPEED = 3.0  # maximum velocity for the wheels [rad / s]
WHEELS_DISTANCE = 0.4492  # distance between 2 caster wheels [m]
SUB_WHEELS_DISTANCE = 0.098  # distance between 2 sub wheels of a caster wheel [m]
WHEEL_RADIUS = 0.08  # wheel radius
M_PI_4 = 0.785398163397448309616  # pi/4
M_PI = 3.14159265358979323846  # pi

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
    rotation_motors = []
    rotation_sensors = []

    def almost_equal(a, b):
        return (a < b + TOLERANCE) and (a > b - TOLERANCE)

    def step(self):
        """Throw step error"""
        if self.robot.step(TIME_STEP) == -1:
            sys.exit()

    def initialize_devices(self):
        """Initialise all the devices for wheels"""
        self.wheel_motors.append(self.robot.getDevice("fl_caster_l_wheel_joint"))
        self.wheel_motors.append(self.robot.getDevice("fl_caster_r_wheel_joint"))
        self.wheel_motors.append(self.robot.getDevice("fr_caster_l_wheel_joint"))
        self.wheel_motors.append(self.robot.getDevice("fr_caster_r_wheel_joint"))
        self.wheel_motors.append(self.robot.getDevice("bl_caster_l_wheel_joint"))
        self.wheel_motors.append(self.robot.getDevice("bl_caster_r_wheel_joint"))
        self.wheel_motors.append(self.robot.getDevice("br_caster_l_wheel_joint"))
        self.wheel_motors.append(self.robot.getDevice("br_caster_r_wheel_joint"))

        for i in range(len(self.wheel_motors)):
            self.wheel_sensors.append(Motor.getPositionSensor(self.wheel_motors[i]))

        self.rotation_motors.append(self.robot.getDevice("fl_caster_rotation_joint"))
        self.rotation_motors.append(self.robot.getDevice("fr_caster_rotation_joint"))
        self.rotation_motors.append(self.robot.getDevice("bl_caster_rotation_joint"))
        self.rotation_motors.append(self.robot.getDevice("br_caster_rotation_joint"))

        for i in range(len(self.rotation_motors)):
            self.rotation_sensors.append(
                Motor.getPositionSensor(self.rotation_motors[i])
            )

    def enable_devices(self):
        """Enable devices initialized in the class"""
        for i in range(0, 7):
            PositionSensor.enable(self.wheel_sensors[i], TIME_STEP)
            # init the motors for speed control
            Motor.setPosition(self.wheel_motors[i], float(inf))
            Motor.setVelocity(self.wheel_motors[i], 0.0)

        for i in range(len(self.rotation_motors)):
            PositionSensor.enable(self.rotation_sensors[i], TIME_STEP)

    def set_wheels_speeds(self, fll, flr, frl, frr, bll, blr, brl, brr):
        """Set velocity of 8 wheels"""
        Motor.setVelocity(self.wheel_motors[0], fll)
        Motor.setVelocity(self.wheel_motors[1], flr)
        Motor.setVelocity(self.wheel_motors[2], frl)
        Motor.setVelocity(self.wheel_motors[3], frr)
        Motor.setVelocity(self.wheel_motors[4], bll)
        Motor.setVelocity(self.wheel_motors[5], blr)
        Motor.setVelocity(self.wheel_motors[6], brl)
        Motor.setVelocity(self.wheel_motors[7], brr)

    def set_wheel_speed(self, speed):
        """Set the combined speed"""
        self.set_wheels_speeds(speed, speed, speed, speed, speed, speed, speed, speed)

    def enable_passive_wheels(self, enable):
        torques = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        if enable:
            for i in range(len(torques)):
                torques.append(Motor.getAvailableTorque(self.wheel_motors[i]))
        else:
            for i in range(len(torques)):
                Motor.setAvailableTorque(self.wheel_motors[i], torques[i])

    def set_rotation_wheels_angle(self, fl, fr, bl, br, wait_on_feedback):
        if wait_on_feedback:
            self.stop_wheels()
            self.enable_passive_wheels(True)

        Motor.setPosition(self.rotation_motors[0], fl)
        Motor.setPosition(self.rotation_motors[1], fr)
        Motor.setPosition(self.rotation_motors[2], bl)
        Motor.setPosition(self.rotation_motors[3], br)

        if wait_on_feedback:
            target = [fl, fr, bl, br]
            while True:
                all_reached = True
                for i in range(len(target)):
                    current_position = PositionSensor.getValue(self.rotation_sensors[i])
                    # if self.almost_equal(current_position, target[i]) == False:
                    if (current_position < target[i] + TOLERANCE) and (
                        current_position > target[i] - TOLERANCE
                    ) == False:
                        all_reached = False
                        break
                if all_reached:
                    break
                else:
                    self.step()
            self.enable_passive_wheels(False)

    def robot_rotate(self, angle):
        self.stop_wheels()

        self.set_rotation_wheels_angle(
            3.0 * M_PI_4, M_PI_4, -3.0 * M_PI_4, -M_PI_4, True
        )
        if angle < 0:
            max_wheel_speed = MAX_WHEEL_SPEED
        else:
            max_wheel_speed = -MAX_WHEEL_SPEED

        self.set_wheels_speeds(
            max_wheel_speed,
            max_wheel_speed,
            max_wheel_speed,
            max_wheel_speed,
            max_wheel_speed,
            max_wheel_speed,
            max_wheel_speed,
            max_wheel_speed,
        )

        initial_wheel0_position = PositionSensor.getValue(self.wheel_sensors[0])
        expected_travel_distance = fabs(
            angle * 0.5 * (WHEELS_DISTANCE + SUB_WHEELS_DISTANCE)
        )

        while True:
            wheel0_position = PositionSensor.getValue(self.wheel_sensors[0])

            wheel0_travel_distance = fabs(
                WHEEL_RADIUS * (wheel0_position - initial_wheel0_position)
            )

            if wheel0_travel_distance > expected_travel_distance:
                break

            if expected_travel_distance - wheel0_travel_distance > 0.025:
                self.set_wheels_speeds(
                    0.1 * max_wheel_speed,
                    0.1 * max_wheel_speed,
                    0.1 * max_wheel_speed,
                    0.1 * max_wheel_speed,
                    0.1 * max_wheel_speed,
                    0.1 * max_wheel_speed,
                    0.1 * max_wheel_speed,
                    0.1 * max_wheel_speed,
                )

            self.step()

            self.set_rotation_wheels_angle(0.0, 0.0, 0.0, 0.0, True)
            self.stop_wheels()

    def stop_wheels(self):
        """Stop the wheels"""
        self.set_wheels_speeds(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def robot_go_forward(self, distance):
        """Function to tell the distance for the robot"""
        max_wheel_speed = MAX_WHEEL_SPEED if distance > 0 else -MAX_WHEEL_SPEED
        self.set_wheel_speed(max_wheel_speed)

    def run(self):
        self.initialize_devices()
        self.enable_devices()
        self.robot_go_forward(0.35)
        self.robot_rotate(M_PI)
        self.robot_go_forward(0.35)


if __name__ == "__main__":
    robot = MyRobot()
    while robot.step() != 1:
        robot.run()
