"""Client router module for all client API routes."""

import csv
import json
import logging
from datetime import datetime
from typing import Any, Dict, Hashable, List
from datetime import datetime
import pandas as pd
from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/client/v1", tags=["client"])


@router.get("/update-sensor")
def update_sensor(sensor_id: str, temperature: float, humidity: float):
    now = datetime.now().timestamp()
    data_obj = {
        "timestamp": now,
        "sensor_id": sensor_id,
        "data": {"temperature": temperature, "humidity": humidity},
    }

    data_row = [now, sensor_id, temperature, humidity]
    with open("data/data_home.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data_row)

    return data_obj


def get_data(file_path: str = "data/data_home.csv"):
    df = pd.read_csv(file_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    return df.to_dict(orient="records")


def transform_data(data):
    return [
        {
            "id": "temperature",
            "data": [{"x": x["timestamp"], "y": x["temperature"]} for x in data],
        },
        {
            "id": "humidity",
            "data": [{"x": x["timestamp"], "y": x["humidity"]} for x in data],
        },
    ]


@router.get("/all-data")
async def get_all_data(
    file_path: str = "data/data_home.csv",
):
    return get_data(file_path)
    # return transform_data(data)

    data = {}
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        logger.exception(f"File not found at {file_path}")
    except Exception as exc:
        logger.exception(exc)

    return data
