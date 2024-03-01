#Set HVAC mode

class MyClimateEntity(ClimateEntity):
    # Implement one of these methods.

    def set_hvac_mode(self, hvac_mode):
        """Set new target hvac mode."""

    async def async_set_hvac_mode(self, hvac_mode):
        """Set new target hvac mode."""

#Turn on
        
class MyClimateEntity(ClimateEntity):
    # Implement one of these methods.
    # The `turn_on` method should set `hvac_mode` to any other than
    # `HVACMode.OFF` by optimistically setting it from the service handler
    # or with the next state update

    def turn_on(self):
        """Turn the entity on."""

    async def async_turn_on(self):
        """Turn the entity on."""

#Turn off
        
class MyClimateEntity(ClimateEntity):
    # Implement one of these methods.
    # The `turn_off` method should set `hvac_mode` to `HVACMode.OFF` by
    # optimistically setting it from the service handler or with the next state update

    def turn_off(self):
        """Turn the entity off."""

    async def async_turn_off(self):
        """Turn the entity off."""

#Toggle

class MyClimateEntity(ClimateEntity):
    # It's not mandatory to implement the `toggle` method as the base implementation
    # will call `turn_on`/`turn_off` according to the current HVAC mode.

    # If implemented, the `toggle` method should set `hvac_mode` to the right `HVACMode` by
    # optimistically setting it from the service handler or with the next state update.

    def toggle(self):
        """Toggle the entity."""

    async def async_toggle(self):
        """Toggle the entity."""

#Set Temperature
class MyClimateEntity(ClimateEntity):
    # Implement one of these methods.

    def set_preset_mode(self, preset_mode):
        """Set new target preset mode."""

    async def async_set_preset_mode(self, preset_mode):
        """Set new target preset mode."""

#Set Fan Mode
        
class MyClimateEntity(ClimateEntity):
    # Implement one of these methods.

    def set_fan_mode(self, fan_mode):
        """Set new target fan mode."""

    async def async_set_fan_mode(self, fan_mode):
        """Set new target fan mode."""

#Set humidity

class MyClimateEntity(ClimateEntity):
    # Implement one of these methods.

    def set_humidity(self, humidity):
        """Set new target humidity."""

    async def async_set_humidity(self, humidity):
        """Set new target humidity."""


#Set swing mode

class MyClimateEntity(ClimateEntity):
    # Implement one of these methods.

    def set_swing_mode(self, swing_mode):
        """Set new target swing operation."""

    async def async_set_swing_mode(self, swing_mode):
        """Set new target swing operation."""

#Set temperature

class MyClimateEntity(ClimateEntity):
    # Implement one of these methods.

    def set_temperature(self, **kwargs):
        """Set new target temperature."""

    async def async_set_temperature(self, **kwargs):
        """Set new target temperature."""

#Control auxiliary heater

class MyClimateEntity(ClimateEntity):
    # Implement one of these methods.

    def turn_aux_heat_on(self):
        """Turn auxiliary heater on."""

    async def async_turn_aux_heat_on(self):
        """Turn auxiliary heater on."""

    # Implement one of these methods.

    def turn_aux_heat_off(self):
        """Turn auxiliary heater off."""

    async def async_turn_aux_heat_off(self):
        """Turn auxiliary heater off."""
        