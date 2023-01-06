"""Premier exercice"""
from time import sleep


class Robot:
    """Création d'un robot"""

    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ["shutdown", "running"]

    def __init__(self, name: str):
        """Définit le nom du robot"""
        self.__name = name

    def robot_power_on(self):
        """Définit si le robot est allumé"""
        self.__power = 1

    def robot_power_off(self):
        """Définit si le robot est éteint"""
        self.__power = 0

    def robot_charging(self):
        """Instancie la charge du robot"""
        if self.__battery_level != 100:
            for i in range(0, 101):
                sleep(0.1)
                self.__battery_level = i
                print(self.__battery_level, "%")
        else:
            print("Battery already full")

    def robot_speed(self, speed: int):
        """Définit la vitesse du robot"""
        self.__current_speed = speed

    def robot_status(self):
        """Define robot state"""
        return self.__states[self.__power]

    def __str__(self):
        return f"name: {self.__name}, power: {self.__states[self.__power]}, charge: {self.__battery_level}%, speed: {self.__current_speed} km/h"


monrobot = Robot("Paul")
monrobot.robot_power_on()
monrobot.robot_charging()
monrobot.robot_speed(120)
print(monrobot)
