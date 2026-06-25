Orbital Velocity Calculator
===========================

A Python script that calculates and displays circular orbital
velocity and period for Earth orbits using the vis-viva equation:

    v = sqrt( G * M / r )

Where:
    G = gravitational constant (6.674e-11 m³/kg/s²)
    M = Earth mass (5.972e24 kg)
    r = distance from Earth center (radius + altitude)

Results
-------
Computes orbital velocity (km/s) and period (hours) for
three key orbit regimes:

    ISS  / LEO  —  408 km   —  ~7.7 km/s  —  ~1.5 hrs
    GPS  / MEO  — 20,200 km —  ~3.9 km/s  —  ~12 hrs
    GEO        — 35,786 km  —  ~3.1 km/s  —  ~24 hrs

Key insight: as altitude increases, velocity decreases but
orbital period increases. At GEO, the 24-hour period matches
Earth's rotation — which is why satellites there appear
stationary above one spot on Earth.

Tools used
----------
    Python 3
    NumPy  — vectorized math across 1000 altitude points
    Matplotlib — plot generation (saved as PNG in WSL)

Author: Rhys Owens
Course: Aerospace Engineering
