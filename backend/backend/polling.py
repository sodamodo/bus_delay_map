
if __name__ == '__main__':
    from api_methods import get_route_line, get_route_delay, average_delay, get_stops_for_route, get_cursor

else:
    from .api_methods import get_route_line, get_route_delay, average_delay, get_stops_for_route, get_cursor



# from backend.api_methods import get_route_line, get_route_delay, average_delay, get_stops_for_route, get_cursor
import datetime
from time import sleep

##### Every x seconds, get route name, avg delay, timestamp #####

# How to parameterize the route. Get a short list of routes for MVP

routes = ["1R", "51A", "72", "20", "18"]

for route in routes:


    stops = get_stops_for_route(route)


    polyline_json = get_route_line(route)
    delay_list = get_route_delay(route_stops=stops, route=route)
    print("delay list-->", delay_list)
    avg_delay = average_delay(delay_list=delay_list)

    cur = get_cursor()


    try:
        avg_delay = '%.1f' % avg_delay

    except:
        continue
    print(avg_delay)

    print(datetime.datetime.now())

    cur.execute("INSERT INTO delays VALUES ('{}', '{}', '{}')".format(route, avg_delay, datetime.datetime.now()))
    print("inserted!")
