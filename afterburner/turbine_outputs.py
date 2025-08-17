# outputs of the turbine and inputs to the afterburner

import math

T05 = 877.67  # K
P05 = 297559.99  # Pa
h05 = 1009315.47  # J/kg
cp_ab = 1150  # J/kgK
gamma_ab = 1.333
T06 = 2400  # K
LHV = 43e6  # J/kg
m_total = 117.3  # kg/s
n_ab = 0.95 # afterburner efficiency
exit_energy_flow =   118392704.25 # W, from turbine outputs