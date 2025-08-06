import math
import numpy as np
import matplotlib.pyplot as plt

from combustor_functions import *
from compressor_outputs import *

T04 = calculate_T04(T03, f, n_b, LHV, cp)
h04 = calculate_exit_enthalpy(cp, T04)
P04 = calculate_P04(P03, p_loss_ratio)
m_f = calculate_fuel_mass_flow_rate(m_dot, f)
m_total = calculate_mass_flow_total(m_dot, f)
E04 = calculate_energy_flow_rate(m_total, h04)
Φ = calculate_equivalence_ratio(f, f_stoich)
q_added = calculate_q_added(LHV, m_f)
temp_rise = calculate_temp_rise(T03, T04)
enthalpy_rise = calculate_enthalpy_rise(T04, T03, cp)        



print(f"Stagnation temperature at combustor exit: {T04:.2f} K")
print(f"Exit enthalpy at combustor exit: {h04:.2f} J/kg")
print(f"Stagnation pressure at combustor exit: {P04:.2f} Pa")
print(f"Fuel mass flow rate: {m_f:.2f} kg/s")
print(f"Total mass flow rate: {m_total:.2f} kg/s")
print(f"Energy flow at combustor exit: {E04:.2f} W")
print(f"Equivalence ratio: {Φ:.2f}")
print(f"Heat added in combustor: {q_added:.2f} W")
print(f"Temperature rise in combustor: {temp_rise:.2f} K")
print(f"Enthalpy rise in combustor: {enthalpy_rise:.2f} J/kg")



f_values = np.linspace(0.01, 0.04, 100)
T04_values = []
E04_values = []
q_values = []
Φ_values = []
ΔT_values = []

for f_sweep in f_values:
    T04_sweep = calculate_T04(T03, f_sweep, n_b, LHV, cp)
    h04_sweep = calculate_exit_enthalpy(cp, T04_sweep)
    P04_sweep = calculate_P04(P03, p_loss_ratio)
    m_f_sweep = calculate_fuel_mass_flow_rate(m_dot, f_sweep)
    m_total_sweep = calculate_mass_flow_total(m_dot, f_sweep)
    E04_sweep = calculate_energy_flow_rate(m_total_sweep, h04_sweep)
    Φ_sweep = calculate_equivalence_ratio(f_sweep, f_stoich)
    q_added_sweep = calculate_q_added(LHV, m_f_sweep)
    temp_rise_sweep = calculate_temp_rise(T03, T04_sweep)

    T04_values.append(T04_sweep)
    E04_values.append(E04_sweep)
    q_values.append(q_added_sweep)
    Φ_values.append(Φ_sweep)
    ΔT_values.append(temp_rise_sweep)





# Plotting results

# T04 vs F/A ratio plot
plt.figure()
plt.plot(f_values, T04_values)
plt.xlabel('Fuel to Air Ratio (f)')
plt.ylabel('Stagnation Tmperature at Combustor Exit (K)')
plt.title('T04 vs Fuel to Air Ratio')
plt.grid(True)

# Energy Flow vs F/A ratio plot
plt.figure()
plt.plot(f_values, E04_values, color='blue')
plt.xlabel('Fuel to Air Ratio (f)')
plt.ylabel('Energy Flow at Combustor Exit (W)')
plt.title('Energy Flow vs Fuel to Air Ratio')
plt.grid(True)

# Temp Rise vs F/A ratio plot
plt.figure()
plt.plot(f_values, ΔT_values, color='green')
plt.xlabel('Fuel to Air Ratio (f)')
plt.ylabel('Temperature Rise in Combustor (K)')
plt.title('Temperature Rise vs Fuel to Air Ratio')
plt.grid(True)

# Equivalence Ratio vs F/A ratio plot
plt.figure()
plt.plot(f_values, Φ_values, color='orange')
plt.xlabel('Fuel to Air Ratio (f)')
plt.ylabel('Equivalence Ratio (Φ)')
plt.title('Equivalence Ratio vs Fuel to Air Ratio')
plt.grid(True)

# Heat Added vs F/A ratio plot
plt.figure()
plt.plot(f_values, q_values, color='red')
plt.xlabel('Fuel to Air Ratio (f)')
plt.ylabel('Heat Added in Combustor (W)')
plt.title('Heat Added vs Fuel to Air Ratio')
plt.grid(True)

plt.show()


