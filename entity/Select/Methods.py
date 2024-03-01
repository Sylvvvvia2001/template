#Select option
'''Called when the user or automation wants to change the current selected option.'''
class MySelect(SelectEntity):
    # Implement one of these methods.

    def select_option(self, option: str) -> None:
        """Change the selected option."""

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
