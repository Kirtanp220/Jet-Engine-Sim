# Inlet Calcualtion- Stage 1
# Calculating stagnation pressure, temperature, enthalpy, and energy flow up until the outlet of the inlet
# This code simulates the inlet of a jet engine, calculating various thermodynamic properties
# Written by: Kirtan Patel
# Date: 2025-07-06

import math

# Input Values
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


#step 1: Calcualte ideal stagnation temperature
T0 = T1 + V1**2/ (2*cp)  # K, Stagnation Temperature

# step 2 : Calculate real stagantion temperature
T0_real = T1 + eta_i * (T0 - T1)  # K, Real Stagnation Temperature

# step 3 : Calculate real stagnation pressure
P0_real = P1 * (T0_real/ T1)**(gamma/(gamma - 1))  # Pa, Real Stagnation Pressure

#step 4 : Calculate pressure after recovery efficiency
P0_real_after_eta_p = eta_p * P0_real # Pa, Real Stagnation Pressure after applying efficiency

# step 5 : Calculate stagnation enthalpy
h0_real = cp * T0_real  # J/kg, Real Stagnation Enthalpy

# step 6 : Calculate energy flow
energy_flow = m_flow * h0_real  # W, Energy Flow 

# step 7 : Calculate new static temperature at outlet
T2 = T1 + (V1**2/ (2 * cp)) - (V2**2 / (2 * cp))  # K, Static Temperature at Outlet

#step 7.1 : Calculate Mach number at inlet and outlet
a2 = math.sqrt(gamma * R * T2)  # m/s, Speed of sound at outlet
a1 = math.sqrt(gamma * R * T1)  # m/s, Speed of sound at inlet

M2 = V2 / a2  # Mach number at outlet
M1 = V1 / a1  # Mach number at inlet

# step 7.2: Calculate densities at inlet and outlet using ideal gas law
rho2 = P1 / (R * T2)  # kg/m^3, Density at Outlet
rho1 = P1 / (R * T1)  # kg/m^3, Density at Inlet

# step 7.3: Calculate area ratio 
area_ratio = (V1/V2) * (rho2/rho1)  # Area ratio between inlet and outlet

# step 8 : Calculate ideal stagnation temperature at outlet
T0_outlet = T1 + eta_i * (T0_real - T1)  # K, Ideal Stagnation Temperature at Outlet

# step 9 : Calculate ideal stagnation pressure at outlet
P0_outlet = P1 * (T0_outlet / T1)**(gamma / (gamma - 1))  # Pa, Ideal Stagnation Pressure at Outlet

# step 10 : Calculate static pressure at outlet
P2 = P0_outlet * (T2 / T0_outlet)**(gamma / (gamma - 1))  # Pa, Static Pressure at Outlet

# step 11: Real stagnation pressure at outlet after applying efficiency
P0_real_station1 = P0_real #renaming for clarity
P0_real_station_2 = eta_p * P0_real_station1  # Pa, Real Stagnation Pressure at Outlet after applying efficiency

# step 12: In an adiabatic duct, the real stagnation temperature does not change
T0_real_outlet = T0_real  # K, Real Stagnation Temperature at Outlet (remains the same)

# step 13: Calculate real stagnation enthalpy at outlet
h0_real_outlet = cp * T0_real_outlet  # J/kg, Real

# step 14: Calculate energy flow at outlet
energy_flow_outlet = m_flow * h0_real_outlet  # W, Energy Flow at Outlet

# Irreversible vs Reversible Inlet Processes
# Isentropic Processes involve ideal conditions meaning a reversible process with no entropy change.
# In a real inlet, the proccess is non isentropic, meaning there is an increase in entropy due to irreversibilities such as friction and shock waves. 

# Real stagnation pressure at outlet
P0_actual_outlet = P0_real_station_2  # Pa, Real Stagnation Pressure at Outlet

# Ideal stagnation pressure at outlet
P0_ideal_outlet = P0_outlet  # Pa, Ideal Stagnation Pressure at Outlet

# Pressure loss Calculation
pressure_lost = (P0_ideal_outlet - P0_actual_outlet) / P0_ideal_outlet * 100  # Percentage of pressure lost due to inefficiencies

#Comparing code with assumed baseline values based on standard subsonic inlet conditions
#Since data was not accesible for comparison, we will use assumed values for static pressure, temperature, and stagnation pressure at the inlet and outlet.

import numpy as np
import matplotlib.pyplot as plt

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
plt.bar(x + bar_width/2, [P0_ideal_outlet, P0_real_station_2], width=bar_width, label='Calculated Stagnation Pressure', color='orange')
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

print(f"Real Stagnation Pressure at Outlet (P0_real_station_2): {P0_real_station_2:.2f} Pa")
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

import matplotlib.pyplot as plt

# Define Station Numbers
stations = [ 'Inlet', 'Outlet']
# Define Pressure Values
real_stag_pressure = [P0_real_after_eta_p, P0_real_station_2]
ideal_stag_pressure = [P1 * (T0 / T1)**(gamma / (gamma - 1)), P0_outlet]
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
real_stag_pressure_loss =[P0_real,P0_real_station_2]
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