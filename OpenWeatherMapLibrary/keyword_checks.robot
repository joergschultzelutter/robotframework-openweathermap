*** Settings ***
Library			OpenWeatherMapLibrary.py
Library			OperatingSystem

Suite Setup     Run My Suite Setup Tasks

*** Variables ***

*** Test Cases ***
Latitude Getter Setter
	${VALUE1}=  Convert To Number	1.234
	Set OpenWeatherMap Latitude	    ${VALUE1}
	${VALUE2}=	Get OpenWeatherMap Latitude
	Should Be Equal	${VALUE1}	${VALUE2}

Longitude Getter Setter
	${VALUE1}=			Convert To Number	5.678	
	Set OpenWeatherMap Longitude 	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap Longitude
	Should Be Equal			${VALUE1}	${VALUE2}

API Key Getter Setter
	Set Local Variable		${VALUE1}	myAPIKey
	Set OpenWeatherMap API Key 	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap API Key
	Should Be Equal			${VALUE1}	${VALUE2}

Number Of Results Getter Setter
	${VALUE1}=			Convert To Integer	1234
	Set OpenWeatherMap Number Of Results	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap Number Of Results
	Should Be Equal			${VALUE1}	${VALUE2}

Excludes Getter Setter
	Set Local Variable		${VALUE1}	hourly,daily
	Set OpenWeatherMap Excludes 	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap Excludes
	Should Be Equal			${VALUE1}	${VALUE2}

Output Format Getter Setter
	Set Local Variable		${VALUE1}	json
	Set OpenWeatherMap Output Format	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap Output Format
	Should Be Equal			${VALUE1}	${VALUE2}

Unit Format Getter Setter
	Set Local Variable		${VALUE1}	metric
	Set OpenWeatherMap Unit Format	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap Unit Format
	Should Be Equal			${VALUE1}	${VALUE2}

Language Getter Setter
	Set Local Variable		${VALUE1}	de	
	Set OpenWeatherMap Language	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap Language
	Should Be Equal			${VALUE1}	${VALUE2}

Datetime Start Getter Setter
	${VALUE1}=			Convert To Number	1234	
	Set OpenWeatherMap Datetime Start	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap Datetime Start
	Should Be Equal			${VALUE1}	${VALUE2}

Datetime End Getter Setter
	${VALUE1}=			Convert To Number	5678	
	Set OpenWeatherMap Datetime End	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap Datetime End
	Should Be Equal			${VALUE1}	${VALUE2}

Datetime Getter Setter
	${VALUE1}=			Convert To Number	9012	
	Set OpenWeatherMap Datetime	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap Datetime
	Should Be Equal			${VALUE1}	${VALUE2}

Get Current Weather Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Current Weather 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get Hourly Forecast 4 Days Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Hourly Forecast 4 Days 	latitude=${LON}     longitude=${LAT}	apikey=${APIKEY}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get OneCall Forecast Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get OneCall Forecast	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get Daily Forecasts 16 Days Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Daily Forecasts 16 Days 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get Climatic Forecast 30 Days Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Climatic Forecast 30 Days 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get Current Solar Radiation Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Current Solar Radiation 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get Solar Radiation Forecast Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Solar Radiation Forecast 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get Solar Radiation History Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Solar Radiation History 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}    dt_start=${DT_START}   dt_end=${DT_END}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get 5 Day 3 Hour Forecast Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get 5 Day 3 Hour Forecast 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get Current Air Pollution Data Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Current Air Pollution Data 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get Air Pollution Data Forecast Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Air Pollution Data Forecast 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get Air Pollution Data History Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Air Pollution Data History 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}    dt_start=${DT_START}   dt_end=${DT_END}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

Get Road Risk Data Test
	${RESPONSE_CODE}    ${RESPONSE_BODY}=	Get Road Risk Data 	latitude=${LAT}     longitude=${LON}	apikey=${APIKEY}    dt=${DT_START}
	Log To Console	    ${RESPONSE_CODE}
	Log To Console	    ${RESPONSE_BODY}

*** Keywords ***
Run My Suite Setup Tasks
    Get API Access Key
    Define My Test Variables

Get API Access Key
	${APIKEY}=	Get Environment Variable	OWM_API_KEY
	Should Not Be Equal	${APIKEY}	${None}
	Set Suite Variable	${APIKEY}	${APIKEY}	

Define My Test Variables
    # Create my lat/lon default set ....
    ${LAT}=                 Convert To Number       51.82798
    ${LON}=                 Convert To Number       9.4455

    # ... and elevate it to Global status
    Set Global Variable     ${LAT}                  ${LAT}
    Set Global Variable     ${LON}                  ${LON}

    # Create a start/Stop datetime set ....
    ${DT_START}=            Convert To Integer      1648771200
    ${DT_END}=              Convert To Integer      1651363199

    # ... and elevate it to Global status
    Set Global Variable      ${DT_START}            ${DT_START}
    Set Global Variable      ${DT_END}              ${DT_END}
