#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"
#include "esp_log.h"

#define STEP_PIN 0
#define DIR_PIN 2
#define ENABLE_PIN 15

void app_main(void) {
    // Configure the I/O pins for the step, direction, and enable signals
    gpio_pad_select_gpio(STEP_PIN);
    gpio_pad_select_gpio(DIR_PIN);
    gpio_pad_select_gpio(ENABLE_PIN);

    gpio_set_direction(STEP_PIN, GPIO_MODE_OUTPUT);
    gpio_set_direction(DIR_PIN, GPIO_MODE_OUTPUT);
    gpio_set_direction(ENABLE_PIN, GPIO_MODE_OUTPUT);

    // Example sequence: enable the amplifier, set direction, perform a step, then disable
    gpio_set_level(ENABLE_PIN, 1); // Enable amplifier
    vTaskDelay(1000 / portTICK_PERIOD_MS); // Delay for a bit

    gpio_set_level(DIR_PIN, 1); // Set direction
    gpio_set_level(STEP_PIN, 1); // Perform a step
    vTaskDelay(100 / portTICK_PERIOD_MS); // Short delay

    gpio_set_level(STEP_PIN, 0); // Reset step pin
    gpio_set_level(ENABLE_PIN, 0); // Disable amplifier
}
