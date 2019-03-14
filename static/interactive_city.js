var image_url=""
var city_info={}
var mymap = L.map('mapid', {zoomControl: false})
L.control.scale({maxWidth: 200}).addTo(mymap);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWVhdGNvbXB1dGVyIiwiYSI6ImNqcm9keHdseDEyajI0NHRrNm15OHFvd3cifQ.VhqpdUXjGxSlUK9bgeFP3g', {
//	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	id: 'mapbox.streets',
}).addTo(mymap);



var mapModule = (function () {
	var zoom_level = 16; // Private Variable
	var pub = {};// public object - returned at end of module
	pub.changeZoom = function () {
		if(zoom_level > 8 ){
			mymap.setZoom(zoom_level)
			zoom_level = zoom_level - 1;
		}else{
			zoom_level = 16
		}
	};

	pub.changePosition = function(city_data) {
		mymap.setView([city_data.lat, city_data.lng, zoom_level])
		var marker = L.marker([city_data.lat, city_data.lng]).addTo(mymap);
	}

	return pub; // expose externally
}());

function updateInfo(city_data){
	if(Object.entries(city_data).length === 0){
		document.getElementById("primary_stats").innerHTML = "loading"
	}else{
		document.getElementById("primary_stats").innerHTML = city_data.name + ", "+ city_data.sub_country+ ", "+ city_data.country_name  
		document.getElementById("seconday_stats").innerHTML = "Weather: "+ city_data.weather + "<br>Temperature: "+city_data.temperature + "<br>LAT: "+city_data.lat+"<br> LNG: "+city_data.lng
	}
}

function httpGetAsync(theUrl, callback)
{
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function() { 
		if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
			callback(xmlHttp.responseText);
	}
	xmlHttp.open("GET", theUrl, true); // true for asynchronous 
	xmlHttp.send(null);
}

function newUrl(){
	httpGetAsync("/city_url", function(response){
		image_url=response;
	});
}


function updateCityData(){
	httpGetAsync("/current_city_data", function(response){
		city_info=JSON.parse(response)
		console.log("new city")
		updateInfo(city_info)
		mapModule.changePosition(city_info)
	});
}

function newCity(){
	httpGetAsync("/new_city", function(response){
		city_info=JSON.parse(response)
		console.log("new city")
		updateInfo(city_info)
		mapModule.changePosition(city_info)

	});
}
newCity();
setInterval(newCity, 2000000);
setInterval(mapModule.changeZoom, 30000);
setInterval(updateCityData, 30000);
