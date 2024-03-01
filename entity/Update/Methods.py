#Install
'''
This method can be implemented so users can install an offered update directly from within Home Assistant.

This method requires UpdateEntityFeature.INSTALL to be set. Additionally, if this integration supports installing specific version or is capable of backing up before starting the update installation process, UpdateEntityFeature.SPECIFIC_VERSION and UpdateEntityFeature.BACKUP can be set respectively.
'''

class MyUpdate(UpdateEntity):
    # Implement one of these methods.

    def install(
        self, version: str | None, backup: bool, **kwargs: Any
    ) -> None:
        """Install an update."""

    async def async_install(
        self, version: str | None, backup: bool, **kwargs: Any
    ) -> None:
        """Install an update.

        Version can be specified to install a specific version. When `None`, the
        latest version needs to be installed.

        The backup parameter indicates a backup should be taken before
        installing the update.
        """

#Release notes
'''
This method can be implemented so users can can get the full release notes in the more-info dialog of the Home Assistant Frontend before they install the update.

The returned string can contain markdown, and the frontend will format that correctly.

This method requires UpdateEntityFeature.RELEASE_NOTES to be set.


'''

class MyUpdate(UpdateEntity):
    # Implement one of these methods.

    def release_notes(self) -> str | None:
        """Return the release notes."""
        return "Lorem ipsum"

    async def async_release_notes(self) -> str | None:
        """Return the release notes."""
        return "Lorem ipsum"

