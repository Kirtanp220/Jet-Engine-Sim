# These are the outputs of the inlet simulation which are used in the compressor simulation.
import math

P2 = 125545.56 # Static pressure at start of compressor (Pa)
T2 = 308.32 # Static temperature at start of compressor (K)
T0_real_inlet = 314.98 # Real stagnation temperature at inlet (K)
P0_real_inlet = 136981.68 # Real stagnation pressure at inlet (Pa)
M_inlet = 0.36 # Mach number at inlet
rho_inlet = 1.14 # Density at inlet (kg/m^3)
V_inlet = 125.0 # Velocity at inlet (m/s)
h0_real_inlet = 316551.87 # Real stagnation enthalpy at inlet (J/kg)
gamma = 1.4 # Specific heat ratio for air
R = 287.05 # Specific gas constant for air (J/(kg*K))
cp = 1005.0 # Specific heat at constant pressure for air (J/(kg*K))
rp = 30 # Pressure ratio across the compressor
eta_c = 0.88 # Efficiency of the compressor
m_flow = 115.0 # Mass flow rate (kg/s)
energy_flow = 36403465.05 # Energy flow rate (W)

P01 = P0_real_inlet
T01 = T0_real_inlet



