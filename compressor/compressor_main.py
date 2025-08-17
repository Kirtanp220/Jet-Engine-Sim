import math
import numpy as np
import matplotlib.pyplot as plt

from inlet_outputs import *
from compressor_functions import *


P02 = calculate_stag_pressure_2(P01, rp)
T02 = calculate_stag_temperature_2(T01, eta_c, gamma, P02, P01)
h0_2 = calculate_stag_enthalpy_2(T02, cp)
energy_flow_2 = energy_flow_2(h0_2, m_flow)

print(f"Stagnation pressure at compressor exit: {P02:.2f} Pa")
print(f"Stagnation temperature at compressor exit: {T02:.2f} K")
print(f"Stagnation enthalpy at compressor exit: {h0_2:.2f} J/kg")
print(f"Energy flow through the compressor: {energy_flow_2:.2f} W")

# Plotting the results

# Stagnation Pressure Rise
stations = ['Inlet', 'Compressor Exit']
pressures = [P01, P02]
plt.figure(figsize=(10, 5))
plt.bar(stations, pressures, color=['blue', 'orange'])
plt.title('Stagnation Pressure Rise')
plt.ylabel('Pressure (Pa)')
plt.xlabel('Stations')
plt.grid(True)
plt.tight_layout()
plt.show()

# Stagnation Temperature Rise
stations = ['Inlet', 'Compressor Exit']
temperatures = [T01, T02]
plt.figure(figsize=(10, 5))
plt.bar(stations, temperatures, color=['blue', 'orange'])
plt.title('Stagnation Temperature Rise')
plt.ylabel('Temperature (K)')
plt.xlabel('Stations')
plt.grid(True)
plt.tight_layout()
plt.show()

# Energy Flow
stations = ['Inlet', 'Compressor Exit']
energy_flows = [36403465.05, energy_flow_2]  
plt.figure()
plt.plot(stations, energy_flows, marker='o', label='Energy Flow')
plt.title("Energy Flow Throughout Compressor")
plt.ylabel('Energy Flow (W)')
plt.xlabel('Station')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Compressor Sensitivity Plot
efficiencies = np.linspace(0.8, 1.0, 100)
T02_eff_range = [calculate_stag_temperature_2(T01, eta,  gamma, P02, P01,)
    for eta in efficiencies]
plt.figure()
plt.plot(efficiencies, T02_eff_range, color='green', label='T02 vs n_c')
plt.axhline(y=T02, color='orange', linestyle='--', label=f'Current T02= {T02:.2f}K')
plt.axvline(x=eta_c, color='red', linestyle='--', label=f'Current n_c = {eta_c}')
plt.title('Compressor Exit Temp vs Efficiency')
plt.xlabel('Compressor Efficiency (n_c)')
plt.ylabel('Stagnation Temp at Exit (K)')
plt.legend()
plt.tight_layout()
plt.show()

