from staticmap import StaticMap, CircleMarker
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
import sys, json, random, os 

font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-BoldOblique.ttf", 20)
font2 = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-BoldOblique.ttf", 21)

with open('../cities.json') as f:
    cities = json.load(f)

tk_instance=tk.Tk()
screen_width = tk_instance.winfo_screenwidth()
screen_height = tk_instance.winfo_screenheight()
pip_image_width = 300 
pip_image_height = 200

random_city = cities[random.randint(0,len(cities))]
random_city_name = random_city['name']
random_city_country = random_city['country']
tile_url="https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey=125aa6ccc74f432ea81716925aa374ca"

unrendered_map=StaticMap(screen_width, screen_height, 200,200, url_template=tile_url)
tiny_map=StaticMap(pip_image_width, pip_image_height, 0, 0, url_template=tile_url)

def add_markers(chosen_map, zoom_level):
    marker=CircleMarker((float(random_city['lng']), float(random_city['lat'])), 'black', 5)
    marker2=CircleMarker((float(random_city['lng'])+zoom_level, float(random_city['lat'])+zoom_level), 'black', 0)
    marker3=CircleMarker((float(random_city['lng'])-zoom_level, float(random_city['lat'])-zoom_level), 'black', 0)
    chosen_map.add_marker(marker)
    chosen_map.add_marker(marker2)
    chosen_map.add_marker(marker3)

add_markers(unrendered_map,0.02) 
add_markers(tiny_map,2)

def save_map(map_to_save, name, tiny_map):
    path_str="./thecityof%smap.jpg" % name 
    tmp_str ="/tmp/Thumb.jpg" 
    ready_map = map_to_save.render()
    ready_map.save(path_str)
    small_map = tiny_map.render()
    small_map.save(tmp_str)

    img = Image.open(path_str)
    pip_img = Image.open(tmp_str)
    draw = ImageDraw.Draw(img)

    x=100
    y=100
    shadow_color=(255,255,255) 
    text=random_city_name+", "+random_city_country
    draw.text((x-1, y-1), text, font=font, fill=shadow_color)
    draw.text((x+1, y-1), text, font=font, fill=shadow_color)
    draw.text((x-1, y+1), text, font=font, fill=shadow_color)
    draw.text((x+1, y+1), text, font=font, fill=shadow_color)
    draw.text((x,y), text, (0,0,0),font=font)
    draw.rectangle([95,495, 105+pip_image_width, 505+pip_image_height], fill=(0,0,0))
    img.paste(pip_img, (100,500))
    print("saving")
    img.save(path_str)
    os.system("nitrogen --set-auto  %s" % path_str)
    
save_map(unrendered_map, random_city_name, tiny_map)
