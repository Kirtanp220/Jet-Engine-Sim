import math
import numpy as np
import matplotlib.pyplot as plt

from nozzle_functions import *
from afterburner_outputs import *


area_ratio= calculate_area_ratio(M_e, gamma)
T_exit= calculate_T_exit(T0, M_e, gamma)
P_exit= calculate_P_exit(P0, M_e, gamma)
density_exit= calculate_density_exit(P_exit, T_exit, R)
v_exit= calculate_velocity_exit(M_e, gamma, R, T_exit)
nozzle_exit_area= calculate_nozzle_exit_area(m_dot, density_exit, v_exit)
thrust= calculate_thrust(m_dot, m_total, u0, v_exit, P_exit, P_ambient, nozzle_exit_area)


print(f"Area Ratio: {area_ratio:.2f}")
print(f"Exit Temperature: {T_exit:.2f} K")
print(f"Exit Pressure: {P_exit:.2f} Pa")
print(f"Exit Density: {density_exit:.2f} kg/m^3")
print(f"Exit Velocity: {v_exit:.2f} m/s")
print(f"Nozzle Exit Area: {nozzle_exit_area:.2f} m^2")
print(f"Thrust: {thrust:.2f} N")


# We will now simulate a visual representation of a CD nozzle, which will include area profile, pressure vs position, temp vs position, and mach # vs position.

# X axis: nozzle length
x = np.linspace(0, 1, 500)

def nozzle_shape(x):
    return 1 - 0.8 * np.exp(-((x-0.5)/0.15)**2)

y= nozzle_shape(x)

mach = np.piecewise(x, [x < 0.5, x == 0.5, x > 0.5],
                    [lambda x: 0.3 + 1.4 * x, 1.0, lambda x: 1 +2.5 *(x-0.5)])
temperature= 1.2 - 0.5 *x
pressure= 1.1-0.6 * x**1.2

#plotting

fig, ax1 = plt.subplots(figsize=(10, 6))

# nozzle shape
ax1.plot(x, y, color='blue', linewidth=2)
ax1.plot(x, -y, color= 'blue', linewidth=2)
ax1.fill_between(x, y, -y, color='lightblue', alpha=0.5)
ax1.set_ylabel('Nozzle Radius (arb. units)')
ax1.set_xlabel('Nozzle Length (arb. units)')
ax1.set_title('CD Nozzle Shape and Flow Properties')
ax1.set_ylim([-1.2, 1.2])
ax1.set_xlim([0, 1])

# Twin y-axis for flow properties
ax2 = ax1.twinx()
ax2.plot(x, mach, label='Mach Number (↑)', color='red', linewidth=2)
ax2.plot(x, pressure, label='Pressure (↓)', color='green', linestyle='--', linewidth=2 )
ax2.plot(x, temperature, label='Temperature (↓)', color='orange', linestyle=':', linewidth=2)
ax2.set_ylabel('Flow Properties (qualitative scale)')
ax2.legend(loc='upper right')

# Annotations

ax1.text(0.1, 1.05, 'Converging Section', fontsize=10, ha='center', color='blue')
ax1.text(0.5, 1.05, 'Throat (M=1)', fontsize=10, ha='center', color='blue')
ax1.text(0.85, 1.05, 'Diverging Section', fontsize=10, ha='center', color='blue')

plt.tight_layout()
plt.show()

