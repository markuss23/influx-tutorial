import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from config.database import get_influxdb_client

router = APIRouter(
    prefix="/auticka",
    tags=["Auticka"]
)

load_dotenv()
bucket = os.getenv("INFLUX_BUCKET")
ORG = os.getenv("INFLUX_ORG")


@router.get("/data")
def get_data(client=Depends(get_influxdb_client)):
    query_api = client.query_api()
    query = f'from(bucket:"{bucket}") |> range(start: 0)'
    result = query_api.query(org=ORG, query=query)

    return result


@router.get("/data2")
def get_data(client=Depends(get_influxdb_client)):
    query_api = client.query_api()
    query = f'from(bucket:"{bucket}") |> range(start: -1)'
    result = query_api.query(org=ORG, query=query)

    return result
