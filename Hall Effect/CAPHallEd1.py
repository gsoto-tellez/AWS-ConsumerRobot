from machine import Pin
import time

HALL_SENSOR_PIN = 4  # Ensure this is the correct pin number for your setup

# Initialize the hall sensor as a global variable to make it accessible across functions
hall_sensor = Pin(HALL_SENSOR_PIN, Pin.IN)

def read_sensor():
    # Directly read the value from the hall sensor
    return hall_sensor.value()

def main():
    try:
        while True:
            sensor_state = read_sensor()
            print("Hall effect sensor state:", sensor_state)
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
