def calculate_T04(T03, n_b, f, LHV, cp):
    """
    Calculate the stagnation temperature at the combustor exit.
    
    Parameters:
    T03 (float): Stagnation temperature at the compressor outlet (K)
    n_b (float): Combustor efficiency
    f (float): Fuel to air ratio
    LHV (float): Lower heating value of fuel (J/kg)
    cp (float): Specific heat capacity at constant pressure (J/(kg*K))
    
    Returns:
    float: Stagnation pressure at the combustor exit (Pa)
    """
    return T03 + (n_b * f * LHV) / (cp)  

def calculate_exit_enthalpy(cp, T04):
    """
    Calculate the exit enthalpy at the combustor outlet.
    
    Parameters:
    cp (float): Specific heat capacity at constant pressure (J/(kg*K))
    T04 (float): Stagnation temperature at the combustor outlet (K)
    
    Returns:
    float: Exit enthalpy at the combustor outlet (J/kg)
    """
    return cp * T04

def calculate_P04(P03, p_loss_ratio):
    """
    Calculate the stagnation pressure at the combustor exit.
    
    Parameters:
    P03 (float): Stagnation pressure at the compressor outlet (Pa)
    p_loss_ratio (float): Pressure loss ratio in the combustor
    
    Returns:
    float: Stagnation pressure at the combustor exit (Pa)
    """
    return P03 * (1 - p_loss_ratio)

def calculate_fuel_mass_flow_rate(m_dot, f):
    """
    Calculate the fuel mass flow rate.
    
    Parameters:
    m_dot (float): Mass flow rate (kg/s)
    f (float): Fuel to air ratio
    
    Returns:
    float: Fuel mass flow rate (kg/s)
    """
    return m_dot * f

def calculate_mass_flow_total(m_dot, f):
    """
    Calculate the total mass flow rate including fuel.
    
    Parameters:
    m_dot (float): Mass flow rate (kg/s)
    f (float): Fuel to air ratio
    
    Returns:
    float: Total mass flow rate (kg/s)
    """
    return m_dot * (1 + f)

def calculate_energy_flow_rate(m_total, h04):
    """
    Calculate the energy flow rate at the combustor outlet.
    
    Parameters:
    m_total (float): Total mass flow rate including fuel (kg/s)
    h04 (float): Exit enthalpy at the combustor outlet (J/kg)
    
    Returns:
    float: Energy flow rate at the combustor outlet (W)
    """
    return m_total * h04

def calculate_equivalence_ratio(f,f_stoich):
    """
    Calculate the equivalence ratio.
    
    Parameters:
    f (float): Fuel to air ratio
    f_stoich (float): Stoichiometric fuel to air ratio
    
    Returns:
    float: Equivalence ratio
    """
    return f / f_stoich

def calculate_q_added(LHV, fuel_mass_flow_rate):
    """
    Calculate the heat added in the combustor.
    
    Parameters:
    LHV (float): Lower heating value of fuel (J/kg)
    fuel_mass_flow_rate (float): Fuel mass flow rate (kg/s)
    
    Returns:
    float: Heat added in the combustor (W)
    """
    return LHV * fuel_mass_flow_rate

def calculate_temp_rise(T03, T04):
    """
    Calculate the temperature rise in the combustor.
    
    Parameters:
    T03 (float): Stagnation temperature at the compressor outlet (K)
    T04 (float): Stagnation temperature at the combustor outlet (K)
    
    Returns:
    float: Temperature rise in the combustor (K)
    """
    return T04 - T03

def calculate_enthalpy_rise(T04, T03, cp):
    """
    Calculate the enthalpy rise in the combustor.
    
    Parameters:
    T04 (float): Stagnation temperature at the combustor outlet (K)
    T03 (float): Stagnation temperature at the compressor outlet (K)
    cp (float): Specific heat capacity at constant pressure (J/(kg*K))
    
    Returns:
    float: Enthalpy rise in the combustor (J/kg)
    """
    return cp * (T04 - T03)