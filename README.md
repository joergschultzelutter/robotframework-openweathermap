# robotframework-openweathermap

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![CodeQL](https://github.com/joergschultzelutter/robotframework-openweathermap/actions/workflows/codeql.yml/badge.svg)](https://github.com/joergschultzelutter/robotframework-openweathermap/actions/workflows/codeql.yml)

```robotframework-openweathermap``` is a [Robot Framework](https://www.robotframework.org) keyword collection for the [OpenWeatherMap](https://www.openweathermap.org/api) API.

## Installation

The easiest way is to install this package is from pypi:

    pip install robotframework-openweathermap

## Robot Framework Library Examples

Prerequisites:

The accompanying Robot Framework [test case](https://github.com/joergschultzelutter/robotframework-openweathermap/tests/library_checks.robot) relies on two requirements: 

- [get an OpenWeatherMap API key](https://home.openweathermap.org/users/sign_up) (it's free)
- create an environment variable ```OWM_API_KEY``` and assign the OpenWeatherMap API key to that variable

## Library usage and supported keywords

### Default settings 

The following rules apply:

- The default value for each parameter is ```None```
- Each parameter supports ```Getter``` and ```Setter``` keywords, e.g, ```Set OpenWeatherMap Latitude```
- Each OpenWeatherMap Keyword also permits the usage of these parameters. Example:

```robot
Get Current Weather latitude=....
```
- A keyword's parameter value has priority over the ```Setter``` value. This means that if you use ```Set OpenWeathermap Latitude  10``` and ```Get Current Weather  latitude=20```, the value will be ```20```  

### Options for setting the parameter values

You can either specify all parameters during the initial setup of the library or alternatively via separate keywords

#### Option 1 - set as position parameters

```robot
*** Settings ***

Library  OpenWeatherMapLibrary  12.0  34.0  ...

*** Test Cases ***
My first test case
```

#### Option 2 - set as named parameters

```robot
*** Settings ***

Library  OpenWeatherMapLibrary  latitude=12.0  longitude=34.0  ...

*** Test Cases ***
My first test case
```

#### Option 3 - Use Robot Keywords





### Generic Getter / Setter Robot Keywords supported by this library

You can use these optional Getter/Setter methods for setting your fixed default values. If you specify the same parameter as part of the actual API call, the value specified with that API call supersedes these generic values.


| Keyword  | Description | Arguments | Valid Values |
|----------|-------------|-----------|--------------|
| ``Get``/``Set OpenWeatherMap Latitude`` | Gets / Sets the latitude value        | ``latitude``  | float value |
| ``Get``/``Set OpenWeatherMap Longitude`` | Gets / Sets the longitude value        | ``longitude``  | float value |
| ``Get``/``Set OpenWeatherMap API Key`` | Gets / Sets the OWM API Key        | ``apikey``  | string |
| ``Get``/``Set OpenWeatherMap Number Of Results`` | Gets / Sets the max number of results  | ``number``  | integer > 0 |
| ``Get``/``Set OpenWeatherMap Language`` | Gets / Sets the desired output language        | ``language``  | see [OpenWeatherMap API](https://openweathermap.org/current#multi)<br />for valid values |
| ``Get``/``Set OpenWeatherMap Excludes`` | Gets / Sets the exclude(s) value.<br /> Separarate multiple values with a comma<br />See [API documentation](https://openweathermap.org/api/one-call-api) for details        | ``exclude``  | ``current``<br />``minutely``<br />``hourly``<br />``daily``<br />``alerts`` |
| ``Get``/``Set OpenWeatherMap Output Format`` | Gets / Sets the output format (e.g. ``json``)        | ``output_format``  | ``json``<br />``xml``<br />``html``
| ``Get``/``Set OpenWeatherMap Unit Format`` | Gets / Sets the unit format<br />See [API Documentation](https://openweathermap.org/api/one-call-api#data) for details<br />Format availability depends on API call | ``unit_format``  | ``standard``<br />``metric``<br >``imperial`` |
| ``Get``/``Set OpenWeatherMap Datetime Start`` | Gets / Sets the start datetime for date ranges        | ``dt_start``  | Unix timestamp |
| ``Get``/``Set OpenWeatherMap Datetime End`` | Gets / Sets the end datetime for date ranges        | ``dt_end``  | Unix timestamp |
| ``Get``/``Set OpenWeatherMap Datetime`` | Gets / Sets a single point in time        | ``dt``  | Unix Timestamp |

## OpenWeatherMap Keywords

Please note that some of these keywords require a paid OpenWeatherMap subscription.

| Keyword | Description | Mandatory<br />parameters | Optional<br />parameters | Comments |
| ------- | ----------- | -------------------- | ------------------- | -------- |
| [Get Current Weather](https://openweathermap.org/current) | Access current weather data for any location on<br /> Earth including over 200,000 cities | ``latitude``<br />``longitude``<br />``apikey``|``output_format``<br />``unit_format``<br />``language`` | | 

## Known issues

