#!/opt/local/bin/python3
#
# Robot Framework Keyword library wrapper for
# OpenWeatherMap API
# Author: Joerg Schultze-Lutter, 2022
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from robot.api.deco import library, keyword

import re
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(module)s -%(levelname)s- %(message)s"
)
logger = logging.getLogger(__name__)

__version__ = "0.1.0"
__author__ = "Joerg Schultze-Lutter"


@library(scope="GLOBAL", auto_keywords=True)
class OpenWeatherMapLibrary:
    # These are our default parameter settings
    # Change these settings if you e.g. prefer to use
    # a different APRS-IS server
    # Dependent on the APRS Server that you want to
    # connect with, read-only access via N0CALL may not work
    # at all & you will receive connection errors when
    # trying to do so.
    DEFAULT_LATITUDE = 0.0
    DEFAULT_LONGITUDE = 0.0
    DEFAULT_APIKEY = None
    DEFAULT_FORMAT = "json"
    DEFAULT_UNIT = "standard"
    DEFAULT_LANG = None
    DEFAULT_EXCLUDE = None
    DEFAULT_NUMBER_OF_RESULTS = None

    # Class-internal parameters
    __owm_latitude = None
    __owm_longitude = None
    __owm_apikey = None
    __owm_format = None
    __owm_unit = None
    __owm_lang = None
    __owm_exclude = None
    __owm_number = None

    def __init__(
            self,
            owm_latitude: float = DEFAULT_LATITUDE,
            owm_longitude: float = DEFAULT_LONGITUDE,
            owm_apikey: str = DEFAULT_APIKEY,
            own_format: str = DEFAULT_FORMAT,
            owm_unit: str = DEFAULT_UNIT,
            owm_lang: str = DEFAULT_LANG,
            owm_exclude: str = DEFAULT_EXCLUDE,
            owm_number: int = DEFAULT_NUMBER_OF_RESULTS,
    ):
        self.__owm_latitude = owm_latitude
        self.__owm_longitude = owm_longitude
        self.__owm_apikey = owm_apikey
        self.__owm_number = owm_number
        self.__owm_lang = owm_lang
        self.__owm_exclude = owm_exclude
        self.__owm_format = own_format
        self.__owm_unit = owm_unit

    # Python "Getter" methods
    #
    # Note that adding a Robot decorator (@keyword) will not
    # cause an error but the keyword will not be recognized later on
    # Therefore, Robot-specific "getter" keywords are required
    @property
    def owm_latitude(self):
        return self.__owm_latitude

    @property
    def owm_longitude(self):
        return self.__owm_longitude

    @property
    def owm_apikey(self):
        return self.__owm_apikey

    @property
    def owm_number(self):
        return self.__owm_number

    @property
    def owm_lang(self):
        return self.__owm_lang

    @property
    def owm_exclude(self):
        return self.__owm_exclude

    @property
    def owm_format(self):
        return self.__owm_format

    @property
    def owm_unit(self):
        return self.__owm_unit

    # Python "Setter" methods
    #
    # Note that adding a Robot decorator (@keyword) will not
    # cause an error but the keyword will not be recognized later on
    # Therefore, Robot-specific "setter" keywords are required

    @owm_latitude.setter
    def owm_latitude(self, owm_latitude: float):
        if not owm_latitude:
            raise ValueError("No latitude value has been specified")
        self.__owm_latitude = owm_latitude

    @owm_longitude.setter
    def owm_longitude(self, owm_longitude: float):
        if not owm_longitude:
            raise ValueError("No longitude value has been specified")
        self.__owm_longitude = owm_longitude

    @owm_apikey.setter
    def owm_apikey(self, owm_apikey: str):
        if not owm_apikey:
            raise ValueError("No API-Key value has been specified")
        self.__owm_apikey = owm_apikey

    @owm_number.setter
    def owm_number(self, owm_number: int):
        if not owm_number:
            raise ValueError("No Number of Results value has been specified")
        self.__owm_number = owm_number

    @owm_lang.setter
    def owm_lang(self, owm_lang: str):
        if not owm_lang:
            raise ValueError("No lang value has been specified")
        self.__owm_lang = owm_lang

    @owm_exclude.setter
    def owm_exclude(self, owm_exclude: str):
        if not owm_exclude:
            raise ValueError("No exclude value has been specified")
        self.__owm_exclude = owm_exclude

    @owm_format.setter
    def owm_format(self, owm_format: str):
        if not owm_format:
            raise ValueError("No output format value has been specified")
        self.__owm_format = owm_format

    @owm_unit.setter
    def owm_unit(self, owm_unit: str):
        if not owm_unit:
            raise ValueError("No unit of measure value has been specified")
        self.__owm_unit = owm_unit

    #
    # Robot-specific "getter" keywords
    #
    @keyword("Get OpenWeatherMap Latitude")
    def get_owm_latitude(self):
        return self.owm_latitude

    @keyword("Get OpenWeatherMap Longitude")
    def get_owm_longitude(self):
        return self.owm_longitude

    @keyword("Get OpenWeatherMap API Key")
    def get_owm_apikey(self):
        return self.owm_apikey

    @keyword("Get OpenWeatherMap Number Of Results")
    def get_owm_number(self):
        return self.owm_number

    @keyword("Get OpenWeatherMap Language")
    def get_owm_lang(self):
        return self.owm_lang

    @keyword("Get OpenWeatherMap Excludes")
    def get_owm_exclude(self):
        return self.owm_exclude

    @keyword("Get OpenWeatherMap Output Format")
    def get_owm_format(self):
        return self.owm_format

    @keyword("Get OpenWeatherMap Unit Format")
    def get_owm_unit(self):
        return self.owm_unit

    #
    # Robot-specific "setter" keywords
    #
    @keyword("Set OpenWeatherMap Latitude")
    def set_owm_latitude(self, owm_latitude: float = None):
        logger.debug(msg="Setting OWM Latitude")
        self.owm_latitude = owm_latitude

    @keyword("Set OpenWeatherMap Longitude")
    def set_owm_longitude(self, owm_longitude: float = None):
        logger.debug(msg="Setting OWM Longitude")
        self.owm_longitude = owm_longitude

    @keyword("Set OpenWeatherMap API Key")
    def set_owm_apikey(self, owm_apikey: str = None):
        logger.debug(msg="Setting OWM API Key")
        self.owm_apikey = owm_apikey

    @keyword("Set OpenWeatherMap Number Of Results")
    def set_owm_number(self, owm_number: int = None):
        logger.debug(msg="Setting OWM Number Of Results")
        self.owm_number = owm_number

    @keyword("Set OpenWeatherMap Language")
    def set_owm_lang(self, owm_lang: str = None):
        logger.debug(msg="Setting OWM Language")
        self.owm_lang = owm_lang

    @keyword("Set OpenWeatherMap Excludes")
    def set_owm_excludes(self, owm_exclude: str = None):
        logger.debug(msg="Setting OWM Excludes")
        self.owm_exclude = owm_exclude

    @keyword("Set OpenWeatherMap Output Format")
    def set_owm_lang(self, owm_format: str = None):
        logger.debug(msg="Setting OWM Output Format")
        self.owm_format = owm_format

    @keyword("Set OpenWeatherMap Unit Format")
    def set_owm_unit(self, owm_unit: str = None):
        logger.debug(msg="Setting OWM Unit")
        self.owm_unit = owm_unit

    #
    # Robot Framework Action Keywords for OpenWeatherMap
    #
    @keyword("Get Current Weather")
    def get_current_weather(self, latitude: float = None, longitude: float = None, apikey: float = None):
        __pro_api = False
        pass

    @keyword("Get Hourly Forecasts Four Days")
    def get_hourly_forecasts_four_days(self,latitude: float = None, longitude: float = None, apikey: float = None, format: str = None, number: int = None, lang: str=None):
        __pro_api = True
        pass

    @keyword("Get OneCall Forecast")
    def get_onecall_forecast(self,latitude: float = None, longitude: float = None, apikey: float = None, exclude: str = None, unit: str = None, lang: str=None):
        __pro_api = False
        pass

    @keyword("Get Daily Forecasts 16 Days")
    def get_daily_forecasts_16_days(self,latitude: float = None, longitude: float = None, apikey: float = None, number: int = None, format: str = None, unit: str = None, lang: str=None):
        __pro_api = False
        pass

    @keyword("Get Climatic Forecast 30 Days")
    def get_climatic_forecast_30_days(self, latitude: float = None, longitude: float = None, apikey: float = None, number: int = None, format: str = None, unit: str = None, lang: str=None):
        __pro_api = True
        pass

    @keyword("Get Current Solar Radiation")
    def get_current_solar_radiation(self, latitude: float = None, longitude: float = None, apikey: float = None):
        __pro_api = False
        pass

    @keyword("Get Solar Radiation Forecast")
    def get_solar_radiation_forecast(self, latitude: float = None, longitude: float = None, apikey: float = None):
        __pro_api = False
        pass

    @keyword("Get 5 Day 3 Hour Forecast")
    def get_5_day_3_hour_forecast(self, latitude: float = None, longitude: float = None, apikey: float = None, number: int = None, format: str = None, unit: str = None, lang: str=None):
        __pro_api = False
        pass

    @keyword("Get Air Pollution Data")
    def get_air_pollution_data(self, latitude: float = None, longitude: float = None, apikey: float = None):
        __pro_api = False
        pass


if __name__ == "__main__":
    pass
