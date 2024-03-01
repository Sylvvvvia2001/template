#Open valve
'''
Only implement this method if the flag SUPPORT_OPEN is set. For valves that can set position, this method should be left unimplemented and only set_valve_position is required.
'''

class MyValve(ValveEntity):
    # Implement one of these methods.

    def open_valve(self) -> None:
        """Open the valve."""

    async def async_open_valve(self) -> None:
        """Open the valve."""

#Close valve
'''
Only implement this method if the flag SUPPORT_CLOSE is set. For valves that can set position, this method should be left unimplemented and only set_valve_position is required.
'''

class MyValve(ValveEntity):
    # Implement one of these methods.

    def close_valve(self) -> None:
        """Close valve."""

    async def async_close_valve(self) -> None:
        """Close valve."""

#Set valve position
'''
Only implement this method if the flag SUPPORT_SET_POSITION is set. For valves that can open and close, this method should be left unimplemented and only open_valve and close_valve are required.
'''

class MyValve(ValveEntity):
    # Implement one of these methods.

    def set_valve_position(self, position: int) -> None:
        """Move the valve to a specific position."""

    async def async_set_valve_position(self, position: int) -> None:
        """Move the valve to a specific position."""

#Stop valve
'''
Only implement this method if the flag SUPPORT_STOP is set. 
'''
class MyValve(ValveEntity):
    # Implement one of these methods.

    def stop_valve(self) -> None:
        """Stop the valve."""

    async def async_stop_valve(self) -> None:
        """Stop the valve."""