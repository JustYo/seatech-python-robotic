"""Deuxième exercice"""

class Humain():
    """Création d'un humain"""
    __sexe = ""
    __nourriture = []
    __digestion = ["Vomis", "Digestion bonne"]
    __state = True

    def __init__(self, sexe):
        self.__sexe = sexe

    def humain_nourriture(self, nourriture):
        """Initialise les nourritures de l'humain"""
        if isinstance(nourriture, str):
            self.__nourriture.append(nourriture)
        elif isinstance(nourriture, list):
            for ele in nourriture:
                self.__nourriture.append(ele)
        else:
            print("Nourriture inconnue")

    def humain_digestion(self):
        """L'humain ne digère pas l'oignon"""
        if "oignon" in self.__nourriture:
            self.__state = False
        else:

            self.__state = True

    def __str__(self):
        return f"Attributs de l'Humain : Sexe: {self.__sexe}, Nourriture: {self.__nourriture}, Digestion: {self.__digestion[self.__state]}"
