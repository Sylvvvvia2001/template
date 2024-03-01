#Image
'''
Implement async_image or image if your entity returns bytes of the image instead of providing a URL. Frontend will call async_image or image to fetch the image. If the image is fetched remotely, image data should be cached and the cache invalidated when image_last_updated is changed.

Note that:

The image entity's async_image or image method is only called when frontend fetches the image.
Frontend will:
Fetch the image once when a page with an image entity is loaded
Refetch the image when the image entity's state changed by the image entity changing image_last_updated
This means it's incorrect to bump the image_last_updated property inside async def async_image. Instead, the image entity should, when an updated image is available or periodically if the image should be refetched after some time, update the image_last_updated timestamp. This can for example happen as part of an entity coordinator update.
'''

class MyImage(ImageEntity):
    # Implement one of these methods.

    def image(self) -> bytes | None:
        """Return bytes of image."""

    async def async_image(self) -> bytes | None:
        """Return bytes of image."""