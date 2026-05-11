import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from physics_engine import update_state, R_EARTH

# --- Initial Setup ---
altitude = 400000  # 400km (ISS altitude)
r_0 = R_EARTH + altitude
v_0 = np.sqrt((6.67430e-11 * 5.972e24) / r_0) # Circular velocity

# Initial State: [x, y, vx, vy]
state = np.array([r_0, 0.0, 0.0, v_0])
dt = 20  # Seconds per frame
x_data, y_data = [], []

# --- Visualization ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
limit = r_0 * 1.5
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)

earth = plt.Circle((0, 0), R_EARTH, color='#1f77b4', label='Earth')
ax.add_artist(earth)
line, = ax.plot([], [], 'white', lw=1, label='Orbit Path')
dot, = ax.plot([], [], 'ro', markersize=5, label='Satellite')

def animate(i):
    global state
    state = update_state(state, dt)
    x_data.append(state[0])
    y_data.append(state[1])
    
    line.set_data(x_data, y_data)
    dot.set_data([state[0]], [state[1]])
    return line, dot

ani = FuncAnimation(fig, animate, frames=200, interval=20, blit=True)
plt.legend(loc='upper right')
plt.title("Satellite Orbital Dynamics Simulation")
plt.show()
