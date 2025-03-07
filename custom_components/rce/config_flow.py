"""RCE PSE config flow"""
from __future__ import annotations

import re
from typing import Any

import voluptuous as vol
import logging

from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
    FlowResult
)

from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv
_LOGGER = logging.getLogger(__name__)

from .const import (
    DOMAIN,
    CONF_CUSTOM_PEAK_HOURS_RANGE, DEFAULT_CUSTOM_PEAK_HOURS_RANGE,
    CONF_LOW_PRICE_CUTOFF, DEFAULT_LOW_PRICE_CUTOFF,
    CONF_NUMBER_OF_CHEAPEST_HOURS, DEFAULT_NUMBER_OF_CHEAPEST_HOURS,
    CONF_PRICE_MODE, DEFAULT_PRICE_MODE, PRICE_MODES,
    CONF_PRICE_MULTIPLIER, DEFAULT_PRICE_MULTIPLIER,
    CONF_UNIT, DEFAULT_UNIT, UNIT_TO_MULTIPLIER,
    CONF_PRICE_CAP, DEFAULT_PRICE_CAP
)

RE_HOURS_RANGE = re.compile(r"^/d{1,2}-/d{1,2}$")

DATA_SCHEMA = vol.Schema(
    {
        vol.Optional(
            CONF_CUSTOM_PEAK_HOURS_RANGE,
            default=DEFAULT_CUSTOM_PEAK_HOURS_RANGE
        ): str,
        vol.Optional(
            CONF_LOW_PRICE_CUTOFF,
            default=DEFAULT_LOW_PRICE_CUTOFF
        ): vol.Coerce(int),
        vol.Optional(
            CONF_NUMBER_OF_CHEAPEST_HOURS,
            default=DEFAULT_NUMBER_OF_CHEAPEST_HOURS
        ): vol.Coerce(int),
        vol.Optional(
            CONF_PRICE_MODE,
            default=DEFAULT_PRICE_MODE
        ): vol.In(PRICE_MODES),
        vol.Optional(
            CONF_PRICE_MULTIPLIER,
            default=DEFAULT_PRICE_MULTIPLIER
        ): vol.Coerce(float),
        vol.Optional(
            CONF_UNIT,
            default=DEFAULT_UNIT,
        ): vol.In(list(UNIT_TO_MULTIPLIER.keys())),
        vol.Optional(
            CONF_PRICE_CAP,
            default=DEFAULT_PRICE_CAP,
        ): vol.Coerce(bool),
    }
)

class PSESensorConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for RCE PSE sensor."""
    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(
            config_entry: ConfigEntry,
    ) -> PSESensorOptionFlow:
        """Create the options flow."""
        return PSESensorOptionFlow(config_entry)

    async def async_step_user(self, user_input=None) -> FlowResult:

        if user_input is not None:
            await self.async_set_unique_id("rce")
            self._abort_if_unique_id_configured()
            _LOGGER.debug(f"User data: {user_input}")
            return self.async_create_entry(title="PSE RCE", data={}, options=user_input)

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA)

class PSESensorOptionFlow(OptionsFlow):
    """Handle a option flow for RCE PSE sensor."""

    VERSION = 1

    def __init__(self, config_entry) -> None:
        """Initialize the options flow."""
        self.config_entry = config_entry
        _LOGGER.debug("Config: %s", self.config_entry.data)
        _LOGGER.debug("Options: %s", self.config_entry.options)

    async def async_step_init(self, user_input=None) -> ConfigFlowResult:
        """Manage the options."""

        if user_input is not None:
            _LOGGER.debug("user_input: %s", user_input)
            return self.async_create_entry(title="PSE RCE", data=user_input)

        return self.async_show_form(step_id="init", data_schema=self.add_suggested_values_to_schema(DATA_SCHEMA, self.config_entry.options))
