# Outputs from the afterburner and input to the nozzle

import math

M_e = 2.0 # Exit Mach number
P0 = 262524.11 # Total pressure in Pa
T0 = 2400 # Total temperature in K
m_dot = 122.4551 # Mass flow rate in kg/s af afterburner
gamma = 1.3333 # Specific heat ratio
R= 287.05 # Specific gas constant in J/(kg*K)
P_ambient = 101325 # Ambient pressure in Pa
u0 = 0 # Initial velocity in m/s
m_total= 117.3 # Total mass in kg