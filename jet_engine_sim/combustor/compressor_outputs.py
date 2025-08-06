# these are the outputs measured at the end of the compressor and inputs to the combustor

import math

P03 = 4109450.40  # Pa, Stagnation Pressure at Compressor Outlet
T03 = 902.93  # K, Stagnation Temperature at Compressor Outlet
H03 = 907440.43  # J/kg, Stagnation Enthalpy at Compressor Outlet
m_dot = 115.0  # kg/s, Mass Flow Rate
f = 0.02 # Fuel to Air Ratio
n_b = 0.98 # Combustor Efficiency
LHV = 43000000.0  # J/kg, Lower Heating Value of Jet-A Fuel
cp = 1150.0  # J/(kg*K), Specific Heat Capacity at Constant Pressure
f_stoich = 0.067  # Stoichiometric Fuel to Air Ratio for Jet-A
p_loss_ratio = 0.06  # Pressure Loss Ratio in Combustor