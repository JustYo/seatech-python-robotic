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
        """Robot allumé"""
        self.__power = True

    def robot_power_off(self):
        """Robot éteint"""
        self.__power = False

    def robot_charging(self):
        """Démarre la charge du robot"""
        if self.__battery_level != 100:
            for i in range(0, 101):
                sleep(0.1)
                self.__battery_level = i
                print(self.__battery_level, "%")
        else:
            print("Battery already full")

    def robot_speed(self, speed: int):
        """Définit la vitesse du robot"""
        if self.__power:
            self.__current_speed = speed
        else:
            self.__current_speed = 0

    def robot_status(self):
        """Define l'état d'allumage du robot"""
        return self.__states[self.__power]

    def __str__(self):
        return f"name: {self.__name}, power: {self.__states[self.__power]}, charge: {self.__battery_level}%, speed: {self.__current_speed} km/h"


# main
if __name__ == "__main__":
    robot_name = input("Donner un nom à votre robot : ")
    monrobot = Robot(robot_name)
    monrobot.robot_power_on()
    monrobot.robot_charging()
    robot_vitesse = input("Rentrer la vitesse du robot : ")
    monrobot.robot_speed(robot_vitesse)
    print(monrobot)
