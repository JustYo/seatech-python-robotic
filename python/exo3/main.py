""" You can use classes below or create your own 👍️"""

from abc import ABCMeta, abstractmethod

class UnmannedVehicle(metaclass=ABCMeta):
    """
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @property
    @abstractmethod
    def get_brand(self):
        """Get the brand of a vehicule"""

    @property
    @abstractmethod
    def get_horse_power(self):
        """Get horse power"""

    @property
    @abstractmethod
    def set_fuel(self, fuel):
        """set fuel"""

    @property
    @abstractmethod
    def get_fuel(self):
        """Get fuel"""

    @abstractmethod
    def nohuman(self):
        """Test if the vehicul is unmanned"""

    @classmethod
    @abstractmethod
    def get_default_brand(cls):
        """Get the default brand"""

class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""

    @abstractmethod
    def set_altitude(self, altitude: int):
        """Set the altitude"""

    @abstractmethod
    def set_passengers(self, passengers: int):
        """Set passengers number"""

    @abstractmethod
    def get_altitude(self):
        """Get the altitude"""

    @abstractmethod
    def get_passengers(self):
        """Get the passengers number"""

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def set_wheels(self, wheels: int):
        """Set wheels number"""

    @abstractmethod
    def set_horse_power(self, horse_power: int):
        """Set the number of horse power"""

    @abstractmethod
    def get_wheels(self):
        """get wheels number"""

    @abstractmethod
    def get_horse_power(self):
        """Get the number of horse power"""

class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def set_veh_type(self, veh_type):
        """Set the undersea vehicule type"""

    @abstractmethod
    def set_deep(self, depth: int):
        """Set the deepness"""

    @abstractmethod
    def get_veh_type(self):
        """Get the undersea vehicule type"""

    @abstractmethod
    def get_deep(self):
        """Get the deepness"""

class UAV(UnmannedVehicle, AerialVehicle):
    """Unmanned Aerial Vehicle"""
    brand = ""
    horse_power = 2
    fuel = ""

class UUV(UnmannedVehicle, UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    pass

class UGV(UnmannedVehicle, GroundVehicle):
    """Unmanned Ground Vehicle"""
    pass
