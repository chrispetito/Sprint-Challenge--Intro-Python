# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:      #Base class

    def __init__(self, name):
        self.name = name

class FlightVehicle:
    pass

class Starship:
    pass

class GroundVehicle:
    pass

class Airplane:
    pass

class Car:
    pass

class Motorcycle:
    pass