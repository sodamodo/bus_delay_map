# from backend.database import get_cursor, aggregate_features, get_stops_for_route, populate_stops, base_url
# from backend.fixtures import create_dummy_prediction_fixtures as cdpf
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from backend.api_methods import get_route_delay, average_delay, get_stops_for_route

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from backend.api_methods import get_route_line, average_delay, get_stops_for_route, get_route_delay
import requests
import ast
import json



@csrf_exempt
def get_avg_delay_for_route(request):


        ##############################################
        # So I don't have to spend all day making calls
        ##############################################
        # with open("72_delay.txt", "r") as f:
        #     response = json.loads(f.read())
        #
        #
        #     return JsonResponse(response)


        # Will receive route from POST from client
        route = "72"

        polyline_json = get_route_line(route)


        delay_list = get_route_delay(route)


        avg_delay = average_delay(delay_list=delay_list)
        print("type of avg delay--->", avg_delay)


        with open('delay_list.txt', 'a+') as outfile:
            outfile.write(str(avg_delay) + "\n")


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
        geojson_template["properties"]["delay"] = avg_delay

        geojson = geojson_template

        print(geojson)

        with open('72_delay.txt', 'w') as outfile:
            json.dump(geojson, outfile)



        return JsonResponse(geojson)
