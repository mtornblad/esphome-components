#pragma once

#include <utility>
#include "esphome/components/i2c/i2c.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/core/component.h"


namespace esphome {
namespace thermia {

class Thermia : public i2c::I2CDevice, public Component {
 public:
  void setup() override;
  void loop() override;

  void set_number(uint8_t number) { number_ = number; }
  void set_min_value(int32_t min_value) { this->min_value_ = min_value; }
  void set_max_value(int32_t max_value) { this->max_value_ = max_value; }

  float get_setup_priority() const override;

 protected:
  uint8_t number_{0};
  int32_t value_{0};
  int encoder_filter_ = 1;
  int32_t min_value_{INT32_MIN};
  int32_t max_value_{INT32_MAX};

  sensor::Sensor* encoder_value_{nullptr};
  sensor::Sensor* firmware_version_{nullptr};
};


}  // namespace thermia
}  // namespace esphome