# from backend.database import get_cursor, aggregate_features, get_stops_for_route, populate_stops, base_url
# from backend.fixtures import create_dummy_prediction_fixtures as cdpf
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from backend.api_methods import get_route_delay, average_delay, get_stops_for_route

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from backend.api_methods import get_route_line, average_delay, get_stops_for_route, get_route_delay
from backend.database import get_cursor

import requests
import ast
import json
import re



@csrf_exempt
def get_avg_delay_for_route(request):

        cur = get_cursor()


        # SOOOOO HACKY LEARN HOW TO USE A COMPTUER
        body_unicode = request.body.decode('utf-8')
        print(body_unicode)
        route = body_unicode[5:]
        print("sliced route-->", route)



        #### Gets the JSON for the line shape
        polyline_json = get_route_line(route)


        cur.execute("SELECT delay, route_name, datetime FROM delays WHERE route_name = '{}' ORDER BY datetime DESC LIMIT 1;".format(route))
        delay = cur.fetchone()[0]

        ###########################################################
        ###########################################################
        ###########################################################


        # with open('delay_list.txt', 'a+') as outfile:
        #     outfile.write(str(avg_delay) + "\n")


        geojson_template = {
                      "type": "Feature",
                      "geometry": {
                        "type": "MultiLineString",
                        "coordinates": ""
                      },
                      "properties": {
                        "route": "",
                        "delay": ""
                      }
                    }


        geojson_template["geometry"]["coordinates"] = polyline_json["coordinates"]
        geojson_template["properties"]["route"] = route
        geojson_template["properties"]["delay"] = delay

        geojson = geojson_template


        with open('72_delay.txt', 'w') as outfile:
            json.dump(geojson, outfile)



        return JsonResponse(geojson)
