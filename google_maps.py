#Directions API
import urllib.request
import json
import re

maps_endpoint = "https://maps.googleapis.com/maps/api/directions/json?"
address_endpoint = 'https://maps.googleapis.com/maps/api/geocode/json?'
api_key = <YOUR API KEY HERE>
def ask_user():
    origin = re.sub(' +','+', input('Where are you?'))
    #origin = '158+Golfview+Ave,+Toronto'
    destination = re.sub(' +','+',input('Where do you want to go?').replace(r' +', '+'))
    #destination = '111+Quail+Feather+Crescent,+Brampton'
    mode = 'transit' #Bus routes
    nav_request = 'origin={}&destination={}&mode={}&key={}'.format(origin, destination, mode, api_key)
    return maps_endpoint+nav_request

def parse_transit(dict):
    arrival_stop = dict['arrival_stop']['name']
    arrival_time = dict['arrival_time']['text']
    departure_stop = dict['departure_stop']['name']
    departure_time = dict['departure_time']['text']
    bus_stops = dict['num_stops']
    bus_name = dict['line']['name']+' '+dict['line']['short_name']
    summary = f"{bus_name} departs from {departure_stop} at {departure_time}. Arrives in {arrival_stop} at {arrival_time } after {bus_stops} stops."
    return summary

try:
    request = ask_user()

    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)

    total_distance = directions['routes'][0]['legs'][0]["distance"]["text"]
    total_duration = directions['routes'][0]['legs'][0]["duration"]["text"]
    start_location = directions['routes'][0]['legs'][0]["start_address"]
    end_location = directions['routes'][0]['legs'][0]["end_address"]

    summary = f"START LOCATION : {start_location}\n\
    END LOCATION : {end_location}\n\
    TOTAL DISTANCE : {total_distance}\n\
    TOTAL DURATION : {total_duration}\n\
    ------------------------------------------------------------------\n\n"

    steps_array = directions['routes'][0]['legs'][0]['steps']

    for index, step in enumerate(steps_array):
        
        summary += f"Step {index}: {re.sub('<[^<]+?>', '', step['html_instructions'])}\n"
        start =    step['start_location']
        stop = step['end_location']
        distance = step['distance']
        if step.get('transit_details', None):
            parse_transit(step['transit_details'])
            summary += f"It takes {step['duration']['text']}\n"
        else:
            start_latlng = f"latlng={start['lat']},{start['lng']}&key={api_key}"
            stop_latlng = f"latlng={stop['lat']},{stop['lng']}&key={api_key}"
            answer_start = ','.join(json.loads(urllib.request.urlopen(address_endpoint+start_latlng).read())["results"][0]['formatted_address'].split(',')[:2])
            answer_stop = ','.join(json.loads(urllib.request.urlopen(address_endpoint+stop_latlng).read())["results"][0]['formatted_address'].split(',')[:2])
            summary += f"{answer_start} ----> {answer_stop}. Approximately {step['duration']['text']}\n"
    print(summary)
except:
    print("Please try to be precise / check spelling")
