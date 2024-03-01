#Camera Image
'''
When the width and height are passed, scaling should be done on a best-effort basis. The UI will fall back to scaling at the display layer if scaling cannot be done by the camera.

Return the smallest image that meets the minimum width and minimum height.

When scaling the image, aspect ratio must be preserved. If the aspect ratio is not the same as the requsted height or width, it is expected that the width and/or height of the returned image will be larger than requested.

Pass on the width and height if the underlying camera is capable of scaling the image.

If the integration cannot scale the image and returns a jpeg image, it will automatically be scaled by the camera integration when requested.
'''

class MyCamera(Camera):
    # Implement one of these methods.

    def camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        """Return bytes of camera image."""
        raise NotImplementedError()

    async def async_camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        """Return bytes of camera image."""


#Stream Source
'''
The stream source should return a url that is usable by ffmpeg (e.g. an RTSP url). Requires CameraEntityFeature.STREAM.

A camera entity with a stream source by default uses StreamType.HLS to tell the frontend to use an HLS feed with the stream component. This stream source will also be used with stream for recording.
'''

class MyCamera(Camera):

    async def stream_source(self) -> str | None:
        """Return the source of the stream."""
'''A common way for a camera entity to render a camera still image is to pass the stream source to async_get_image in the ffmpeg component.'''


#WebRTC Streams
'''WebRTC enabled cameras can be used by facilitating a direct connection with the home assistant frontend. This usage requires CameraEntityFeature.STREAM with frontend_stream_type set to StreamType.WEB_RTC. The integration should implement async_handle_web_rtc_offer which passes the frontend's SDP offer to the device and returns back the answer.

WebRTC streams do not use the stream component and do not support recording.'''

class MyCamera(Camera):

    async def async_handle_web_rtc_offer(self, offer_sdp: str) -> str | None:
        """Handle the WebRTC offer and return an answer."""

#RTSP to WebRTC
'''An integration may provide a WebRTC stream for any RTSP camera using async_register_rtsp_to_web_rtc_provider. The current best practice is for an integration to provide the actual stream manipulation with an Add-on or external service.
'''
async def handle_offer(stream_source: str, offer_sdp: str) -> str:
    """Handle the signal path for a WebRTC stream and return an answer."""
    try:
        return await client.offer(offer_sdp, stream_source)
    except ClientError as err:
        raise HomeAssistantError from err

# Call unsub() when integration unloads
unsub = camera.async_register_rtsp_to_web_rtc_provider(
    hass, DOMAIN, handle_offer
)

#Turn on
class MyCamera(Camera):
    # Implement one of these methods.

    def turn_on(self) -> None:
        """Turn on camera."""

    async def async_turn_on(self) -> None:
        """Turn on camera."""

#Turn off
class MyCamera(Camera):
    # Implement one of these methods.

    def turn_off(self) -> None:
        """Turn off camera."""

    async def async_turn_off(self) -> None:
        """Turn off camera."""

#Enable Motion Detection
class MyCamera(Camera):
    # Implement one of these methods.

    def enable_motion_detection(self) -> None:
        """Enable motion detection in the camera."""

    async def async_enable_motion_detection(self) -> None:
        """Enable motion detection in the camera."""


#Disable Motion Detection
class MyCamera(Camera):
    # Implement one of these methods.

    def disable_motion_detection(self) -> None:
        """Disable motion detection in camera."""

    async def async_disable_motion_detection(self) -> None:
        """Disable motion detection in camera."""
