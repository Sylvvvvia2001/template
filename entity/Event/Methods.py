#Firing events
'''
The event entity is a little different compared to other entities. Home Assistant manages the state, but the integration is responsible for firing the events. This is done by calling the _trigger_event method on the event entity.

This method takes the event type as the first argument and optionally extra state data as the second argument.
'''

class MyEvent(EventEntity):

    _attr_device_class = EventDeviceClass.BUTTON
    _attr_event_types = ["single_press", "double_press"]

    @callback
    def _async_handle_event(self, event: str) -> None:
        """Handle the demo button event."""
        self._trigger_event(event, {"extra_data": 123})
        self.async_write_ha_state()

    async def async_added_to_hass(self) -> None:
        """Register callbacks with your device API/library."""
        my_device_api.listen(self._async_handle_event)


'''
Only event types that are defined in the event_types property can be fired. If an event type is fired that is not defined in the event_types property, a ValueError will be raised.

TIP
Be sure to deregister any callbacks when the entity is removed from Home Assistant.
'''