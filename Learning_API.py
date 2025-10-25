import tkinter as tk  
from tkinter import ttk ,messagebox
import requests

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("420x260")
        self.resizable(False , False)

        #city input
        frm = ttk.Frame(self,padding = 12)
        frm.pack(fill="both",expand =True)

        ttk.Label(frm, text="City:").grid(row = 0 , column = 0, sticky = "w")
        self.city_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.city_var,width=28).grid(row = 0 , column =1 , sticky ="we" , padx=(6,0))


        #units selector 
        ttk.Label(frm,text="Units:").grid(row = 0 , column =2 , padx = (12,0))
        self.units_var = tk.StringVar(value="metric")
        units_cb = ttk.Combobox(frm, textvariable = self.units_var, values =["metric" , "imperial"], width = 10 , state = "readonly")
        units_cb.grid(row = 0, column = 3 , padx = (6,0))

        self.btn = ttk.Button(frm, text = "Get Weather" ,command = self.on_get_weather)
        self.btn.grid(row = 0 , column = 4 , padx = (12,0))

        #output area

        ttk.Separator(frm).grid(row = 1, column = 0 , columnspan=5, sticky="ew", pady=10)
        self.status_var = tk.StringVar(value= "Enter a city and click Get Weather.")
        ttk.Label(frm,textvariable = self.status_var, anchor = "w" , justify= "left").grid(row = 2, column = 0 , columnspan =5,sticky ="we")


        for c in range(5):
            frm.grid_columnconfigure(c,weight = 0)
        frm.grid_columnconfigure(1, weight =1)
    
    def _geocode_city(self,city:str):
           """Return (lat,lon,display name) or None if not found. """
           url = "https://geocoding-api.open-meteo.com/v1/search"
           params = {"name" : city , "count" : 1, "language" : "en" , "format" : "json"}
           r = requests.get(url,params = params , timeout = 10)
           r.raise_for_status()
           data = r.json()
           results = data.get("results")
           if not results :
                  return None
           first = results[0]
           lat = first["latitude"]
           lon = first["longtitude"]
           label = f'{first["name"]},{ first.get("country","")}'.strip().strip(",")
           return lat, lon, label 

    def _weathercode_text(self, code: int) -> str:
        """Map Open-Meteo weathercode to a human description."""
        mapping = {
            0:"Clear sky", 1:"Mainly clear", 2:"Partly cloudy", 3:"Overcast",
            45:"Fog", 48:"Depositing rime fog",
            51:"Light drizzle", 53:"Moderate drizzle", 55:"Dense drizzle",
            56:"Light freezing drizzle", 57:"Dense freezing drizzle",
            61:"Slight rain", 63:"Moderate rain", 65:"Heavy rain",
            66:"Light freezing rain", 67:"Heavy freezing rain",
            71:"Slight snow", 73:"Moderate snow", 75:"Heavy snow",
            77:"Snow grains",
            80:"Slight rain showers", 81:"Moderate rain showers", 82:"Violent rain showers",
            85:"Slight snow showers", 86:"Heavy snow showers",
            95:"Thunderstorm", 96:"Thunderstorm with slight hail", 97:"Thunderstorm with slight hail",
            99:"Thunderstorm with heavy hail"
        }
        return mapping.get(int(code), f"Code {code}")

    def _fetch_current_weather(self,lat:float, lon : float ):
          # return dict with temperature C, wind and weather code.
          url = "https://api.open-meteo.com/v1/forecast"
          params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "weather_code", "wind_speed_10m"],
            "timezone": "auto",
        }
          
          r = requests.get(url, params=params, timeout=10)
          r.raise_for_status()
          data = r.json()
          current = data.get("current", {})
          return{
                            "temp_c": current.get("temperature_2m"),
            "code": current.get("weather_code"),
            "wind": current.get("wind_speed_10m"),
          }

          
           


        #button function
    def on_get_weather(self):
            city = self.city_var.get().strip()
            if not city:
                messagebox.showwarning("Missing City", "Please enter a city name")
                return
            self.btn.configure(state ="disabled")
        
                  

if __name__ == "__main__":
                app = WeatherApp()
                app.mainloop()