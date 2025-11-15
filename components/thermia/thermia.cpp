#include "thermia.h"
#include "esphome/core/helpers.h"
#include "esphome/core/log.h"

namespace esphome {
namespace thermia {

static const char* const TAG = "thermia";

static const uint8_t THERMIA_ADDRESS = 0xFE;

float Thermia::get_setup_priority() const {
  return setup_priority::IO;
}

void Thermia::setup() {
  ESP_LOGI(TAG, "Setting up Thermia...");
  uint8_t firmware;
  if (this->read_register(THERMIA_ADDRESS, &firmware, 1) !=
      i2c::ERROR_OK) {
    ESP_LOGE(TAG, "Thermia Setup Failed");
    this->mark_failed();
    return;
  }
  setEncoderValue(0);
  ESP_LOGI(TAG, "Thermia Firmware: %d", firmware);
}



}  // namespace thermia
}  // namespace esphome