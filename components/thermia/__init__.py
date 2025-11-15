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
CONF_THERMIA = "thermia"

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(Thermia),
    }
).extend(i2c.i2c_device_schema(0x42))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)

