import math
import numpy as np
import matplotlib.pyplot as plt

from combustor_outputs import *
from turbine_functions import *



turbine_work_req = calculate_turbine_work_req(W_compressor, n_mech)
T05_prime = calculate_T05_prime(T04, W_compressor, cp_turbine, m_total)
T05 = calculate_T05(T04, n_turbine, T05_prime)
P05 = calculate_P05(P04, T05_prime, T04, gamma_turbine)
h05 = calculate_h05(cp_turbine, T05)
exit_energy_flow = calculate_exit_energy_flow(h05, m_total)



print(f"Turbine work required: {turbine_work_req:.2f} W")
print(f"T05' (required temperature drop): {T05_prime:.2f} K")
print(f"T05 (stagnation temperature at turbine exit): {T05:.2f} K")
print(f"P05 (stagnation pressure at turbine exit): {P05:.2f} Pa")
print(f"h05 (stagnation enthalpy at turbine exit): {h05:.2f} J/kg")
print(f"Exit energy flow: {exit_energy_flow:.2f} W")



# Graphical representation of the turbine performance

# Pressure drop plot

plt.figure()
plt.title('Turbine Stag Pressure Drop')
plt.plot([ ' P04 (Inlet)', ' P05 (Exit) '], [P04, P05], marker='s', linestyle='--', linewidth=2, color='blue')
plt.ylabel('Stag Pressure (Pa)')
plt.grid(True)
plt.tight_layout()
plt.show()


# Temp drop plot

plt.figure()
plt.title('Turbine Stag Temperature Drop')
plt.plot([ ' T04 (Inlet)', "T05' (Ideal) ", 'T05 (Actual) '], [T04, T05_prime, T05], marker='o', linestyle='--', linewidth=2, color='red')
plt.ylabel('Stag Temperature (K)')
plt.grid(True)
plt.tight_layout()
plt.show()


# Energy flow throughout turbine

energy_out = exit_energy_flow #actualenergy left 
energy_in = W_compressor / n_mech # energy required for turbine

plt.figure()
plt.title('Turbine Energy Flow')
plt.bar(['Required Turbine Work', 'Exit Energy Flow'], [energy_in, energy_out], color=['orange', 'green'])
plt.ylabel('Power (W)')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()


# Enthalpy drop plot

W_left_in_flow = exit_energy_flow  # energy left in flow
W_irrev_loss = cp_turbine * (T05 - T05_prime) * m_total  # irreversible loss in energy
W_compressor = W_compressor  # work done by the compressor

labels = ['Compressor Work', 'Irreversible Loss', 'Exit Energy Flow']  
values = (W_compressor, W_irrev_loss, W_left_in_flow)

plt.figure()
plt.title('Turbine Enthalpy Drop')
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral', 'lightgreen'])
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()