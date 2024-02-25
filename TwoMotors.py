from machine import Pin
import time

# Motor 1 configuration
MOTOR1_STEP = 5  # Adjust pin number based on your ESP32 setup - STEP+
MOTOR1_DIR = 4  # Adjust pin number based on your ESP32 setup - DIR+
MOTOR1_EN = 2    # Adjust pin number based on your ESP32 setup - EN+

# Motor 2 configuration
MOTOR2_STEP = 33 # Adjust for your ESP32 setup - STEP+ for the second motor
MOTOR2_DIR = 26  # Adjust for your ESP32 setup - DIR+ for the second motor
MOTOR2_EN = 14    # Adjust for your ESP32 setup - EN+ for the second motor

# Initialize motor 1 pins
motor1_dir = Pin(MOTOR1_DIR, Pin.OUT)
motor1_step = Pin(MOTOR1_STEP, Pin.OUT)
motor1_en = Pin(MOTOR1_EN, Pin.OUT)

# Initialize motor 2 pins
motor2_dir = Pin(MOTOR2_DIR, Pin.OUT)
motor2_step = Pin(MOTOR2_STEP, Pin.OUT)
motor2_en = Pin(MOTOR2_EN, Pin.OUT)

# Function to enable or disable drivers
def enable_motor(motor_en, enable=True):
    motor_en.value(not enable)  # Assuming LOW enables the driver, adjust if necessary

# Function to set direction
def set_direction(motor_dir, clockwise=True):
    motor_dir.value(clockwise)

# Function to make a step
def make_step(motor_step, delay=0.005):
    motor_step.value(1)
    time.sleep(delay)  # Step pulse width
    motor_step.value(0)
    time.sleep(delay)

# Example sequence
try:
    enable_motor(motor1_en, True)  # Enable motor 1
    enable_motor(motor2_en, True)  # Enable motor 2

    set_direction(motor1_dir, True)  # Motor 1 direction: clockwise
    set_direction(motor2_dir, False)  # Motor 2 direction: counter-clockwise

    for _ in range(200):  # Run for 200 steps
        make_step(motor1_step)
        make_step(motor2_step)

    # Change direction
    set_direction(motor1_dir, False)
    set_direction(motor2_dir, True)

    for _ in range(200):  # Run for another 200 steps
        make_step(motor1_step)
        make_step(motor2_step)

except KeyboardInterrupt:
    enable_motor(motor1_en, False)  # Disable motor 1
    enable_motor(motor2_en, False)  # Disable motor 2
    print("Stopped by user")
