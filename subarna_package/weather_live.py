import requests, json 
import pandas as pd

def weather_detect():

	api_key = "045dcf2677cd5451ba72c08e8fdda98c"
  

	base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
 
	city_name = input("Enter city name : ") 
  
 
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  

	response = requests.get(complete_url) 
  

	x = response.json() 
  
	
	if x["cod"] != "404": 
  
    
		y = x["main"] 
  
   
		current_temperature = y["temp"] 
  
    
		current_pressure = y["pressure"] 
  
    
		current_humidiy = y["humidity"] 
  
    
		z = x["weather"] 
  
    
		weather_description = z[0]["description"] 
  
    
		print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
			"\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
			"\n humidity (in percentage) = " +
                    str(current_humidiy) +
			"\n description = " +
                    str(weather_description)) 
  
	else:
    
		print(" City Not Found ") 
    
todays_date=10192019
import datetime
todays_date=pd.to_datetime(todays_date)
