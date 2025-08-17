import math
import numpy as np
import matplotlib.pyplot as plt

from afterburner_functions import *
from turbine_outputs import *

f_ab = calculate_f_ab(cp_ab, T06, T05, LHV)
ab_fuel_mass_flow= calculate_ab_fuel_mass_flow(f_ab, m_total)
m_new = calculate_m_flow_new(m_total, ab_fuel_mass_flow)
h06= calculate_h06(cp_ab, T06)
energy_flow_ab_exit= calculate_energy_flow_ab(m_new, h06)
P06= calculate_P06(P05, loss_fraction=0.05)

print(f"Fuel-to-air ratio in afterburner: {f_ab:.4f}")
print(f"Fuel mass flow rate in afterburner: {ab_fuel_mass_flow:.4f} kg/s")
print(f"New total mass flow rate after afterburner: {m_new:.4f} kg/s")
print(f"Specific enthalpy at afterburner exit: {h06:.4f} J/kg")
print(f"Energy flow at afterburner exit: {energy_flow_ab_exit:.4f} W")
print(f"Pressure at afterburner exit: {P06:.4f} Pa")


# Plotting the results

# Energy flow increase

plt.figure()
plt.title('Energy Flow Comparison: Afterburner vs. Turbine')
plt.bar(['Turbine Exit', 'Afterburner Exit'], [exit_energy_flow, energy_flow_ab_exit], color=['blue', 'red'])
plt.ylabel('Energy Flow (W)')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()

# Stag Enthalpy increase plot

plt.figure()
plt.title('Stagnation Enthalpy Increase in Afterburner')
plt.bar([' Before AB (h05)', ' After AB (h06)'], [h05, h06], color=['green', 'orange'])
plt.ylabel('Specific Enthalpy (J/kg)')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()

# Mass flow rate increase plot

plt.figure()
plt.title('Mass Flow Rate Comparison: Before and After Afterburner')
plt.bar(['Before Afterburner', 'After Afterburner'], [m_total, m_new], color=['purple', 'cyan'])
plt.ylabel('Mass Flow Rate (kg/s)')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()

#AB energy distribution plot

delta_energy=energy_flow_ab_exit - exit_energy_flow
plt.figure()
plt.title('Energy Distribution in Afterburner')
plt.pie([exit_energy_flow, delta_energy], labels=['Turbine Exit Energy', 'Afterburner Energy Increase'], autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()


