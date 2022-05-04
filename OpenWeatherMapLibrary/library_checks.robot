*** Settings ***
Library						OpenWeatherMapLibrary.py

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






