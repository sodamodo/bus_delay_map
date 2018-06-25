import psycopg2
import json
import requests
import ast

base_url = "https://api.actransit.org/transit/{}/?token=369BB8F6542E51FF57BC06577AFE829C"

def get_cursor():
    conn = psycopg2.connect(dbname="gis", user="gisuser", password="password", host="localhost")
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor
