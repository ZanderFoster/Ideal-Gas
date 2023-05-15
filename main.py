import CoolProp.CoolProp as cp
import numpy as np
import matplotlib.pyplot as plt

def simulate_gas_expansion(initial_pressure, initial_volume, initial_temp, final_volume, gas='hydrogen', iteration_step=0.001):
    molar_mass = cp.PropsSI('MOLAR_MASS', gas)
    R = cp.PropsSI('GAS_CONSTANT', gas) / molar_mass

    initial_mass = initial_pressure * initial_volume / (R * initial_temp)

    volumes = [initial_volume]
    pressures = [initial_pressure]
    temperatures = [initial_temp]

    if final_volume < initial_volume:
        step = 1.0 - iteration_step  # Decrease the volume in each step
        check_volume = lambda v: v > final_volume  # Check if current volume is greater than final volume
        min_pressure = 1e-2  # Minimum pressure allowed
    else:
        step = 1.0 + iteration_step  # Increase the volume in each step
        check_volume = lambda v: v < final_volume  # Check if current volume is smaller than final volume
        min_pressure = 0.0  # No minimum pressure for expansion

    volume_tolerance = 1e-2  # Tolerance for volume difference
    pressure_tolerance = 1e-2  # Tolerance for pressure difference

    while abs(volumes[-1] - final_volume) / initial_volume > volume_tolerance and abs(pressures[-1]) / initial_pressure > pressure_tolerance and check_volume(volumes[-1]):
        final_mass = initial_mass * (initial_volume / volumes[-1])

        final_pressure = (final_mass * R * temperatures[-1]) / volumes[-1]
        final_pressure = max(final_pressure, min_pressure)  # Enforce minimum pressure

        volumes.append(volumes[-1] * step)
        pressures.append(final_pressure)

        final_temp = (initial_temp * initial_volume) / (volumes[-1] * (initial_mass / final_mass))
        temperatures.append(final_temp)

    volumes = np.array(volumes)
    pressures = np.array(pressures)
    temperatures = np.array(temperatures)

    return volumes, pressures, temperatures


initial_pressure = 4200.0  # bar
initial_volume = 1  # m^3
initial_temp = 300.0  # Kelvin
final_volume = 0.1  # m^3 (can be smaller or larger than initial volume)

iteration_step = 0.001  # iteration step size in %

volumes, pressures, temperatures = simulate_gas_expansion(initial_pressure, initial_volume, initial_temp, final_volume, iteration_step=iteration_step)

plt.plot(volumes, pressures, label='Pressure')
plt.plot(volumes, temperatures, label='Temperature')
plt.xlabel('Volume (m^3)')
plt.ylabel('Pressure (bar) / Temperature (K)')
plt.title('Expansion of Hydrogen Gas')
plt.legend()
plt.grid(True)
plt.show()
