"""Cyborg : combinaison d'un humain et d'un robot"""
from humain import Humain
from robot import Robot


class Cyborg(Humain, Robot):
    """test"""

    def __init__(self, name, sexe):
        Robot.__init__(self, name)
        Humain.__init__(self, sexe)
        self.name = name
        self.sexe = sexe

    def __str__(self):
        return f"{Robot.__str__(self)}\n{Humain.__str__(self)}"

if __name__=="__main__":
    cyborg = Cyborg("Deux Ex Machina", "M")

    print(cyborg.name, "sexe", cyborg.sexe)
    print("Charging battery...")
    cyborg.robot_charging()
    cyborg.robot_power_on()
    print("State: ", cyborg.robot_status())
    cyborg.humain_nourriture("banana")
    cyborg.humain_nourriture(["oignon", "chips"])
    cyborg.humain_digestion()
    print(cyborg)
