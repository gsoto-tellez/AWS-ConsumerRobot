from machine import Pin
import time

# Define GPIO pins connected to the driver's STEP+, DIR+, and EN+ inputs
STEP = 17 # GPIO for STEP+
DIR = 4  # GPIO for DIR+
EN = 2    # GPIO for EN+

# Initialize GPIO pins
dir_pin = Pin(DIR, Pin.OUT)
step_pin = Pin(STEP, Pin.OUT)
en_pin = Pin(EN, Pin.OUT)

# Enable the stepper motor driver (assuming LOW to enable)
en_pin.value(0)

# Function to set the motor direction
def set_direction(clockwise):
    if clockwise:
        dir_pin.value(1)  # Clockwise
    else:
        dir_pin.value(0)  # Counter-clockwise

# Function to make the motor take a single step
def make_step():
    step_pin.value(1)
    time.sleep(0.001)  # Pulse duration, adjust as necessary
    step_pin.value(0)
    time.sleep(0.001)

# Example usage
try:
    set_direction(clockwise=True)  # Set initial direction to clockwise
    while True:
        make_step()  # Make steps in a loop

except KeyboardInterrupt:
    # Disable the stepper motor driver when stopping the script
    en_pin.value(1)  # Assuming HIGH to disable
    print("Stopped and motor driver disabled")
