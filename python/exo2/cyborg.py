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
        self.weapons = ""
        self.style = ""

    def select_weapons(self):
        """Give weapons to the robot"""
        weapons_selected = input("Choose your weapon soldier (hands, katana, laser saber) : ")
        self.weapons = weapons_selected

    def fight_style(self):
        """Robot fight style"""
        if self.weapons == "hand":
            self.style = "Boxe"
        elif self.weapons == "katana":
            self.style = "Ninja"
        elif self.style == "laser saber":
            self.style = "Jedi"
        else:
            self.style = "Chuck Norris"


    def __str__(self):
        return f"Cyborg : weapon: {self.weapons}, fight style: {self.style}\n{Robot.__str__(self)}\n{Humain.__str__(self)}"

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
    cyborg.select_weapons()
    cyborg.fight_style()
    print(cyborg)
