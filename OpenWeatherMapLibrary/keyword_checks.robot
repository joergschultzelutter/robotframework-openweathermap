*** Settings ***
Library						OpenWeatherMapLibrary.py
Library						OperatingSystem

Suite Setup	Get API Access Key

*** Variables ***

*** Test Cases ***
Latitude Getter Setter
	${VALUE1}=			Convert To Number	1.234	
	Set OpenWeatherMap Latitude	${VALUE1}	
	${VALUE2}=			Get OpenWeatherMap Latitude
	Should Be Equal			${VALUE1}	${VALUE2}

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
	${VALUE1}=			Convert To Number	51.0
	${VALUE2}=			Convert To Number	8.0
	${RESPONSE_CODE}  ${RESPONSE_BODY}=	Get Current Weather 	latitude=${VALUE1}	longitude=${VALUE2}	apikey=${APIKEY}    output_format=xml
	Log To Console	  ${RESPONSE_CODE}
	Log To Console	  ${RESPONSE_BODY}

Get OneCall Forecast Test
	${VALUE1}=			Convert To Number	51.0		
	${VALUE2}=			Convert To Number	8.0		
	${RESPONSE_CODE}  ${RESPONSE_BODY}=	Get OneCall Forecast	latitude=${VALUE1}	longitude=${VALUE2}	apikey=${APIKEY}
	Log To Console	  ${RESPONSE_CODE}
	Log To Console	  ${RESPONSE_BODY}

*** Keywords ***
Get API Access Key
	${APIKEY}=	Get Environment Variable	OWM_API_KEY
	Should Not Be Equal	${APIKEY}	${None}
	Set Suite Variable	${APIKEY}	${APIKEY}	
