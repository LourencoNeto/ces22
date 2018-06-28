import random
import inspect
from abc import ABC, abstractmethod


class AutoMobileFactory(ABC):
    """Basic abstract Factory class for making polygons (products).
    This class has to be sublassed by a factory class that MUST implement
    the "products" method.
    A factory class can create many different polygon objects (products) without
    exposing the instantiation logic to the client. Infact, since all methods of
    this class are abstract, this class can't be instantiated at all! Also, each
    subclass of PolygonFactory should implement the "products" method and keep
    it abstract, so even that subclass can't be instatiated.
    """

    @classmethod
    @abstractmethod
    def products(cls):
        """Products that the factory can manufacture. Implement in subclass."""
        pass

    @classmethod
    @abstractmethod
    def make_automobile(cls, color=None):
        """Instantiate a random polygon from all the ones that are available.
        This method creates an instance of a product randomly chosen from all
        products that the factory class can manufacture. The 'color' property of
        the manufactured object is reassigned here. Then the object is returned.
        Parameters
        ----------
        color : str
            color to assign to the manufactured object. It replaces the color
            assigned by the factory class.
        Returns
        -------
        polygon : an instance of a class in cls.products()
            polygon is the product manufactured by the factory class. It's one
            of the products that the factory class can make.
        """
        product_name = random.choice(cls.products())
        this_module = __import__(__name__)
        polygon_class = getattr(this_module, product_name)
        polygon = polygon_class(factory_name=cls.__name__)
        if color is not None:
            polygon.color = color
        return polygon

    @classmethod
    @abstractmethod
    def color(cls):
        return "black"


class Motor_VehicleFactory(AutoMobileFactory):
    """Abstract Factory class for making triangles."""

    @classmethod
    @abstractmethod
    def products(cls):
        return tuple(["_Car", "_MotorCycle", "_Bus"])


class No_Motor_VehicleFactory(AutoMobileFactory):
    """Abstract Factory class for making quadrilaterals."""

    @classmethod
    @abstractmethod
    def products(cls):
        return tuple(["_Bike", "_Skate", "_Scooter"])


class _AutoMobile(ABC):
    """Basic abstract class for polygons.
    This class is private because the client should not try to instantiate it.
    The instantiation process should be carried out by a Factory class.
    A _Polygon subclass MUST override ALL _Polygon's abstract methods, otherwise
    a TypeError will be raised as soon as we try to instantiate that subclass.
    """

    def __init__(self, factory_name=None):
        self._color = "black"
        self._manufactured = factory_name

    def __str__(self):
        return "{} {} manufactured by {} ".format(
            self.color,
            self.__class__.__name__,
            self.manufactured,
        )

    @property
    @abstractmethod
    def family(self):
        pass

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def manufactured(self):
        return self._manufactured

    @manufactured.setter
    def manufactured(self, factory_name):
        self._manufactured = factory_name


class _Motor_Vehicle(_AutoMobile):
    """Basic concrete class for triangles."""

    @property
    def family(self):
        return "Motor Vehicles"



class _Car(_Motor_Vehicle):
    
    pass

class _MotorCycle(_Motor_Vehicle):

    pass


class _Bus(_Motor_Vehicle):
    pass


class _No_Motor_Vehicle(_AutoMobile):
    """Basic concrete class for quadrilaterals."""

    @property
    def family(self):
        return "Non-Motorized Vehicles"



class _Bike(_No_Motor_Vehicle):

    pass

class _Skate(_No_Motor_Vehicle):

    pass

class _Scooter(_No_Motor_Vehicle):
    pass


def give_me_some_automobiles(factories, color=None):
    """Interface between the client and a Factory class.
    Parameters
    ----------
    factories : list, or abc.ABCMeta
        list of factory classes, or a factory class
    color : str
        color to pass to the manufacturing method of the factory class.
    Returns
    -------
    products : list
        a list of objects manufactured by the Factory classes specified
    """
    if not hasattr(factories, "__len__"):
        factories = [factories]

    products = list()
    for factory in factories:
        num = random.randint(5, 10)
        for i in range(num):
            product = factory.make_automobile(color)
            products.append(product)

    return products


def print_automobile(automobile, show_repr=False, show_hierarchy=False):
    print(str(automobile))
    if show_repr:
        print(repr(automobile))
    if show_hierarchy:
        print(inspect.getmro(automobile.__class__))
        print("\n")


def main():
    print("Let's start with something simple: some triangles")
    motor_vehicles = give_me_some_automobiles(Motor_VehicleFactory, color="blue")
    print("{} motor_vehicles".format(len(motor_vehicles)))
    for motor_vehicle in motor_vehicles:
        print_automobile(motor_vehicle)

    print("\nuse a different factory and add a color")
    non_motorized_vehicles = give_me_some_automobiles(No_Motor_VehicleFactory)
    print("{} non_motorized_vehicles".format(len(non_motorized_vehicles)))
    for non_motorized_vehicle in non_motorized_vehicles:
        print_automobile(non_motorized_vehicle)

    print("\nand now a mix of everything. And all in red!")
    factories = [Motor_VehicleFactory, No_Motor_VehicleFactory]
    automobiles = give_me_some_automobiles(factories, color="red")
    print("{} automobiles".format(len(automobiles)))
    for automobile in automobiles:
        print_automobile(automobile)

    print(
        "we can still instantiate directly any subclass of _Polygon (but we "
        "shouldn't because they are private)"
    )
    print_automobile(_Bike())
    print("we can't instantiate _AutoMobile because it has abstract methods.")


if __name__ == "__main__":
    main()