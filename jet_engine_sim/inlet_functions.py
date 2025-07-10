import math


def calculate_ideal_stagnation_temperature(T1, V1, cp):
    """
    Calculate the ideal stagnation temperature.
    
    Parameters:
    T1 (float): Static temperature in Kelvin.
    V1 (float): Static velocity in m/s.
    cp (float): Specific heat capacity at constant pressure in J/(kg*K).
    
    Returns:
    float: Ideal stagnation temperature in Kelvin.
    """
    return T1 + (V1**2) / (2 * cp)

def calculate_real_stagnation_temperature(T1, eta_i, T0):
    """
    Calculate the real stagnation temperature considering efficiency.
    
    Parameters:
    T1 (float): Static temperature in Kelvin.
    eta_i (float): Efficiency of the inlet.
    T0 (float): Ideal stagnation temperature in Kelvin.
    
    Returns:
    float: Real stagnation temperature in Kelvin.
    """
    return T1 + eta_i * (T0 - T1)

def calculate_real_stagnation_pressure(P1, T0_real, T1, gamma):
    """
    Calculate the real stagnation pressure.
    
    Parameters:
    P1 (float): Static pressure in Pa.
    T0_real (float): Real stagnation temperature in Kelvin.
    T1 (float): Static temperature in Kelvin.
    gamma (float): Ratio of specific heats (Cp/Cv).
    
    Returns:
    float: Real stagnation pressure in Pa.
    """
    return P1 * (T0_real / T1) ** (gamma / (gamma - 1))

def calculate_real_stagnation_pressure_after_eta_p(eta_p, P0_real):
    """
    Calculate the real stagnation pressure after applying pressure recovery efficiency.
    
    Parameters:
    eta_p (float): Pressure recovery efficiency.
    P0_real (float): Real stagnation pressure in Pa.
    
    Returns:
    float: Real stagnation pressure after applying efficiency in Pa.
    """
    return eta_p * P0_real

def calculate_stagnation_enthalpy(T0_real, cp):
    """
    Calculate the stagnation enthalpy.
    
    Parameters:
    T0_real (float): Real stagnation temperature in Kelvin.
    cp (float): Specific heat capacity at constant pressure in J/(kg*K).
    
    Returns:
    float: Stagnation enthalpy in J/kg.
    """
    return cp * T0_real

def calculate_energy_flow(m_flow, h0_real):
    """
    Calculate the energy flow.
    
    Parameters:
    m_flow (float): Mass flow rate in kg/s.
    h0_real (float): Real stagnation enthalpy in J/kg.
    
    Returns:
    float: Energy flow in Watts.
    """
    return m_flow * h0_real

def calculate_new_static_temperature_at_outlet(T1, V1, V2, cp):
    """
    Calculate the new static temperature at the outlet.
    
    Parameters:
    T1 (float): Static temperature at inlet in Kelvin.
    V1 (float): Static velocity at inlet in m/s.
    V2 (float): Static velocity at outlet in m/s.
    cp (float): Specific heat capacity at constant pressure in J/(kg*K).
    
    Returns:
    float: New static temperature at outlet in Kelvin.
    """
    return T1 + ((V1**2 - V2**2) / (2 * cp))

def calculate_mach_number(T1, T2, V1, V2, R, gamma, a1, a2):
    """
    Calculate the Mach number at the inlet and outlet.
    
    Parameters:
    T1 (float): Static temperature at inlet in Kelvin.
    T2 (float): Static temperature at outlet in Kelvin.
    V1 (float): Static velocity at inlet in m/s.
    V2 (float): Static velocity at outlet in m/s.
    R (float): Specific gas constant in J/(kg*K).
    gamma (float): Ratio of specific heats (Cp/Cv).
    a1 (float): Speed of sound at inlet in m/s.
    a2 (float): Speed of sound at outlet in m/s.
    
    Returns:
    tuple: Mach number at inlet and outlet.
    """
    a2 = math.sqrt(gamma * R * T2)  # m/s, Speed of sound at outlet
    a1 = math.sqrt(gamma * R * T1)  # m/s, Speed of sound at inlet 
    M1 = V1 / a1
    M2 = V2 / a2
    if M1 < 0 or M2 < 0:
        raise ValueError("Mach number cannot be negative. Check input values.")
    return M1, M2

def calculate_densities_at_inlet_outlet(P1, T1, T2, R):
    """
    Calculate the densities at the inlet and outlet.
    
    Parameters:
    P1 (float): Static pressure at inlet in Pa.
    T1 (float): Static temperature at inlet in Kelvin.
    T2 (float): Static temperature at outlet in Kelvin.
    R (float): Specific gas constant in J/(kg*K).
    
    Returns:
    tuple: Density at inlet and outlet in kg/m^3.
    """
    rho1 = P1 / (R * T1)  # kg/m^3, Density at inlet
    rho2 = P1 / (R * T2)  # kg/m^3, Density at outlet
    return rho1, rho2

def calculate_area_ratio(V1, V2, rho1, rho2):
    """
    Calculate the area ratio at the inlet and outlet.
    
    Parameters:
    V1 (float): Static velocity at inlet in m/s.
    V2 (float): Static velocity at outlet in m/s.
    rho1 (float): Density at inlet in kg/m^3.
    rho2 (float): Density at outlet in kg/m^3.
    
    Returns:
    float: Area ratio.
    """
    return (V1/V2) * (rho2/rho1)

def calculate_ideal_stagnation_temperature_at_outlet(T1, eta_i, T0_real):
    """
    Calculate the ideal stagnation temperature at the outlet.
    
    Parameters:
    T1 (float): Static temperature at inlet in Kelvin.
    eta_i (float): Efficiency of the inlet.
    T0_real (float): Real stagnation temperature in Kelvin.
    
    Returns:
    float: Ideal stagnation temperature at outlet in Kelvin.
    """
    return T1 + eta_i * (T0_real - T1)

def calculate_ideal_stagnation_pressure_at_outlet(P1, T1, T0_outlet, gamma):
    """
    Calculate the ideal stagnation pressure at the outlet.
    
    Parameters:
    P1 (float): Static pressure at inlet in Pa.
    T1 (float): Static temperature at inlet in Kelvin.
    T0_outlet (float): Ideal stagnation temperature at outlet in Kelvin.
    gamma (float): Ratio of specific heats (Cp/Cv).
    
    Returns:
    float: Ideal stagnation pressure at outlet in Pa.
    """
    return P1 * (T0_outlet / T1) ** (gamma / (gamma - 1))

def calculate_static_pressure_at_outlet(P0_outlet, T2, T0_outlet, gamma):
    """
    Calculate the static pressure at the outlet.
    
    Parameters:
    P0_outlet (float): Ideal stagnation pressure at outlet in Pa.
    T2 (float): Static temperature at outlet in Kelvin.
    T0_outlet (float): Ideal stagnation temperature at outlet in Kelvin.
    gamma (float): Ratio of specific heats (Cp/Cv).
    
    Returns:
    float: Static pressure at outlet in Pa.
    """
    return P0_outlet * (T2 / T0_outlet) ** (gamma / (gamma - 1))


def calculate_real_stagnation_enthalpy_at_outlet(T0_real_outlet, cp):
    """
    Calculate the real stagnation enthalpy at the outlet.
    
    Parameters:
    T0_real_outlet (float): Real stagnation temperature at outlet in Kelvin.
    cp (float): Specific heat capacity at constant pressure in J/(kg*K).
    
    Returns:
    float: Real stagnation enthalpy at outlet in J/kg.
    """
    return cp * T0_real_outlet

def calculate_energy_flow(m_flow, h0_real_outlet):
    """
    Calculate the energy flow at the outlet.
    
    Parameters:
    m_flow (float): Mass flow rate in kg/s.
    h0_real_outlet (float): Real stagnation enthalpy at outlet in J/kg.
    
    Returns:
    float: Energy flow at outlet in Watts.
    """
    return m_flow * h0_real_outlet


def calculate_pressure_lost(P0_ideal_outlet, P0_actual_outlet):
    """
    Calculate the pressure lost.
    
    Parameters:
    P0_ideal_outlet (float): Ideal stagnation pressure at outlet in Pa.
    P0_actual_outlet (float): Actual stagnation pressure at outlet in Pa.
    
    Returns:
    float: Pressure lost in Pa.
    """
    return (P0_ideal_outlet - P0_actual_outlet) / P0_ideal_outlet * 100

