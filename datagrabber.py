import wikipedia, glob, requests, json, geocoder
class DataGrabber():
    def __init__(self, city=None):
        self.city = city


    def get_geoname_data(self, city_string=""):
        geoname_obj = geocoder.geonames(city_string, key="meatcomputer")
        if 'ERROR' in geoname_obj.status:
            return "problem"
        return geoname_obj.geojson


    def get_weather(self):
        url = "api.openweathermap.org/data/2.5/weather?lat="+self.city.lat+"&lon="+self.city.lng
        response = requests.get(url)
        return response
        
