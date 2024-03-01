#Set mode

class MyHumidifierEntity(HumidifierEntity):
    # Implement one of these methods.

    def set_mode(self, mode):
        """Set new target preset mode."""

    async def async_set_mode(self, mode):
        """Set new target preset mode."""

#Set humidity
'''
If the current mode does not allow to adjust target humidity, the device should automatically change its mode to the one which makes it possible upon this call.'''

class MyHumidifierEntity(HumidifierEntity):
    # Implement one of these methods.

    def set_humidity(self, humidity):
        """Set new target humidity."""

    async def async_set_humidity(self, humidity):
        """Set new target humidity."""

#Turn on
class MyHumidifierEntity(HumidifierEntity):
    # Implement one of these methods.

    def turn_on(self, **kwargs):
        """Turn the device on."""

    async def async_turn_on(self, **kwargs):
        """Turn the device on."""

#Turn off
        
class MyHumidifierEntity(HumidifierEntity):
    # Implement one of these methods.

    def turn_off(self, **kwargs):
        """Turn the device off."""

    async def async_turn_off(self, **kwargs):
        """Turn the device off."""
