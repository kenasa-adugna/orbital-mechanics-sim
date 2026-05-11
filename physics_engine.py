import numpy as np

G = 6.67430e-11 
M_EARTH = 5.972e24 
R_EARTH = 6.371e6   

def calculate_gravity(pos):
    
    distance = np.linalg.norm(pos)
    if distance < R_EARTH:
        return np.array([0, 0])  
    
    accel_mag = -G * M_EARTH / distance**3
    return accel_mag * pos

def update_state(state, dt):
   
    pos = state[:2]
    vel = state[2:]
    
    accel = calculate_gravity(pos)
    vel = vel + accel * dt
    pos = pos + vel * dt
    
    return np.array([pos[0], pos[1], vel[0], vel[1]])
