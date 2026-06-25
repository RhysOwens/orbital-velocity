# orbital_velocity.py
import numpy as np
import matplotlib.pyplot as plt
# constants
G = 6.674e-11  # gravitational constant, m³/kg/s²
M = 5.972e24  # Earth mass, kg
R_earth = 6.371e6  # Earth radius, m
# altitude range: 200 km to 40,000 km
altitudes_km = np.linspace(200, 40000, 1000)
r = R_earth + altitudes_km * 1000  # convert to meters
# orbital velocity equation: v = sqrt(G*M/r)
v = np.sqrt(G * M / r) / 1000  # convert m/s to km/s
# orbital period in hours: T = 2*pi*r / v
T = (2 * np.pi * r) / (v * 1000) / 3600
# mark key orbits
key = {
'ISS (408 km)':  408,
'GPS (20,200 km)': 20200,
'GEO (35,786 km)': 35786,
}
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
# plot 1: velocity vs altitude
ax1.plot(altitudes_km, v, color='steelblue', linewidth=2)
for label, alt in key.items():
	r_k = R_earth + alt * 1000
	v_k = np.sqrt(G * M / r_k) / 1000
ax1.plot(alt, v_k, 'ro', markersize=7)
ax1.annotate(label, (alt, v_k), textcoords="offset points",
xytext=(8, 4), fontsize=8)
ax1.set_xlabel('Altitude (km)')
ax1.set_ylabel('Orbital velocity (km/s)')
ax1.set_title('Orbital velocity vs altitude')
ax1.grid(True, alpha=0.3)
# plot 2: orbital period vs altitude
ax2.plot(altitudes_km, T, color='darkorange', linewidth=2)
for label, alt in key.items():
	r_k = R_earth + alt * 1000
	v_k = np.sqrt(G * M / r_k)
	T_k = (2 * np.pi * r_k) / v_k / 3600
ax2.plot(alt, T_k, 'ro', markersize=7)
ax2.annotate(label, (alt, T_k), textcoords="offset points",
xytext=(8, 4), fontsize=8)
ax2.axhline(y=24, color='green', linestyle='--', alpha=0.5, label='24 hr (GEO)')
ax2.set_xlabel('Altitude (km)')
ax2.set_ylabel('Orbital period (hours)')
ax2.set_title('Orbital period vs altitude')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
# print a summary table
print(f"\n{'Orbit':<20} {'Alt (km)':>10} {'Vel (km/s)':>12} {'Period (hr)':>12}")
print("-" * 56)
for label, alt in key.items():
	r_k = R_earth + alt * 1000
	v_k = np.sqrt(G * M / r_k) / 1000
	T_k = (2 * np.pi * r_k) / (v_k * 1000) / 3600
print(f"{label:<20} {alt:>10,} {v_k:>12.2f} {T_k:>12.2f}")
