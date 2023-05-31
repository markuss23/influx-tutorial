from influxdb_client import InfluxDBClient
import os
from dotenv import load_dotenv

load_dotenv()
ORG = os.getenv("INFLUX_ORG")
URL = os.getenv("INFLUX_URL")
TOKEN = os.getenv("INFLUX_TOKEN")

def get_influxdb_client():
    client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
    try:
        yield client
    finally:
        client.close()
