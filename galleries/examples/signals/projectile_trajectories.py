"""
==========================================
Projectile Trajectories at Multiple Angles
==========================================

This example shows ideal projectile motion for six launch angles with
the same initial speed under constant gravitational acceleration. It
illustrates the tradeoff between maximum height and horizontal range.
"""

import matplotlib.pyplot as plt
import numpy as np

g = 9.81
v0 = 30.0
angles_deg = np.array([15, 25, 35, 45, 55, 65], dtype=float)

fig, ax = plt.subplots(figsize=(8, 5))

for angle_deg in angles_deg:
    theta = np.deg2rad(angle_deg)
    flight_range = (v0**2 * np.sin(2 * theta)) / g
    x = np.linspace(0, flight_range, 300)
    y = x * np.tan(theta) - (g * x**2) / (2 * v0**2 * np.cos(theta) ** 2)
    ax.plot(x, y, linewidth=1.5, label=f"{angle_deg:.0f}°")

ax.set_xlabel("Horizontal distance (m)")
ax.set_ylabel("Height (m)")
ax.set_title("Projectile trajectories for equal launch speed")
ax.set_aspect("equal", adjustable="box")
ax.legend(title="Launch angle", loc="upper right")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules
#    is shown in this example:
#
#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`
#    - `matplotlib.axes.Axes.set_aspect`
#    - `matplotlib.axes.Axes.legend` / `matplotlib.pyplot.legend`
#    - `matplotlib.pyplot.subplots`
#
# .. tags::
#
#    plot-type: line
#    level: beginner
