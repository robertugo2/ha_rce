### *Fork of https://github.com/jacek2511/ha_rce. Thanks @jacek2511 for your work!*
Improved:
 * Simplify the config flow
 * Add new parameter: price multiplier - thanks to that it is possible to include 23% VAT for an exported energy (the multiplier is set by default to 1.23)
 * Attributes are compatible with https://github.com/MTrab/energidataservice so it is possible to use this integration in https://github.com/springfall2008/batpred
# homeassistant-rce

[![GitHub Latest Release][releases_shield]][latest_release] [![License][license-shield]](LICENSE) [![GitHub All Releases][downloads_total_shield]][releases] [![GH-last-commit][latest_commit]][commits] [![HACS][hacsbadge]][hacs]
<!-- [![usage_badge](https://img.shields.io/badge/dynamic/json?label=Usage&query=ha_rce.total&url=https://analytics.home-assistant.io/custom_integrations.json)](https://analytics.home-assistant.io) -->


# homeassistant-rce
**Rynkowa cena energii elektrycznej (RCE)**

This is an integration between Home Assistant and PSE RCE

The RCE sensor provides the current price with today's and tomorrow's prices as attributes. Prices for the next day become available around 3:00 p.m.

<a href="https://github.com/RomRider/apexcharts-card">ApexCharts</a> card is recommended for visualization of the data in Home Assistant.

Example configuration for the cards
<pre class="wp-block-code"><code>type: custom:apexcharts-card
graph_span: 24h
span:
  start: day
now:
  show: true
  label: Teraz
  color: var(--secondary-color)
yaxis:
  - decimals: 3
    id: Ceny
    apex_config:
      tickAmount: 5
  - decimals: 1
    id: Prognoza
    opposite: true
    apex_config:
      tickAmount: 5
series:
  - entity: sensor.rynkowa_cena_energii_elektrycznej_rynkowa_cena_energi_elektrycznej
    yaxis_id: Ceny
    type: column
    name: Cena
    float_precision: 0
    data_generator: |
      return entity.attributes.raw_today.map((start, index) => {
        return [new Date(start["hour"]).getTime(), entity.attributes.raw_today[index]['price']];
      });
  - entity: sensor.solcast_pv_forecast_prognoza_na_dzisiaj
    yaxis_id: Prognoza
    type: line
    name: Prognoza
    float_precision: 1
    data_generator: |
      var today = entity.attributes.detailedForecast.map((start, index) => {
        return [new Date(start["period_start"]).getTime(), entity.attributes.detailedForecast[index]["pv_estimate"]];
      });
      var data = today
      return data;</code></pre>

# Install

### Using [HACS](https://hacs.xyz/) (recommended)
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=robertugo2&repository=ha_rce&category=Integration)

You can install the plugin via HACS using the following steps

1. Open HACS
2. Click Integrations
3. Clik the three dots on the top right
4. Click "Custom repositories"
5. Add https://github.com/robertugo2/ha_rce/ and a category of your choice

# Configuration
All integration settings are available in the options in the integration configuration panel.
![image](https://github.com/user-attachments/assets/228cb8c6-c410-47a5-b0f6-41ddf82e2de4)

# Available components

### Sensor
* rynkowa_cena_energii_elektrycznej - current energy price

```
  attributes: 
    next_price - energy price in the next hour
    average - average daily energy price
    off_peak_1 - average energy price from 00:00 to 08:00
    off_peak_2 - average energy price from 20:00 to 00:00
    peak - average energy price from 08:00 to 20:00
    min_average - minimum average energy price in the range of x consecutive hours; where x is configurable in options
    unit - energy unit, default: kWh
    currency - default: PLN
    custom_peak - average energy price over the range of hours defined by custom_peak_range
    min - minimum daily energy price
    max - maximum daily energy price
    mean - median daily energy price
    custom_peak_range - configurable range of hours for which the custom_peak attribute is calculated
    low_price_cutoff - percentage of average price to set the low price attribute (low_price = hour_price < average * low_price_cutoff)
    use_cent - in case of PLN, true means that prices are in gr and if false in zloty
    tomorrow_valid - indicates, if tomorrow's prices were fetched sucessfully
    unit_of_measurement - currency / unit
    raw_today - today's hourly prices in the format
      - hour: 2024-06-28 00:00
        price: 604.2
        low_price: false
      - hour: 2024-06-28 01:00
        price: 488.93
        low_price: false
    raw_tomorrow - tomorrow's hourly prices
  ```

[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg
[latest_release]: https://github.com/robertugo2/ha_rce/releases/latest
[releases_shield]: https://img.shields.io/github/release/robertugo2/ha_rce.svg?style=popout
[releases]: https://github.com/robertugo2/ha_rce/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/robertugo2/ha_rce/total
[license-shield]: https://img.shields.io/github/license/robertugo2/ha_rce
[latest_commit]: https://img.shields.io/github/last-commit/robertugo2/ha_rce.svg?style=flat-square
[commits]: https://github.com/robertugo2/ha_rce/commits/master
