#Set value
'''Called when the user or an automation wants to update the value.'''
class MyNumber(NumberEntity):
    # Implement one of these methods.

    def set_native_value(self, value: float) -> None:
        """Update the current value."""

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
