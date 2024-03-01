#Set value
'''
Called when the user or an automation wants to update the value.
'''

class MyDate(DateEntity):
    # Implement one of these methods.

    def set_value(self, value: date) -> None:
        """Update the current value."""

    async def async_set_value(self, value: date) -> None:
        """Update the current value."""

