
from flask import Flask, render_template, request 
import requests
# import json to load JSON data to a python dictionary 
  
# urllib.request to make a request to api 
import urllib.request 
  
  
app= Flask(__name__) 
  
@app.route('/', methods =['POST', 'GET']) 
def weather(): 
    if request.method == 'POST': 
        city = request.form['city'] 
    else: 
        # for default name mathura 
        city = 'Vellore'
  
    # your API key will come here 
    api = '045dcf2677cd5451ba72c08e8fdda98c' 
  
    # source contain json data from api 
    #source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q =' + city + '&appid =' + api).read() 
    base_url='http://api.openweathermap.org/data/2.5/weather?q ='
    complete_url = base_url + "appid=" + api+ "&q=" + city
    source=complete_url
    response = requests.get(source) 
    # converting JSON data to a dictionary 
    list_of_data=response.json()
  
    # data for variable list_of_data 
    if list_of_data["cod"]!=404:
        y=list_of_data['main']
        data={
            "Current_Temperature":y['temp'],
            "Current_Pressure":y["pressure"],
            "Current_Humidity":y["humidity"],
            "z":x["weather"],
            "Weather_description":x["weather"][0]["description"]
        }
        
    return render_template('index.html', data = data) 
  
  
app.run(debug = True)
weather()
 
