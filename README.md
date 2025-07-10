Jet Engine Inlet to Outlet Simulator
------------------------------------

This project simulates how air flows from ambient conditions through the inlet diffuser to the outlet. It analyzes how air compresses through the system and demonstrates the First Law of Thermodynamics. The simulation tracks both ideal and real values of temperature, pressure, enthalpy, Mach number, and energy flow from the inlet to the outlet.

This inlet simulation is a vital component of a larger project aimed at building a complete jet engine simulator. The code is designed to be clean, first-principle-based, and physically accurate, helping to convey the core physics behind complex propulsion systems.
Calculations Included:
- Static and stagnation pressure
- Static and stagnation temperature
- Energy flow and enthalpy
- Mach numbers at inlet and outlet
- Area ratio and air density

Graphs Generated:
- Real vs ideal stagnation values
- Pressure and temperature transformations (inlet to outlet)
- Velocity vs static temperature
- Energy conservation through the inlet (inlet to outlet)

Assumptions (Physics):
- Ideal gas model for air
- No heat transfer (adiabatic duct)
- Steady-state flow conditions
- Isentropic flow for ideal cases
- Real-world losses modeled through inlet efficiency and pressure recovery efficiency
