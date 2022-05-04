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
    # at all and you will receive connection errors when
    # trying to do so.
    DEFAULT_LATITUDE = 0.0
    DEFAULT_LONGITUDE = 0.0
    DEFAULT_APPID = None
    DEFAULT_MODE = "json"
    DEFAULT_UNIT = "standard"
    DEFAULT_LANG = None
    DEFAULT_EXCLUDE = None
    DEFAULT_CNT = None

    # Class-internal parameters
    __owm_latitude = None
    __owm_longitude = None
    __owm_appid = None
    __owm_mode = None
    __owm_unit = None
    __owm_lang = None
    __owm_exclude = None
    __owm_cnt = None

    def __init__(
            self,
            owm_latitude: float = DEFAULT_LATITUDE,
            owm_longitude: float = DEFAULT_LONGITUDE,
            owm_appid: str = DEFAULT_APPID,
            own_mode: str = DEFAULT_MODE,
            owm_unit: str = DEFAULT_UNIT,
            owm_lang: str = DEFAULT_LANG,
            owm_exclude: str = DEFAULT_EXCLUDE,
            owm_cnt: int = DEFAULT_CNT,
    ):
        self.__owm_latitude = owm_latitude
        self.__owm_longitude = owm_longitude
        self.__owm_appid = owm_appid
        self.__owm_cnt = owm_cnt
        self.__owm_lang = owm_lang
        self.__owm_exclude = owm_exclude
        self.__owm_mode = own_mode
        self.__owm_unit = owm_unit

    # Python "Getter" methods
    #
    # Note that adding an additional Robot decorator (@keyword) will not
    # cause an error but the keyword will not be recognized later on
    # Therefore, Robot-specific "getter" keywords are required
    @property
    def owm_latitude(self):
        return self.__owm_latitude

    @property
    def owm_longitude(self):
        return self.__owm_longitude

    @property
    def owm_appid(self):
        return self.__owm_appid

    @property
    def owm_cnt(self):
        return self.__owm_cnt

    @property
    def owm_lang(self):
        return self.__owm_lang

    @property
    def owm_exclude(self):
        return self.__owm_exclude

    @property
    def owm_mode(self):
        return self.__owm_mode

    @property
    def owm_unit(self):
        return self.__owm_unit

    # Python "Setter" methods
    #
    # Note that adding an additional Robot decorator (@keyword) will not
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

    @owm_appid.setter
    def owm_appid(self, owm_appid: str):
        if not owm_appid:
            raise ValueError("No appid value has been specified")
        self.__owm_appid = owm_appid

    @owm_cnt.setter
    def owm_cnt(self, owm_cnt: int):
        if not owm_cnt:
            raise ValueError("No cnt value has been specified")
        self.__owm_cnt = owm_cnt

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

    @owm_mode.setter
    def owm_mode(self, owm_mode: str):
        if not owm_mode:
            raise ValueError("No mode value has been specified")
        self.__owm_mode = owm_mode

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

    @keyword("Get OpenWeatherMap AppID")
    def get_owm_appid(self):
        return self.owm_appid

    @keyword("Get OpenWeatherMap Cnt")
    def get_owm_cnt(self):
        return self.owm_cnt

    @keyword("Get OpenWeatherMap Language")
    def get_owm_lang(self):
        return self.owm_lang

    @keyword("Get OpenWeatherMap Excludes")
    def get_owm_exclude(self):
        return self.owm_exclude

    @keyword("Get OpenWeatherMap Data Format")
    def get_owm_mode(self):
        return self.owm_mode

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

    @keyword("Set OpenWeatherMap AppID")
    def set_owm_appid(self, owm_appid: str = None):
        logger.debug(msg="Setting OWM AppId")
        self.owm_appid = owm_appid

    @keyword("Set OpenWeatherMap Cnt")
    def set_owm_cnt(self, owm_cnt: int = None):
        logger.debug(msg="Setting OWM Cnt")
        self.owm_cnt = owm_cnt

    @keyword("Set OpenWeatherMap Language")
    def set_owm_lang(self, owm_lang: str = None):
        logger.debug(msg="Setting OWM Language")
        self.owm_lang = owm_lang

    @keyword("Set OpenWeatherMap Excludes")
    def set_owm_excludes(self, owm_exclude: str = None):
        logger.debug(msg="Setting OWM Excludes")
        self.owm_exclude = owm_exclude

    @keyword("Set OpenWeatherMap Data Format")
    def set_owm_lang(self, owm_mode: str = None):
        logger.debug(msg="Setting OWM Mode")
        self.owm_mode = owm_mode

    @keyword("Set OpenWeatherMap Unit Format")
    def set_owm_unit(self, owm_unit: str = None):
        logger.debug(msg="Setting OWM Unit")
        self.owm_unit = owm_unit


if __name__ == "__main__":
    pass
