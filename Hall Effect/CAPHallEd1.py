from machine import Pin
import time

HALL_SENSOR_PIN = 15  # Ensure this is the correct pin number for your setup

# Initialize the hall sensor as a global variable to make it accessible across functions
hall_sensor = Pin(HALL_SENSOR_PIN, Pin.IN)

def read_sensor():
    # Invert the reading for sensors that have opposite logic
    # This function now returns 1 when a magnet is present (sensor is tripped) and 0 otherwise
    return 1 if hall_sensor.value() == 0 else 0

def main():
    try:
        while True:
            sensor_state = read_sensor()
            print("Hall effect sensor state:", sensor_state)
            time.sleep(1)  # Delay for 1 second between readings
    except KeyboardInterrupt:
        print("Program terminated")

if __name__ == "__main__":
    main()
