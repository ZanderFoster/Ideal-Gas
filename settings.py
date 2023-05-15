# Barrel Parameters
barrel_length = 1 # length in meters
barrel_radius = 0.3 # radius in meters
initial_pressure = 101325 # pressure in Pascals

#bullet parameters
bullet_mass = 1 # mass in kg
bullet_initial_velocity = 0

class Gun:
    def __init__(self, initial_volume, initial_pressure, barrel_length, barrel_radius):
        self.initial_volume = initial_volume
        self.volume = initial_volume
        self.initial_pressure = initial_pressure
        self.pressure = initial_pressure
        self.barrel_length = barrel_length
        self.barrel_radius = barrel_radius

class Bullet:
    def __init__(self, mass, initial_velocity, inital_position):
        self.mass = mass
        self.velocity = initial_velocity
        self.inital_position = inital_position
        self.position = inital_position

