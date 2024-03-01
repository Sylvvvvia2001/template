#Turn on Light Device

class MyLightEntity(LightEntity):
    def turn_on(self, **kwargs):
        """Turn the device on."""

    async def async_turn_on(self, **kwargs):
        """Turn device on."""

'''
Note that there's no color_mode passed to the async_turn_on method, instead only a single color attribute is allowed. It is guaranteed that the integration will only receive a single color attribute in a turn_oncall, which is guaranteed to be supported by the light according to the light's supported_color_modes property. To ensure this, colors in the service call will be translated before the entity's async_turn_on method is called if the light doesn't support the corresponding color mode:
'''

'''
Color type	Translation
color_temp	Will be removed from the service call if not supported and translated to hs_color, rgb_color, rgbw_color, rgbww_color or xy_color if supported by the light.
hs_color	Will be removed from the service call if not supported and translated to rgb_color, rgbw_color, rgbww_color or xy_color if supported by the light.
rgb_color	Will be removed from the service call if not supported and translated to rgbw_color, rgbww_color, hs_color or xy_color if supported by the light.
rgbw_color	Will be removed from the service call if not supported.
rgbww_color	Will be removed from the service call if not supported.
xy_color	Will be removed from the service call if not supported and translated to hs_color, rgb_color, rgbw_color or rgbww_color if supported by the light.
'''

#SCALING BRIGHTNESS

'''
Home Assistant includes a utility to scale brightness.

If the light supports brightness, sometimes the brightness value needs scaling:
'''

from homeassistant.util.color import value_to_brightness

BRIGHTNESS_SCALE = (1, 1023)

...

    @property
    def brightness(self) -> Optional[int]:
        """Return the current brightness."""
        return value_to_brightness(BRIGHTNESS_SCALE, self._device.brightness)

'''To scale the brightness to the device range:'''

from homeassistant.util.color import percentage_to_ranged_value
BRIGHTNESS_SCALE = (1, 1023)

...

class MyLightEntity(LightEntity):
    async def async_turn_on(self, **kwargs) -> None:
        """Turn device on."""

        ...

        value_in_range = math.ceil(percentage_to_ranged_value(BRIGHTNESS_SCALE, kwargs[ATTR_BRIGHTNESS]))


#Turn Off Light Device

class MyLightEntity(LightEntity):
    def turn_off(self, **kwargs):
        """Turn the device off."""

    async def async_turn_off(self, **kwargs):
        """Turn device off."""