#Get Events
'''
A calendar entity can return events that occur during a particular time range. Some notes for implementors:

The start_date is the lower bound and applied to the event's end (exclusive). This has a tzinfo of the local Home Assistant timezone.
The end_date is the upper bound and applied to the event's start (exclusive). This has the same tzinfo as start_date.
Recurring events should be flattened and returned as individual CalendarEvent.
An calendar entity is responsible for returning the events in order including correctly ordering all day events. An all day event should be ordered to start at midnight in the Home Assistant timezone (e.g. from the start/end time argument tzinfo, or using homeassistant.util.dt.start_of_local_day). Note that all day events should still set a datetime.date in the CalendarEvent and not a date with a time.
'''

import datetime
from homeassistant.core import HomeAssistant
from homeassistant.components.calendar import CalendarEntity

class MyCalendar(CalendarEntity):

    async def async_get_events(
        self,
        hass: HomeAssistant,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
    ) -> list[CalendarEvent]:
        """Return calendar events within a datetime range."""

#Create Events
'''
A calendar entity may support creating events by specifying the CREATE_EVENT supported feature. Integrations that support mutation must handle rfc5545 fields and best practices such as preserving any new unknown fields that are set and recurring events.
'''

from homeassistant.components.calendar import CalendarEntity

class MyCalendar(CalendarEntity):

    async def async_create_event(self, **kwargs: Any) -> None:
        """Add a new event to calendar."""

#Delete Events
'''
A calendar entity may support deleting events by specifying the DELETE_EVENT supported feature. Integrations that support mutation must support rfc5545 recurring events.

There are three ways that recurring events may be deleted:

Specifying only the uid will delete the entire series
Specifying the uid and recurrence_id will delete the specific event instance in the series
Specifying uid, recurrence_id, and a recurrence_range value may delete a range of events starting at recurrence_id. Currently rfc5545 allows the range value of THISANDFUTURE.
'''

from homeassistant.components.calendar import CalendarEntity


class MyCalendar(CalendarEntity):

    async def async_delete_event(
        self,
        uid: str,
        recurrence_id: str | None = None,
        recurrence_range: str | None = None,
    ) -> None:
        """Delete an event on the calendar."""

#Update Events
'''
A calendar entity may support updating events by specifying the UPDATE_EVENT supported feature. Integrations that support mutation must support rfc5545 recurring events.

There are three ways that recurring events may be updated:

Specifying only the uid will update the entire series
Specifying the uid and recurrence_id will update the specific event instance in the series
Specifying uid, recurrence_id, and a recurrence_range value may update a range of events starting at recurrence_id. Currently rfc5545 allows the range value of THISANDFUTURE.
'''

from homeassistant.components.calendar import CalendarEntity


class MyCalendar(CalendarEntity):

    async def async_update_event(
        self,
        uid: str,
        event: dict[str, Any],
        recurrence_id: str | None = None,
        recurrence_range: str | None = None,
    ) -> None:
        """Update an event on the calendar."""


