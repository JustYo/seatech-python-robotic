""" You can use classes below or create your own 👍️"""

from abc import ABCMeta, abstractmethod


class UnmannedVehicle(metaclass=ABCMeta):
    """
    An autonomous vehicle have to do his mission automatically.
    This mission can be configured by an operator.
    """

    @abstractmethod
    def __init__(self, brand, fuel):
        """Initialize the unmanned vehicule"""

    @property
    @abstractmethod
    def __brand(self):
        """Get the brand of a vehicule"""

    @__brand.setter
    @abstractmethod
    def __brand(self, brand):
        """Get the brand of a vehicule"""

    @property
    @abstractmethod
    def __fuel(self):
        """Get fuel"""

    @__fuel.setter
    @abstractmethod
    def __fuel(self, fuel):
        """Get fuel"""

    @abstractmethod
    def nohuman_presentation(self):
        """Test if the vehicul is unmanned"""

    @classmethod
    @abstractmethod
    def get_default_brand(cls):
        """Get the default brand"""


class AerialVehicle(UnmannedVehicle, metaclass=ABCMeta):
    """A vehicle made for ground fields."""

    altitude = 0
    passengers = 0

    @abstractmethod
    def __init__(self, altitude, passengers):
        """Initialise the aerial vehicule object"""

    @abstractmethod
    def get_altitude(self):
        """Get the altitude"""

    @abstractmethod
    def get_passengers(self):
        """Get the passengers number"""


class GroundVehicle(metaclass=ABCMeta):
    """A vehicle made for ground fields."""

    wheels = 0
    horse_power = 0

    @abstractmethod
    def __init__(self, wheels, horse_power):
        """Initialisation of ground vehicule"""

    @abstractmethod
    def get_wheels(self):
        """get wheels number"""

    @abstractmethod
    def get_horse_power(self):
        """Get the number of horse power"""


class UnderseaVehicle(metaclass=ABCMeta):
    """A vehicle made for ground fields."""

    veh_type = ""
    deep = 0

    @abstractmethod
    def __init__(self, veh_type, deep):
        """Initialise the undersea vehicule"""

    @abstractmethod
    def get_veh_type(self):
        """Get the undersea vehicule type"""

    @abstractmethod
    def get_deep(self):
        """Get the deepness"""


class UAV(AerialVehicle, UnmannedVehicle):
    """Unmanned Aerial Vehicle"""

    __fuel = "Kérozène"
    __brand = "Airbus"

    def __init__(self, altitude, passengers):
        UnmannedVehicle.__init__(self, self.__brand, self.__fuel)
        self.altitude = altitude
        self.passengers = passengers

    def get_altitude(self):
        """Get the altitude"""
        return self.altitude

    @property
    def _UnmannedVehicle__brand(self):
        """Get the brand"""
        return self.__brand

    @property
    def _UnmannedVehicle__fuel(self):
        """Get the fuel"""
        return self.__fuel

    def get_passengers(self):
        """Get the number of passengers"""
        return self.passengers

    @_UnmannedVehicle__brand.setter
    def _UnmannedVehicle__brand(self, brand):
        self.__brand = brand

    @_UnmannedVehicle__fuel.setter
    def _UnmannedVehicle__fuel(self, fuel):
        """Get the fuel"""
        self.__fuel = fuel

    @classmethod
    def get_default_brand(cls):
        return cls.__brand

    def nohuman_presentation(self):
        method_uav = UAV(self.__fuel, self.passengers)
        return f"From Unmanned Vehicule : defaultbrand : {method_uav.get_default_brand()} brand : {self.__brand}, fuel : {self.__fuel}"

    def uav_presentation(self):
        """Present the aerial vehicule"""
        return f"Hello! I am a UAV here are my properties :\nFrom Aerial Vehicule : altitude : {self.altitude}, passengers : {self.passengers}"


class UUV(UnderseaVehicle, UnmannedVehicle):
    """Unmanned Undersea Vehicle"""

    __brand = "iFremer"
    __fuel = "Electrique"

    def __init__(self, veh_type, deep):
        UnmannedVehicle.__init__(self, self.__brand, self.__fuel)
        self.veh_type = veh_type
        self.deep = deep

    def get_deep(self):
        """Get the deep"""
        return self.deep

    def get_veh_type(self):
        return self.veh_type

    @property
    def _UnmannedVehicle__brand(self):
        """Get the brand"""
        return self.__brand

    @property
    def _UnmannedVehicle__fuel(self):
        """Get the fuel"""
        return self.__fuel

    @_UnmannedVehicle__brand.setter
    def _UnmannedVehicle__brand(self, brand):
        self.__brand = brand

    @_UnmannedVehicle__fuel.setter
    def _UnmannedVehicle__fuel(self, fuel):
        """Get the fuel"""
        self.__fuel = fuel

    @classmethod
    def get_default_brand(cls):
        return cls.__brand

    def nohuman_presentation(self):
        method_uuv = UUV(self.deep, self.veh_type)
        return f"From Unmanned Vehicule : defaultbrand : {method_uuv.get_default_brand()} | brand : {self.__brand} | fuel : {self.__fuel}"

    def uuv_presentation(self):
        """Present the vehicule"""
        return f"Hello! I am a UUV here are my properties :\nFrom Undersea Vehicule : deepness : {self.deep} | vehicule type : {self.veh_type}"


class UGV(GroundVehicle, UnmannedVehicle):
    """Unmanned Ground Vehicle"""

    __brand = "Mercedes"
    __fuel = "Essence"

    def __init__(self, wheels, horse_power):
        UnmannedVehicle.__init__(self, self.__brand, self.__fuel)
        self.wheels = wheels
        self.horse_power = horse_power

    def get_wheels(self):
        return self.wheels

    def get_horse_power(self):
        return self.horse_power

    @property
    def _UnmannedVehicle__brand(self):
        """Get the brand"""
        return self.__brand

    @property
    def _UnmannedVehicle__fuel(self):
        """Get the fuel"""
        return self.__fuel

    @_UnmannedVehicle__brand.setter
    def _UnmannedVehicle__brand(self, brand):
        self.__brand = brand

    @_UnmannedVehicle__fuel.setter
    def _UnmannedVehicle__fuel(self, fuel):
        """Get the fuel"""
        self.__fuel = fuel

    @classmethod
    def get_default_brand(cls):
        return cls.__brand

    def nohuman_presentation(self):
        method_ugv = UGV(self.wheels, self.horse_power)
        return f"From Unmanned Vehicule : defaultbrand : {method_ugv.get_default_brand()} | brand : {self.__brand} | fuel : {self.__fuel}"

    def ugv_presentation(self):
        """Present the vehicule"""
        return f"Hello! I am a UGV here are my properties :\nFrom Ground Vehicule : wheels : {self.wheels} | horse power : {self.horse_power}"


class Transformers(UUV, UGV, UAV):
    """Heritate from all the final classes to create an ultimate vehicule"""

    def __init__(
        self,
        name,
        good_bad_guy,
        veh_type,
        deep,
        wheels,
        horse_power,
        altitude,
        passengers,
    ):
        """Init all the classes"""
        UUV.__init__(self, veh_type, deep)
        UGV.__init__(self, wheels, horse_power)
        UAV.__init__(self, altitude, passengers)
        self.name = name
        self.good_bad_guy = good_bad_guy

    def trans_presentation(self):
        """All presentations"""
        self.uav_presentation()
        self.ugv_presentation()
        self.uuv_presentation()
        return f"I am {self.name} and I am a {self.good_bad_guy}\n{self.uav_presentation()}\n{self.ugv_presentation()}\n{self.uuv_presentation()}"

    @property
    def _UnmannedVehicle__brand(self):
        """Get the brand"""
        return self.__brand

    @property
    def _UnmannedVehicle__fuel(self):
        """Get the fuel"""
        return self.__fuel

    @_UnmannedVehicle__brand.setter
    def _UnmannedVehicle__brand(self, brand):
        self.__brand = brand

    @_UnmannedVehicle__fuel.setter
    def _UnmannedVehicle__fuel(self, fuel):
        """Get the fuel"""
        self.__fuel = fuel


if __name__ == "__main__":
    print("\n")
    uav = UAV(300, 400)
    print(uav.uav_presentation())
    print(uav.nohuman_presentation())

    print("\n")
    uuv = UUV("Sous-marin touristique", -400)
    print(uuv.uuv_presentation())
    print(uuv.nohuman_presentation())

    print("\n")
    ugv = UGV(8, 1000)
    print(ugv.ugv_presentation())
    print(ugv.nohuman_presentation())
    print("\n")

    transformers = Transformers(
        "Optimus Prime", "good guy", "Transformers", -1000, 4, 500, 600, 4
    )
    print(transformers.trans_presentation())
