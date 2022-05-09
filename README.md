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





### Action Robot Keywords supported by this library

| Keyword  | Description | Arguments |
|----------|-------------|-----------|
| ``abcd`` | efgh        | ``ijkl``  |

## Known issues

