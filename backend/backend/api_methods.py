# from django.views.decorators.csrf import csrf_exempt
# from backend.fixtures import create_dummy_prediction_fixtures as cdpf

from backend.database import get_cursor, base_url
from django.http import JsonResponse

import requests
import ast
import json

def get_route_delay(route_stops, route="72"):

    predictions = []
    delay_list = []
    for stop_id in route_stops:
        r = requests.get(base_url.format("stops/" + stop_id + "/predictions"))
        if r.status_code == 404:
                continue
        response = (ast.literal_eval(r.text)[0])
        response = json.dumps(response)
        response = json.loads(response)

        # isolates route specific predictions
        if type(response) is not dict:
            print("this is the response type-->", type(response))
            continue
        if response.get("RouteName") == route:
            predictions.append(response)


    for prediction in predictions:
        print(prediction.get("PredictedDelayInSeconds"))
        delay_list.append(prediction.get("PredictedDelayInSeconds"))

    return delay_list

def average_delay(delay_list):

        # switched from JSON output to single number as there's no point to being a dictionary. This Will
        # mean I have to change where the delay is inserted into the final JSON dict

        if len(delay_list) != 0:
            avg_delay = abs(sum(delay_list)/len(delay_list))
            return avg_delay_json

        else:
            return None


def get_stops_for_route(route):

    base_url = "https://api.actransit.org/transit/{}/?token=369BB8F6542E51FF57BC06577AFE829C"
    cur = get_cursor()

    #get list of stops for route parameter
    cur.execute("SELECT stopid FROM stoproutes WHERE routename='{}';".format(route))
    print("SELECT stopid FROM stoproutes WHERE routename='{}';".format(route))
    stop_ids_tuples = cur.fetchall()

    # THERE HAS GOT TO BE  A BETTER WAY TO DO THIS
    stop_ids = []
    for stop_id in stop_ids_tuples:
        stop_ids.append(stop_id[0])


    return stop_ids

def get_route_line(route=72):
        cur = get_cursor()
        cur.execute("SELECT ST_AsGeoJSON(geom :: geometry) FROM mar2512shape WHERE pub_rte='{}'".format(route))
        response = cur.fetchone()[0]
        route_line_json = json.loads(response)
        return route_line_json
