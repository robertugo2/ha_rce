"""Constants for the RCE integration."""

from datetime import timedelta
from typing import Final

import logging

DOMAIN: Final = "rce"
CURRENCY: Final = "PLN"

DEFAULT_CUSTOM_PEAK_HOURS_RANGE = "10-17"
DEFAULT_LOW_PRICE_CUTOFF = 90
DEFAULT_NUMBER_OF_CHEAPEST_HOURS = 3
DEFAULT_PRICE_MODE = "LOW PRICE CUTOFF"
DEFAULT_PRICE_MULTIPLIER: Final = 1.23
DEFAULT_UNIT: Final = "MWh"
DEFAULT_PRICE_CAP: Final = False

CONF_CUSTOM_PEAK_HOURS_RANGE: Final = "custom_peak_range"
CONF_LOW_PRICE_CUTOFF: Final = "low_price_cutoff"
CONF_NUMBER_OF_CHEAPEST_HOURS: Final = "number_of_cheapest_hours"
CONF_PRICE_MODE: Final = "cheapest_price_mode"
CONF_PRICE_MULTIPLIER: Final = "price_multiplier"
CONF_UNIT: Final = "energy_unit"
CONF_PRICE_CAP: Final = "price_cap"

UNIT_TO_MULTIPLIER: Final = {
    "GWh": 1e3,
    "MWh": 1,
    "kWh": 1/1e3,
    "Wh":  1/1e6,
}

PRICE_MODES = [
    "LOW PRICE CUTOFF",
    "CHEAPEST CONSECUTIVE HOURS",
    "CHEAPEST HOURS (NOT CONSECUTIVE)",
]

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=30)
