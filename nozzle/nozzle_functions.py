import math

def calculate_area_ratio(M_e, gamma):
    """
    Calculate the area ratio for the nozzle based on exit Mach number and specific heat ratio.
    
    Parameters:
    M_e (float): Exit Mach number
    gamma (float): Specific heat ratio
    
    Returns:
    float: Area ratio
    """
    return (1 / M_e) * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M_e**2))**((gamma + 1) / (2 * (gamma - 1)))

def calculate_T_exit(T0, M_e, gamma):
    """
    Calculate the exit temperature of the nozzle.
    
    Parameters:
    T0 (float): Total temperature in K
    M_e (float): Exit Mach number
    gamma (float): Specific heat ratio
    
    Returns:
    float: Exit temperature in K
    """
    return T0 / (1 + ((gamma - 1) / 2) * M_e**2)

def calculate_P_exit(P0, M_e, gamma):
    """
    Calculate the exit pressure of the nozzle.
    
    Parameters:
    P0 (float): Total pressure in Pa
    M_e (float): Exit Mach number
    gamma (float): Specific heat ratio
    
    Returns:
    float: Exit pressure in Pa
    """
    return P0 / ((1 + ((gamma - 1) / 2) * M_e**2)**(gamma / (gamma - 1)))

def calculate_density_exit(P_exit, T_exit, R):
    """
    Calculate the exit density of the nozzle.
    
    Parameters:
    P_exit (float): Exit pressure in Pa
    T_exit (float): Exit temperature in K
    R (float): Specific gas constant in J/(kg*K)
    
    Returns:
    float: Exit density in kg/m^3
    """
    return P_exit / (R * T_exit)

def calculate_velocity_exit(M_e, gamma, R, T_exit):
    """
    Calculate the exit velocity of the nozzle.
    
    Parameters:
    M_e (float): Exit Mach number
    gamma (float): Specific heat ratio
    R (float): Specific gas constant in J/(kg*K)
    T_exit (float): Exit temperature in K
    
    Returns:
    float: Exit velocity in m/s
    """
    return M_e * math.sqrt(gamma * R * T_exit)

def calculate_nozzle_exit_area(m_dot, density_exit, velocity_exit):
    """
    Calculate the exit area of the nozzle.
    
    Parameters:
    m_dot (float): Mass flow rate in kg/s
    density_exit (float): Exit density in kg/m^3
    velocity_exit (float): Exit velocity in m/s
    
    Returns:
    float: Exit area in m^2
    """
    return m_dot / (density_exit * velocity_exit)

def calculate_thrust(m_dot, m_total, u0, velocity_exit, P_exit, P_ambient, nozzle_exit_area):
    """
    Calculate the thrust produced by the nozzle.
    
    Parameters:
    m_dot (float): Mass flow rate in kg/s
    m_total (float): Total mass in kg
    u0 (float): Initial velocity in m/s
    velocity_exit (float): Exit velocity in m/s
    P_exit (float): Exit pressure in Pa
    P_ambient (float): Ambient pressure in Pa
    nozzle_exit_area (float): Exit area of the nozzle in m^2
    
    Returns:
    float: Thrust in N
    """
    momentum_thrust = m_dot * velocity_exit - m_total * u0
    pressure_thrust = (P_exit - P_ambient) * nozzle_exit_area
    
    return momentum_thrust + pressure_thrust
