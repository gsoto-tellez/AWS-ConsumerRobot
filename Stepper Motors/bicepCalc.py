import math

# Sprocket Characteristics
N1 = 10  # Teeth for sprocket 1
N2 = 23  # Teeth for sprocket 2
p = 0.25  # Pitch for roller chain & sprockets
sprocket_gear_ratio = N2/N1 #gear ratio of sprockets

# Motor characteristics for Nema 17
step_angle = 1.8
micro_step = 200 #microstepping
steps_per_rev = 360/step_angle*micro_step/(360/step_angle) #steps for mtor
gearbox_ratio = 26.85
effective_steps = gearbox_ratio * steps_per_rev #steps on motor after gearhead on driver

# Define your variables
theta_m = 75  # desired movement in degrees
t_m = 20 #total move time in seconds 
alpha_ratio = 5 #ratio for angular accel/decel. time compared to angular const. speed time

def sprocket_geometry(N, p):
    """Calculate sprocket geometry: diameter and circumference."""
    D = round(p / (math.sin(math.pi / N)), 3)  # Diameter pitch for sprocket
    C = round(math.pi * D, 3)  # Circumference for sprocket
    return D, C

def steps_for_driver_rev(effective_steps):
    """Calculate the steps for one revolution of the bicep."""
    steps_driver_rev = math.ceil(effective_steps) #only at driver #math.ceil=rounding to nearest integer
    return steps_driver_rev

def motion_profile_setup(theta_m, t_m, alpha_ratio):
    """Set up motion profile parameters."""
    alpha_dist = theta_m / alpha_ratio
    omega_dist = theta_m - 2 * alpha_dist
    alpha_time = alpha_dist / theta_m * t_m
    omega_time = t_m - 2 * alpha_time
    max_omega = theta_m / (t_m - alpha_time)
    alpha = 2 * alpha_dist / alpha_time ** 2
    return alpha_time, alpha_dist, alpha, omega_time, omega_dist, max_omega

def convert_to_radians(theta_m, alpha_dist, alpha, omega_dist, max_omega):
    theta_m_rad = round(math.radians(theta_m), 3)  # Convert arm movement (theta_m in degrees) to radians for calculation
    alpha_dist_rad = round(math.radians(alpha_dist), 3)
    alpha_rad = round(math.radians(alpha), 3)
    omega_dist_rad = round(math.radians(omega_dist), 3)
    max_omega_rad = round(math.radians(max_omega), 2)
    return theta_m_rad, alpha_dist_rad, alpha_rad, omega_dist_rad, max_omega_rad

def steps_for_bicep_rev(C2, C1, steps_driver_rev, sprocket_gear_ratio):
    """Calculate the steps for one revolution of the bicep."""
    sprockets_rev_ratio = C2/C1 #driven sprocket compared to driver sprocket
    steps_bicep_rev = math.ceil((steps_driver_rev*sprocket_gear_ratio)*sprockets_rev_ratio)
    return steps_bicep_rev

def calculate_steps(theta_m_rad, D2, C2, steps_bicep_rev):
    """Calculate steps based on sprocket and motor relationship for the driven sprocket."""
    # Calculate linear movement for the driven sprocket based on arm angle (theta_m)
    x_m = theta_m_rad * D2 / 2
    # Calculate fraction of driven sprocket revolution based on linear movement
    fraction_rev_driven = x_m / C2
    # Calculate total steps for the motor (driver) to achieve this fraction of revolution in the driven
    total_motion_steps = math.ceil(steps_bicep_rev * fraction_rev_driven)
    return total_motion_steps

def steps_motion_profile(total_motion_steps, alpha_dist_rad, omega_dist_rad, theta_m_rad):
    alpha_steps = math.ceil(alpha_dist_rad/theta_m_rad *total_motion_steps)
    const_omega_steps = math.ceil(omega_dist_rad/theta_m_rad*total_motion_steps)
    return alpha_steps, const_omega_steps

def calculate_time_delays(alpha_time, omega_time, alpha_steps, const_omega_steps):
    """Calculate time delays for acceleration and constant speed in microseconds."""
    delay_alpha = math.ceil((alpha_time * 1e6) / alpha_steps)
    delay_omega = math.ceil((omega_time * 1e6) / const_omega_steps)
    total_delay_time = 2 * delay_alpha + delay_omega
    return delay_alpha, delay_omega, total_delay_time

def time_steps(delay_alpha, alpha_steps, delay_omega, const_omega_steps):
    alpha_steps_time = round(delay_alpha * alpha_steps/(1e6), 0)
    const_omega_steps_time = round(delay_omega * const_omega_steps/(1e6), 0)
    total_time = round(2*alpha_steps_time+const_omega_steps_time, 0)
    return alpha_steps_time, const_omega_steps_time, total_time

# Sprocket Geometry
D1, C1 = sprocket_geometry(N1, p)
D2, C2 = sprocket_geometry(N2, p)

# Driver Rev Steps
steps_driver_rev = steps_for_driver_rev(effective_steps)

# Motion Profile Characteristics
Motion_Profile = alpha_time, alpha_dist, alpha, omega_time, omega_dist, max_omega = motion_profile_setup(theta_m, t_m, alpha_ratio)

# Radians Characteristics Setup
Radians_Characteristics = theta_m_rad, alpha_dist_rad, alpha_rad, omega_dist_rad, max_omega_rad = convert_to_radians(theta_m, alpha_dist, alpha, omega_dist, max_omega)

#Driven Rev Steps
steps_bicep_rev = steps_for_bicep_rev(C2, C1, steps_driver_rev, sprocket_gear_ratio)

# Total Motion Steps
total_motion_steps = calculate_steps(theta_m_rad, D2, C2, steps_bicep_rev)

# Motion Profile Step Phases
motion_profile_steps = alpha_steps, const_omega_steps = steps_motion_profile(total_motion_steps, alpha_dist_rad, omega_dist_rad, theta_m_rad)

# Delay Time
delay_time = delay_alpha, delay_omega, total_time = calculate_time_delays(alpha_time, omega_time, alpha_steps, const_omega_steps)

#Verifying time per Steps
time_profile_steps = time_steps(delay_alpha, alpha_steps, delay_omega, const_omega_steps)

def calculate_motion_profile():
    # Assuming sprocket_geometry, steps_for_driver_rev, motion_profile_setup, convert_to_radians
    # steps_for_bicep_rev, calculate_steps, steps_motion_profile, calculate_time_delays are defined here
    
    D1, C1 = sprocket_geometry(N1, p)
    D2, C2 = sprocket_geometry(N2, p)
    steps_driver_rev = steps_for_driver_rev(effective_steps)
    alpha_time, alpha_dist, alpha, omega_time, omega_dist, max_omega = motion_profile_setup(theta_m, t_m, alpha_ratio)
    theta_m_rad, alpha_dist_rad, alpha_rad, omega_dist_rad, max_omega_rad = convert_to_radians(theta_m, alpha_dist, alpha, omega_dist, max_omega)
    steps_bicep_rev = steps_for_bicep_rev(C2, C1, steps_driver_rev, sprocket_gear_ratio)
    total_motion_steps = calculate_steps(theta_m_rad, D2, C2, steps_bicep_rev)
    alpha_steps, const_omega_steps = steps_motion_profile(total_motion_steps, alpha_dist_rad, omega_dist_rad, theta_m_rad)
    delay_alpha, delay_omega, total_delay_time = calculate_time_delays(alpha_time, omega_time, alpha_steps, const_omega_steps)
    
    # Return the values you'll need in your motor control script
    return alpha_steps, const_omega_steps, delay_alpha, delay_omega

# Print Motion Profile Variables
print(f"Sprockets Characteristics D1, D2, C1, C2: {D1, D2, C1, C2}")
print(f"Motion Angular Characteristcs: {Motion_Profile}")
print(f"Motion Radian Characteristics: {Radians_Characteristics}")
print(f"Driver Rev Steps: {steps_driver_rev}")
print(f"Bicep Rev Steps: {steps_bicep_rev}")
print(f"Motion Profile Total Steps: {total_motion_steps}")
print(f"Motion Profile Step Phases: {motion_profile_steps}")
print(f"Motion Profile Delay Time: {delay_time}")
print(f"Motion Profile Steps Time: {time_profile_steps}")