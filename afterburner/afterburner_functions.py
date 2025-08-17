def calculate_f_ab(cp_ab, T06, T05, LHV):
    """
    Calculate the fuel-to-air ratio in the afterburner.

    Parameters:
    cp_ab (float): Specific heat at constant pressure for afterburner (J/kgK)
    T06 (float): Temperature at turbine exit (K)
    T05 (float): Temperature at turbine inlet (K)
    LHV (float): Lower heating value of the fuel (J/kg)

    Returns:
    float: Fuel-to-air ratio in the afterburner
    """
    return cp_ab *(T06 - T05) / (LHV - cp_ab * T06)

def calculate_ab_fuel_mass_flow(f_ab, m_total):
    """
    Calculate the fuel mass flow rate in the afterburner.

    Parameters:
    f_ab (float): Fuel-to-air ratio in the afterburner
    m_total (float): Total mass flow rate through the engine (kg/s)

    Returns:
    float: Fuel mass flow rate in the afterburner (kg/s)
    """
    return f_ab * m_total

def calculate_m_flow_new(m_total, ab_fuel_mass_flow):
    """
    Calculate the new total mass flow rate after the afterburner.

    Parameters:
    m_total (float): Total mass flow rate through the engine before afterburner (kg/s)
    ab_fuel_mass_flow (float): Fuel mass flow rate in the afterburner (kg/s)

    Returns:
    float: New total mass flow rate after the afterburner (kg/s)
    """
    return m_total + ab_fuel_mass_flow

def calculate_h06(cp_ab, T06):
    """
    Calculate the specific enthalpy at the afterburner exit.

    Parameters:
    cp_ab (float): Specific heat at constant pressure for afterburner (J/kgK)
    T06 (float): Temperature at turbine exit (K)

    Returns:
    float: Specific enthalpy at the afterburner exit (J/kg)
    """
    return cp_ab * T06

def calculate_energy_flow_ab(m_flow_new, h06):
    """
    Calculate the energy flow at the afterburner exit.

    Parameters:
    m_flow_new (float): New total mass flow rate after the afterburner (kg/s)
    h06 (float): Specific enthalpy at the afterburner exit (J/kg)

    Returns:
    float: Energy flow at the afterburner exit (W)
    """
    return m_flow_new * h06

def calculate_P06(P05, loss_fraction=0.05):
    """
    Calculate the pressure at the afterburner exit.

    Parameters:
    P05 (float): Pressure at turbine inlet (Pa)
    loss_fraction (float): Fraction of pressure loss in the afterburner

    Returns:
    float: Pressure at the afterburner exit (Pa)
    """
    return P05 * (1 - loss_fraction)