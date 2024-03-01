#Play Media
'''Tells the media player to play media. Implement it using the following:'''

class MyMediaPlayer(MediaPlayerEntity):

    def play_media(
        self,
        media_type: str,
        media_id: str,
        enqueue: MediaPlayerEnqueue | None = None,
        announce: bool | None = None, **kwargs: Any
    ) -> None:
        """Play a piece of media."""

    async def async_play_media(
        self,
        media_type: str,
        media_id: str,
        enqueue: MediaPlayerEnqueue | None = None,
        announce: bool | None = None, **kwargs: Any
    ) -> None:
        """Play a piece of media."""

'''
The enqueue attribute is a string enum MediaPlayerEnqueue:

add: add given media item to end of the queue
next: play the given media item next, keep queue
play: play the given media item now, keep queue
replace: play the given media item now, clear queue
When the announce boolean attribute is set to true, the media player should try to pause the current music, announce the media to the user and then resume the music.
'''


#Browse Media
'''If the media player supports browsing media, it should implement the following method:
'''

class MyMediaPlayer(MediaPlayerEntity):

    async def async_browse_media(
        self, media_content_type: str | None = None, media_content_id: str | None = None
    ) -> BrowseMedia:
        """Implement the websocket media browsing helper."""
        return await media_source.async_browse_media(
            self.hass,
            media_content_id,
            content_filter=lambda item: item.media_content_type.startswith("audio/"),
        )

'''If the media player also allows playing media from URLs, you can also add support for browsing Home Assistant media sources. These sources can be provided by any integration. Examples provide text-to-speech and local media.'''

from homeassistant.components import media_source
from homeassistant.components.media_player.browse_media import (
    async_process_play_media_url,
)

class MyMediaPlayer(MediaPlayerEntity):

    async def async_browse_media(
        self, media_content_type: str | None = None, media_content_id: str | None = None
    ) -> BrowseMedia:
        """Implement the websocket media browsing helper."""
        # If your media player has no own media sources to browse, route all browse commands
        # to the media source integration.
        return await media_source.async_browse_media(
            self.hass,
            media_content_id,
            # This allows filtering content. In this case it will only show audio sources.
            content_filter=lambda item: item.media_content_type.startswith("audio/"),
        )

    async def async_play_media(
        self,
        media_type: str,
        media_id: str,
        enqueue: MediaPlayerEnqueue | None = None,
        announce: bool | None = None, **kwargs: Any
    ) -> None:
        """Play a piece of media."""
        if media_source.is_media_source_id(media_id):
            media_type = MediaType.MUSIC
            play_item = await media_source.async_resolve_media(self.hass, media_id, self.entity_id)
            # play_item returns a relative URL if it has to be resolved on the Home Assistant host
            # This call will turn it into a full URL
            media_id = async_process_play_media_url(self.hass, play_item.url)

        # Replace this with calling your media player play media function.
        await self._media_player.play_url(media_id)

#Select sound mode
'''
Optional. Switch the sound mode of the media player.
'''

class MyMediaPlayer(MediaPlayerEntity):
    # Implement one of these methods.

    def select_sound_mode(self, sound_mode):
        """Switch the sound mode of the entity."""

    def async_select_sound_mode(self, sound_mode):
        """Switch the sound mode of the entity."""

#Select source
'''
Optional. Switch the selected input source for the media player.
'''
class MyMediaPlayer(MediaPlayerEntity):
    # Implement one of these methods.

    def select_source(self, source):
        """Select input source."""

    def async_select_source(self, source):
        """Select input source."""