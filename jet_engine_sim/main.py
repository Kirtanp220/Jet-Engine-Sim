import math
import numpy as np
import matplotlib.pyplot as plt

from inlet_functions import *

# Input Parameters
P1 = 101325  # Pa, Inlet Pressure
T1 = 288.15  # K, Inlet Temperature 
gamma = 1.4  # Specific heat ratio for air
R = 287.05  # J/(kg*K), Specific gas constant for air
cp = 1005  # J/(kg*K), Specific heat at constant pressure for air
eta_i = 0.96  # Efficiency of the inlet
V1 = 237  # m/s, Inlet Velocity
m_flow = 20  # kg/s, Mass flow rate
V2 = 40  # m/s, Outlet Velocity (not used in this calculation but can be used for further calculations)
eta_p = 0.99  # Efficiency of the pressure recovery

#Calculations for Inlet and Outlet
T0 = calculate_ideal_stagnation_temperature(T1, V1, cp)
T0_real = calculate_real_stagnation_temperature(T1, eta_i, T0)
P0_real = calculate_real_stagnation_pressure(P1, T0_real, T1, gamma)
P0_real_after_eta_p = calculate_real_stagnation_pressure_after_eta_p(eta_p, P0_real)
h0_real = calculate_stagnation_enthalpy(T0_real, cp)
energy_flow = calculate_energy_flow(m_flow, h0_real)
T2 = calculate_new_static_temperature_at_outlet(T1, V1, V2, cp)
M1, M2 = calculate_mach_number(T1, T2, V1, V2, R, gamma, 0, 0)  # Assuming a1 and a2 are not used in this calculation
rho1, rho2 = calculate_densities_at_inlet_outlet(P1, T1, T2, R)
area_ratio = calculate_area_ratio(V2, V1, rho1, rho2)
T0_outlet = calculate_ideal_stagnation_temperature(T2, V2, R)
P0_outlet = calculate_real_stagnation_pressure(P0_real_after_eta_p, T0_outlet, T2, gamma)
P2 = calculate_static_pressure_at_outlet(P1, T1, T2, gamma)
T0_real_outlet = T0_real
h0_real_outlet = calculate_stagnation_enthalpy(T0_real_outlet, cp)
energy_flow_outlet = calculate_energy_flow(m_flow, h0_real_outlet)
P0_actual_outlet = P0_real_after_eta_p
P0_ideal_outlet = P0_outlet
pressure_lost = calculate_pressure_lost(P0_ideal_outlet, P0_actual_outlet)

labels = ['Inlet', 'Outlet']
bar_width = 0.35  # Width of the bars
x = np.arange(len(labels))  # The label locations

# Static Pressure 
plt.figure(figsize=(8, 6))
plt.bar(x - bar_width/2, [101325, 90000], width=bar_width, label='Standard Subsonic Inlet Static Pressure', color='blue') 
plt.bar(x + bar_width/2, [P1, P2], width=bar_width, label='Calculated Static Pressure', color='orange')        
plt.title('Static Pressure Comparison')
plt.xticks(x, labels)
plt.ylabel('Pressure (Pa)')
plt.legend()
plt.grid(axis='y')
plt.show()

# Static Temperature
plt.figure(figsize=(8, 6))
plt.bar(x - bar_width/2, [288.15, 312], width=bar_width, label='Standard Subsonic Inlet Static Temperature', color='blue')
plt.bar(x + bar_width/2, [T1, T2], width=bar_width, label='Calculated Static Temperature', color='orange')
plt.title('Static Temperature Comparison')
plt.xticks(x, labels)
plt.ylabel('Temperature (K)')
plt.legend()
plt.grid(axis='y')
plt.show()

#Stagnation Pressure
plt.figure(figsize=(8, 6))
plt.bar(x - bar_width/2, [139000, 132000], width=bar_width, label='Standard Subsonic Inlet Stagnation Pressure', color='blue')
plt.bar(x + bar_width/2, [P0_ideal_outlet, P0_real_after_eta_p], width=bar_width, label='Calculated Stagnation Pressure', color='orange')
plt.title('Stagnation Pressure Comparison')
plt.xticks(x, labels)
plt.ylabel('Pressure (Pa)')
plt.legend()
plt.grid(axis='y')
plt.show()

# Stagnation Temperature
plt.figure(figsize=(8, 6))
plt.bar(x - bar_width/2, [314, 314], width=bar_width, label='Standard Subsonic Inlet Stagnation Temperature', color='blue')
plt.bar(x + bar_width/2, [T0_outlet, T0_real_outlet], width=bar_width, label='Calculated Stagnation Temperature', color='orange')
plt.title('Stagnation Temperature Comparison')
plt.xticks(x, labels)
plt.ylabel('Temperature (K)')
plt.legend()
plt.grid(axis='y')
plt.show()


# Output Results
print(f"Ideal Stagnation Temperature (T0): {T0:.2f} K")
print(f"Ideal Stagnation Pressure (P0): {(P1 * (T0 / T1)**(gamma / (gamma - 1))):.2f} Pa")

print(f"Real Stagnation Temperature (T0_real): {T0_real:.2f} K")
print(f"Real Stagnation Pressure at Station 1 (P0_real): {P0_real:.2f} Pa")
print(f"Real Stagnation Pressure after Efficiency (P0_real_after_eta_p): {P0_real_after_eta_p:.2f} Pa")
print(f"Stagnation Enthalpy (h0_real): {h0_real:.2f} J/kg")
print(f"Energy Flow (energy_flow): {energy_flow:.2f} W")

print(f"Static Temperature at Outlet (T2): {T2:.2f} K")
print(f"Ideal Stagnation Temperature at Outlet (T0_outlet): {T0_outlet:.2f} K")
print(f"Ideal Stagnation Pressure at Outlet (P0_outlet): {P0_outlet:.2f} Pa")
print(f"Static Pressure at Outlet (P2): {P2:.2f} Pa")

print(f"Real Stagnation Pressure at Outlet (P0_real_station_2): {P0_real_after_eta_p:.2f} Pa")
print(f"Real Stagnation Temperature at Outlet (T0_real_outlet): {T0_real_outlet:.2f} K")
print(f"Real Stagnation Enthalpy at Outlet (h0_real_outlet): {h0_real_outlet:.2f} J/kg")
print(f"Energy Flow at Outlet (energy_flow_outlet): {energy_flow_outlet:.2f} W")

print(f"Mach Number at Inlet (M1): {M1:.2f}")
print(f"Mach Number at Outlet (M2): {M2:.2f}")

print(f"Density at Inlet (rho1): {rho1:.2f} kg/m^3")
print(f"Density at Outlet (rho2): {rho2:.2f} kg/m^3")
print(f"Area Ratio (A1/A2): {area_ratio:.2f}")

print(f"Pressure Lost due to Inefficiencies: {pressure_lost:.2f}%")
print(f"Real Stagnation Pressure at Outlet: {P0_actual_outlet:.2f} Pa")
print(f"Ideal Stagnation Pressure at Outlet: {P0_ideal_outlet:.2f} Pa")


# Define Station Numbers
stations = [ 'Inlet', 'Outlet']
# Define Pressure Values
real_stag_pressure = [P0_real, P0_real_after_eta_p] 
ideal_stag_pressure = [P0_outlet, P0_outlet]
static_pressure = [P1, P2]

plt.figure()
plt.plot(stations, real_stag_pressure, marker='o', label='Real Stagnation Pressure')
plt.plot(stations, ideal_stag_pressure, marker='o', label='Ideal Stagnation Pressure')
plt.plot(stations, static_pressure, marker='o', label='Static Pressure')
plt.title('Transformation of Pressure in Jet Engine Inlet')
plt.xlabel('Stations')
plt.ylabel('Pressure (Pa)')
plt.legend()
plt.grid()
plt.show()
# the code graphs how the ideal, real, and static pressures change from the inlet to the outlet of the jet engine inlet.

#Define Station Numbers for Temperature
stations_temp = ['Inlet', 'Outlet']
# Define Temperature Values
real_stag_temp = [T0_real, T0_real_outlet]
ideal_stag_temp = [T0, T0_outlet]
static_temp = [T1, T2]

plt.figure()
plt.plot(stations_temp, real_stag_temp, marker='o', label='Real Stagnation Temperature')
plt.plot(stations_temp, ideal_stag_temp, marker='o', label='Ideal Stagnation Temperature')
plt.plot(stations_temp, static_temp, marker='o', label='Static Temperature')
plt.title('Transformation of Temperature in Jet Engine Inlet')
plt.xlabel('Stations')
plt.ylabel('Temperature (K)')
plt.legend()
plt.grid()
plt.show()
# the code graphs how the ideal, real, and static temperatures change from the inlet to the outlet of the jet engine inlet.

# Calculate the stagnation pressure lost due to efficiency
real_stag_pressure_loss =[P0_real,P0_real_after_eta_p]
ideal_stag_pressure_loss = [P1 * (T0 / T1)**(gamma / (gamma - 1)), P0_outlet]

plt.figure()
plt.plot(stations, real_stag_pressure_loss, marker='o', label='Real Stagnation Pressure Loss')
plt.plot(stations, ideal_stag_pressure_loss, marker='o', label='Ideal Stagnation Pressure Loss')
plt.title('Stagnation Pressure Loss in Jet Engine Inlet due to Efficiency')
plt.xlabel('Stations')
plt.ylabel('Pressure (Pa)')
plt.legend()
plt.grid()
plt.show()
# the code graphs how the real and ideal stagnation pressures change from the inlet to the outlet of the jet engine inlet, showing the pressure loss due to efficiency.

# Energy Flow Through the Inlet
energy_flow_values = [energy_flow, energy_flow_outlet]

plt.figure()
plt.plot(stations, energy_flow_values, marker='o', label='Energy Flow')
plt.title('Energy Flow Through Jet Engine Inlet')
plt.xlabel('Stations')
plt.ylabel('Energy Flow (W)')
plt.legend()
plt.grid()
plt.show()
# the code graphs the first principle of thermodynamics, showing that energy is conserved through the inlet of the jet engine, with energy flow remaining constant from the inlet to the outlet.

# Velocity vs Static Pressure
static_temps = [T1, T2]
velocities = [V1, V2]

plt.figure()
plt.plot(static_temps, velocities, marker='o', label='Velocity vs Static Temperature')
plt.title('Velocity vs Static Temperature in Jet Engine Inlet')
plt.xlabel('Static Temperature (K)')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.grid()
plt.show()
# the code graphs the relationship between static temperature and velocity in the jet engine inlet, showing how the velocity changes with static temperature from the inlet to the outlet.





