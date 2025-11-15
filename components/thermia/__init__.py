import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, sensor
from esphome.const import (
    CONF_ID, 
    CONF_TRIGGER_ID
)

MULTI_CONF = True

AUTO_LOAD = ["sensor"]

DEPENDENCIES = ['i2c']

thermia_ns = cg.esphome_ns.namespace('thermia')
Thermia = thermia_ns.class_('Thermia', i2c.I2CDevice, cg.Component)
CONF_ENCODER_FILTER = "encoder_filter"
CONF_BUTTON = "button"
CONF_ENCODER = "encoder"

THERMIA_SCHEMA = cv.Schema(
    {
        cv.Optional(CONF_ENCODER_FILTER, default=1): cv.int_range(min=1, max=100),
    }
).extend(sensor.sensor_schema())

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(Thermia),
        cv.Optional(CONF_ENCODER): THERMIA_SCHEMA,
    }
).extend(i2c.i2c_device_schema(0x42))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)

    if CONF_ENCODER in config:
        sens = await sensor.new_sensor(config[CONF_ENCODER])
        cg.add(var.set_encoder(sens))

        encoderConfig = config[CONF_ENCODER]

        if CONF_ENCODER_FILTER in encoderConfig:
            cg.add(var.set_encoder_filter(encoderConfig[CONF_ENCODER_FILTER]))
