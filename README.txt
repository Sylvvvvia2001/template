The folder of minimum component should have __init__.py and manifest.json at least.

**************************************************************
Here's the example of the bare minimum component folder.

# hello_world/__init__.py:
"""
The "hello world" custom component.
The "hello world" custom component.

This component implements the bare minimum that a component should implement.

Configuration:

To use the hello_world component you will need to add the following to your
configuration.yaml file.

hello_world:
"""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

"""The domain of your component. Should be equal to the name of your component."""
DOMAIN = "hello_world"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.set('hello_world.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True

# hello_world/manifest.json:
{
  "domain": "hello_world",
  "name": "Hello World",
  "codeowners": [],
  "dependencies": [],
  "documentation": "https://github.com/home-assistant/example-custom-config/tree/master/custom_components/hello_world/",
  "iot_class": "local_polling",
  "requirements": [],
  "version": "0.1.0"
}

***********************************************
If you want to make a async component, here's the minimum example:

# hello_world_async/__init__.py:
"""
The "hello world" custom component.

This component implements the bare minimum that a component should implement.

Configuration:

To use the hello_world component you will need to add the following to your
configuration.yaml file.

hello_world_async:
"""
from __future__ import annotations

import asyncio

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

"""The domain of your component. Should be equal to the name of your component."""
DOMAIN = "hello_world_async"


@asyncio.coroutine
def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Setup our skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.async_set('hello_world_async.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True

# hello_world_async/manifest.json
{
  "domain": "hello_world_async",
  "name": "Hello World (async)",
  "codeowners": [],
  "dependencies": [],
  "documentation": "https://github.com/home-assistant/example-custom-config/tree/master/custom_components/hello_world_async/",
  "iot_class": "local_polling",
  "requirements": [],
  "version": "0.1.0"
}