#Press
#The press method can be used to trigger an action towards a device or service. It is called by Home Assistant when the user presses the button or the service to press the button has been called.

class MyButton(ButtonEntity):
    # Implement one of these methods.

    def press(self) -> None:
        """Handle the button press."""

    async def async_press(self) -> None:
        """Handle the button press."""