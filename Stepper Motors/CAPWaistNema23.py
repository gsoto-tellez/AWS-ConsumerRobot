#Sample code for CAP Nema 23 HS22
from machine import Pin
import time
from waistCalc import calculate_motion_profile

#Configuration of Pins
STEP_PIN = 0
DIR_PIN = 2
ENABLE_PIN = 15
#BUTTON_PIN = 15

#Stepper Motor Parameters
step_angle = 1.8
steps_per_revolution = 200 # Effective Sep = 5370 with GR

#setup pins
step_pin = Pin(STEP_PIN, Pin.OUT)
dir_pin = Pin(DIR_PIN, Pin.OUT)
enable_pin = Pin(ENABLE_PIN, Pin.OUT)

# Setup button pin
#button_pin = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)  # Setup as input with pull-up

def step(steps, direction, delay):
    dir_pin.value(direction)
    for _ in range(steps):
        step_pin.value(1)
        time.sleep_us(delay)
        step_pin.value(0)
        time.sleep_us(delay)
        pass

def run1():
    # Values from bicepCalc
    alpha_steps, const_omega_steps, delay_alpha, delay_omega = calculate_motion_profile()
    total_start_time = time.time()  # Start timing for the whole phase
    
    enable_pin.value(0) # Enable the driver after motion is complete
    
    # Accelerate
    start_time = time.time()  # Start timing for acceleration
    step(alpha_steps, 0, delay_alpha)   # steps, direction 1, delay
    print(f"Acceleration 1 Time: {time.time() - start_time} seconds")
    
    # Constant speed
    start_time = time.time()  # Reset start time for constant speed
    step(const_omega_steps, 0, delay_omega)   # steps, direction 1, delay
    print(f"Constant Speed 1 Time: {time.time() - start_time} seconds")
    
    # Decelerate
    start_time = time.time()  # Reset start time for deceleration
    step(alpha_steps, 0, delay_alpha)  # steps, direction 1, delay
    print(f"Deceleration 1 Time: {time.time() - start_time} seconds")
    
    enable_pin.value(1) # Disable the driver after motion is complete
    print(f"First performance run: {time.time() - total_start_time} seconds")
    
def run2():
    #Values from bicepCalc
    alpha_steps, const_omega_steps, delay_alpha, delay_omega = calculate_motion_profile()
    
    total_start_time = time.time()  # Start timing for the whole phase
    
    enable_pin.value(0) # Enable the driver after motion is complete
    
    # Accelerate
    start_time = time.time()  # Start timing for acceleration
    step(alpha_steps, 1, delay_alpha)   # steps, direction 1, delay
    print(f"Acceleration 1 Time: {time.time() - start_time} seconds")
    
    # Constant speed
    start_time = time.time()  # Reset start time for constant speed
    step(const_omega_steps, 1, delay_omega)   # steps, direction 1, delay
    print(f"Constant Speed 1 Time: {time.time() - start_time} seconds")
    
    # Decelerate
    start_time = time.time()  # Reset start time for deceleration
    step(alpha_steps, 1, delay_alpha)  # steps, direction 1, delay
    print(f"Deceleration 1 Time: {time.time() - start_time} seconds")
    
    enable_pin.value(1) # Disable the driver after motion is complete
    print(f"First performance run: {time.time() - total_start_time} seconds")
    
def main():
    #print("Press the button to start...")
    #while button_pin.value() == 1:
     # Wait here until the button is pressed
     #   pass  # Wait until the button is pressed
        
    #print("Button pressed. . . . .")
    
    # Reset the flag at the start of the total execution cycle
    global time_printed
    time_printed = False
    print("Starting sequence...")
    start_time = time.time() # Start Timing
    run1()
    time.sleep(3)  # Pause for 5 seconds, adjust this value as needed
    run2()
    total_end_time = time.time() # End Timing
    print(f"Total Experiment Time: {total_end_time - start_time} seconds")
    
if __name__ == "__main__":
    main()