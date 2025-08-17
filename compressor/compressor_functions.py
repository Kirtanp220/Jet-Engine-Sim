def calculate_stag_pressure_2(P01, rp):
    """
    Calculate the stagnation pressure at the compressor exit.
    
    Parameters:
    P01 (float): Stagnation pressure at the inlet (Pa)
    rp (float): Pressure ratio across the compressor
    
    Returns:
    float: Stagnation pressure at the compressor exit (Pa)
    """
    return P01 * rp

def calculate_stag_temperature_2(T01, eta_c, gamma, P02, P01):
    """
    Calculate the stagnation temperature at the compressor exit.
    
    Parameters:
    T01 (float): Stagnation temperature at the inlet (K)
    eta_c (float): Efficiency of the compressor
    gamma (float): Specific heat ratio for air
    P02 (float): Stagnation pressure at the compressor exit (Pa)
    P01 (float): Stagnation pressure at the inlet (Pa)
    
    Returns:
    float: Stagnation temperature at the compressor exit (K)
    """
    return T01 + T01/eta_c * ((P02 / P01) ** ((gamma - 1) / gamma) - 1)

def calculate_stag_enthalpy_2(T02, cp):
    """
    Calculate the stagnation enthalpy at the compressor exit.
    
    Parameters:
    T02 (float): Stagnation temperature at the compressor exit (K)
    cp (float): Specific heat at constant pressure for air (J/(kg*K))
    
    Returns:
    float: Stagnation enthalpy at the compressor exit (J/kg)
    """
    return cp * T02

def energy_flow_2(h0_2, m_flow):
    """
    Calculate the energy flow through the compressor.
    
    Parameters:
    h0_2 (float): Stagnation enthalpy at the compressor exit (J/kg)
    m_flow (float): Mass flow rate (kg/s)
    
    Returns:
    float: Energy flow through the compressor (W)
    """
    return h0_2 * m_flow



