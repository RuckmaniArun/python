import os
import streamlit as st
import requests

def collect_mintemp_maxtemp(query):
	

	url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=1&appid=5809bf6b396188a3f9c44f9393edb6b3"

	# Collect Latitude, Longitude data

	response = requests.get(url)
	response = response.json()
	print("Latitude, Longitude JSON response data...",response)

	lat,lng = None, None
	if response:
		lat,lng = response[0]['lat'], response[0]['lon']


	# Collect Weather data


	if lat and lng:
		weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=5809bf6b396188a3f9c44f9393edb6b3&units=metric"
		response = requests.get(weather_url)
		data = response.json()
		
		print(data)
		min_temp = data["main"]["temp_min"]
		max_temp = data["main"]["temp_max"]
		print(f"Temperature in {query} is Min: {min_temp}, Max:{max_temp}")
	return min_temp, max_temp



st.set_page_config(
    # Title and icon for the browser's tab bar:
    page_title="Weather For Any City",
    page_icon="🌦️",
    # Make the content take up the width of the page:
    layout="wide",
)





city = st.text_input("City Name : ")
if st.button("Get Weather"):
	min_temp, max_temp = collect_mintemp_maxtemp(city)
	st.success("Weather data successfully fetched")
	st.write(f"Temperature in {city} is Min: {min_temp}, Max:{max_temp}")