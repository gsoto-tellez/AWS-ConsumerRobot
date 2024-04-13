#include <stdio.h>
#include <time.h>
#include <unistd.h> // For usleep function

// Mock functions to simulate GPIO operations
void pinMode(int pin, int mode) {
    // Mode 1 for OUTPUT, 0 for INPUT
    printf("Setting pin %d to %s\n", pin, mode ? "OUTPUT" : "INPUT");
}

void digitalWrite(int pin, int value) {
    printf("Writing %d to pin %d\n", value, pin);
}

void delayMicroseconds(int delay_us) {
    usleep(delay_us);
}

// Constants for pin configuration
#define STEP_PIN 27
#define DIR_PIN 14
#define ENABLE_PIN 12

// Function to perform a number of steps
void step(int steps, int direction, int delay_us) {
    digitalWrite(DIR_PIN, direction);
    for (int i = 0; i < steps; i++) {
        digitalWrite(STEP_PIN, 1);
        delayMicroseconds(delay_us);
        digitalWrite(STEP_PIN, 0);
        delayMicroseconds(delay_us);
    }
}

// Main control function for the stepper motor
void run1() {
    int alpha_steps = 100; // Example value
    int const_omega_steps = 150; // Example value
    int delay_alpha = 800; // Example delay in microseconds
    int delay_omega = 600; // Example delay in microseconds

    clock_t total_start_time = clock();

    digitalWrite(ENABLE_PIN, 0); // Enable the driver

    // Accelerate
    clock_t start_time = clock();
    step(alpha_steps, 1, delay_alpha);
    printf("Acceleration 1 Time: %ld milliseconds\n", (clock() - start_time) * 1000 / CLOCKS_PER_SEC);

    // Constant speed
    start_time = clock();
    step(const_omega_steps, 1, delay_omega);
    printf("Constant Speed 1 Time: %ld milliseconds\n", (clock() - start_time) * 1000 / CLOCKS_PER_SEC);

    // Decelerate
    start_time = clock();
    step(alpha_steps, 1, delay_alpha);
    printf("Deceleration 1 Time: %ld milliseconds\n", (clock() - start_time) * 1000 / CLOCKS_PER_SEC);

    digitalWrite(ENABLE_PIN, 1); // Disable the driver

    printf("First performance run: %ld milliseconds\n", (clock() - total_start_time) * 1000 / CLOCKS_PER_SEC);
}

int main() {
    pinMode(STEP_PIN, 1);
    pinMode(DIR_PIN, 1);
    pinMode(ENABLE_PIN, 1);
    run1();
    return 0;
}
