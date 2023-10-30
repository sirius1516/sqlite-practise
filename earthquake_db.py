import requests
import sqlite3

def save_earthquake(equake_list):
    conn = sqlite3.connect('earthquake_db.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE earthquakes (place TEXT, magnitue REAL)')
    cursor.executemany('INSERT INTO earthquakes VALUES (?, ?)', equake_list)
    conn.commit()
    conn.close()


def select_earthquake():
    conn = sqlite3.connect('earthquake_db.db')
    cursor = conn.cursor()
    cursor.executemany('SELECT * FROM earthquakes')
    data = cursor.fetchall()
    [print(row) for row in data]
    conn.commit()
    conn.close()



url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
start_time = input('Enter start time yyyy-mm-dd: ')
end_time = input('Enter end time yyyy-mm-dd: ')
latitude = input('Enter latitude: ')
longitude = input('Enter longitude: ')
maxradius_km = input('Enter max radius in km: ')
min_magnitude = input('Enter min magnitude: ')

response = requests.get(url, headers={'Accept': 'application/json'},
                        params={
                            'format': 'geojson',
                            'starttime': start_time,
                            'endtime': end_time,
                            'latitude': latitude,
                            'longitude': longitude,
                            'maxradiuskm': maxradius_km,
                            'minmagnitude': min_magnitude
                        })
data = response.json()
earthquake_list = data['features']
equake_list = []
count = 0
for earthquake in earthquake_list:
    count += 1
    # print(f"{count}. Place: {earthquake['properties']['place']} "
    #       f"- Magnitude: {earthquake['properties']['mag']}")
    equake_list.append((earthquake['properties']['place'], earthquake['properties']['mag']))


# save_earthquake(equake_list)
select_earthquake()