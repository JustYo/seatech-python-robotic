""" You can use classes below or create your own 👍️"""

from abc import ABCMeta, abstractmethod

class UnmannedVehicle(metaclass=ABCMeta):
    """
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """

    @abstractmethod
    def get_brand(self):
        """Get the brand of a vehicule"""

    @abstractmethod
    def get_fuel(self):
        """Get fuel"""

    @abstractmethod
    def nohuman_presentation(self):
        """Test if the vehicul is unmanned"""

    @classmethod
    @abstractmethod
    def get_default_brand(cls):
        """Get the default brand"""

class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    altitude = 0
    passengers = 0
    fuel = ""
    brand = "aerial_default"

    @abstractmethod
    def __init__(self, altitude, passengers, fuel, brand):
        """Initialise the aerial vehicule object"""

    @abstractmethod
    def get_altitude(self):
        """Get the altitude"""

    @abstractmethod
    def get_passengers(self):
        """Get the passengers number"""

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    wheels = 0
    horse_power = 0
    fuel = ""
    brand = "ground_default"

    @abstractmethod
    def __init__(self, wheels, horse_power, fuel, brand):
        """Initialisation of ground vehicule"""

    @abstractmethod
    def get_wheels(self):
        """get wheels number"""

    @abstractmethod
    def get_horse_power(self):
        """Get the number of horse power"""

class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    veh_type = ""
    deep = 0
    fuel = ""
    brand = "undersea_default"

    @abstractmethod
    def __init__(self, veh_type, deep, fuel, brand):
        """Initialise the undersea vehicule"""

    @abstractmethod
    def get_veh_type(self):
        """Get the undersea vehicule type"""

    @abstractmethod
    def get_deep(self):
        """Get the deepness"""

class UAV(AerialVehicle, UnmannedVehicle):
    """Unmanned Aerial Vehicle"""
    def __init__(self, altitude, passengers, fuel, brand):
        self.altitude = altitude
        self.passengers = passengers
        self.fuel = fuel
        self.brand = brand

    def get_altitude(self):
        """Get the altitude"""
        return self.altitude

    def get_brand(self):
        """Get the brand"""
        return self.brand

    def get_fuel(self):
        """Get the fuel"""
        return self.fuel

    def get_passengers(self):
        """Get the number of passengers"""
        return self.passengers

    @classmethod
    def get_default_brand(cls):
        return cls.brand

    def nohuman_presentation(self):
        uav = UAV(self.altitude, self.brand, self.fuel, self.passengers)
        return f"From Unmanned Vehicule : defaultbrand : {uav.get_default_brand()} brand : {self.brand}, fuel : {self.fuel}"

    def uav_presentation(self):
        """Present the aerial vehicule"""
        return f"From Aerial Vehicule : altitude : {self.altitude}, passengers : {self.passengers}"

class UUV(UnderseaVehicle, UnmannedVehicle):
    """Unmanned Undersea Vehicle"""
    def __init__(self, veh_type, deep, fuel, brand):
        self.veh_type = veh_type
        self.deep = deep
        self.fuel = fuel
        self.brand = brand

    def get_deep(self):
        """Get the deep"""
        return self.deep

    def get_veh_type(self):
        return self.veh_type

    def get_brand(self):
        """Get the brand"""
        return self.brand

    def get_fuel(self):
        """Get the fuel"""
        return self.fuel

    @classmethod
    def get_default_brand(cls):
        return cls.brand

    def nohuman_presentation(self):
        uuv = UUV(self.deep, self.veh_type, self.brand, self.fuel)
        return f"From Unmanned Vehicule : defaultbrand : {uuv.get_default_brand()} | brand : {self.brand} | fuel : {self.fuel}"

    def uuv_presentation(self):
        """Present the vehicule"""
        return f"From Undersea Vehicule : deepness : {self.deep} | vehicule type : {self.veh_type}"

class UGV(GroundVehicle, UnmannedVehicle):
    """Unmanned Ground Vehicle"""
    def __init__(self, wheels, horse_power, fuel, brand):
        self.wheels = wheels
        self.horse_power = horse_power
        self.fuel = fuel
        self.brand = brand

    def get_wheels(self):
        return self.wheels

    def get_horse_power(self):
        return self.horse_power

    def get_brand(self):
        """Get the brand"""
        return self.brand

    def get_fuel(self):
        """Get the fuel"""
        return self.fuel

    @classmethod
    def get_default_brand(cls):
        return cls.brand

    def nohuman_presentation(self):
        ugv = UGV(self.wheels, self.horse_power, self.brand, self.fuel)
        return f"From Unmanned Vehicule : defaultbrand : {ugv.get_default_brand()} | brand : {self.brand} | fuel : {self.fuel}"

    def ugv_presentation(self):
        """Present the vehicule"""
        return f"From Ground Vehicule : wheels : {self.wheels} | horse power : {self.horse_power}"

class Transformers(UUV, UGV, UAV):
    """Clone all the previous classes"""
    name = ""
    good_bad_guy = ""

    def __init__(self, name, good_bad_guy, veh_type, deep, wheels, horse_power, altitude, passengers, fuel, brand):
        """Init all the classes"""
        UUV.__init__(self, veh_type, deep, fuel, brand)
        UGV.__init__(self, wheels, horse_power, fuel, brand)
        UAV.__init__(self, altitude, passengers, fuel, brand)
        self.name = name
        self.good_bad_guy = good_bad_guy

    def trans_presentation(self):
        """All presentations"""
        self.uav_presentation()
        self.ugv_presentation()
        self.uuv_presentation()
        return f"I am {self.name} and I am a {self.good_bad_guy} guy\n{self.uav_presentation()}\n{self.ugv_presentation()}\n{self.uuv_presentation()}"


if __name__=='__main__':
    uav = UAV(300, 400, "Kerozen", "Airbus")
    print(uav.nohuman_presentation())
    print(uav.uav_presentation())

    uuv = UUV("Sous-marin touristique", -400, "Essence", "iFremer")
    print(uuv.nohuman_presentation())
    print(uuv.uuv_presentation())

    ugv = UGV(8, 1000, "Diezel", "Mercedes")
    print(ugv.nohuman_presentation())
    print(ugv.ugv_presentation())

    transformers = Transformers("Optimus Prime", "Good", "Transformers", -1000, 4, 500, 600, 4, "Essence extraterrestre", "Decepticons")
    print(transformers.trans_presentation())
