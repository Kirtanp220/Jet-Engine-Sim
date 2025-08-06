# outputs of the turbine and inputs to the afterburner

import math

T05 = 862.19  # K
P05 = 276341.17  # Pa
h05 = 991522.52  # J/kg
cp_ab = 1150  # J/kgK
gamma_ab = 1.333
T06 = 2400  # K
LHV = 43e6  # J/kg
m_total = 117.3  # kg/s
n_ab = 0.95 # afterburner efficiency
exit_energy_flow =  116305591.26 # W, from turbine outputs