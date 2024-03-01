#Turn On Command

class MyRemote(RemoteEntity):

    def turn_on(self, activity: str = None, **kwargs):
         """Send the power on command."""

    async def async_turn_on(self, activity: str = None, **kwargs):
         """Send the power on command."""

#Turn Off Command
         
class MyRemote(RemoteEntity):

    def turn_off(self, activity: str = None, **kwargs):
         """Send the power off command."""

    async def async_turn_off(self, activity: str = None, **kwargs):
         """Send the power off command."""

#Toggle Command

class MyRemote(RemoteEntity):

    def toggle(self, activity: str = None, **kwargs):
         """Toggle a device."""

    async def async_toggle(self, activity: str = None, **kwargs):
         """Toggle a device."""

#Send Command
         
class MyRemote(RemoteEntity):

    def send_command(self, command: Iterable[str], **kwargs):
        """Send commands to a device."""

    async def async_send_command(self, command: Iterable[str], **kwargs):
        """Send commands to a device."""


#Learn Command
'''Only implement this method if the flag SUPPORT_LEARN_COMMAND is set.'''

class MyRemote(RemoteEntity):

    def learn_command(self, **kwargs):
        """Learn a command from a device."""

    async def async_learn_command(self, **kwargs):
        """Learn a command from a device."""

#Delete Command
'''Only implement this method if the flag SUPPORT_DELETE_COMMAND is set.'''

class MyRemote(RemoteEntity):

    def delete_command(self, **kwargs):
        """Delete a command from a device."""

    async def async_delete_command(self, **kwargs):
        """Delete a command from a device."""