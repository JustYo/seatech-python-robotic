"""Deuxième exercice"""
from robot import Robot

class Humain(Robot):
    """Création d'un humain"""
    __sexe = ""
    __nourriture = []
    __digestion = ["Vomis", "Digestion bonne"]
    __state = True

    def __init__(self, sexe):
        self.__sexe = sexe

    def humain_nourriture(self, nourriture: list):
        """Initialise les nourritures de l'humain"""
        self.__nourriture = nourriture

    def humaindigestion(self):
        """L'humain ne digère pas l'oignon"""
        if "oignon" in self.__nourriture:
            self.__state = False
        else:
            self.__state = True

    def __str__(self):
        return f"sexe: {self.__sexe}, nourriture: {self.__nourriture}, digestion: {self.__digestion[self.__state]}"
