# Jet-Engine-Sim
Inspired by the F100 PW-229 Pratt and Whitney Engine, a Python-based engine simulator that models core thermodynamics and fluid processes , implementing stage-by-stage calculations using fundamental physics-- from inlet to nozzle.

The simulation models subsonic flow internally, with a supersonic exhaust (CD nozzle)-- wet flow. Assuming isentropic conditions through all stages execpt for the combustion stage; while still calculating for real-world losses (using efficiency values and ratios). Though this model does not recreate precise "real-life" scenarios, but instead is meant to be an educational foundation for learning fundamental concepts.

ASSUMPTIONS-
- Flow- subsonic(internal), supersonic output
- Model Type- Isentropic (except for combustor)
- Output Flow- Wet with afterburner
- Losses- Modelled via efficiences (mechanical, isentropic, etc.)
- Mach at nozzle exit(Assumption)- 2.0
- Temp at afterburner exit(Assumption)- 2400K

FINAL OUTPUTS-
- Exit Temperature: 1440.06 K
- Exit Pressure: 34023.35 Pa
- Exit Density: 0.08 kg/m^3
- Exit Velocity: 1484.78 m/s
- Nozzle Exit Area: 1.00 m^2
- Thrust: 114381.80 N

LICENSE/USAGE-
This code is intended for educational purposes only, and is not suitable for commercial and proffesional usage.

Author: Kirtan Patel
Jet Engine Simulation Project (2025)
