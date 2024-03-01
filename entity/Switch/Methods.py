#Turn on
class MySwitch(SwitchEntity):
    # Implement one of these methods.

    def turn_on(self, **kwargs) -> None:
        """Turn the entity on."""

    async def async_turn_on(self, **kwargs):
        """Turn the entity on."""

#Turn off
class MySwitch(SwitchEntity):
    # Implement one of these methods.

    def turn_off(self, **kwargs):
        """Turn the entity off."""

    async def async_turn_off(self, **kwargs):
        """Turn the entity off."""

#Toggle
'''Optional. If not implemented will default to checking what method to call using the is_on property.'''
class MySwitch(SwitchEntity):
    # Implement one of these methods.

    def toggle(self, **kwargs):
        """Toggle the entity."""

    async def async_toggle(self, **kwargs):
        """Toggle the entity."""