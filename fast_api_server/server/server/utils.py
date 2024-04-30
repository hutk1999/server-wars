from logging import Logger
from typing import Dict

from geolite2 import geolite2
from pydantic import BaseModel


class GeoValues(BaseModel):
    ip: str
    country: str


def convert_ip_to_country(ip: str, server_logger: Logger) -> str:
    geo = geolite2.reader()
    try:
        return geo.get(ip).get('country').get('names').get('en')
    except ValueError:
        server_logger.warning("Couldn't find country for given IP", extra={'values': ip})
        return "Unknown"


def get_geo_values(ip: str, country: str) -> Dict:
    return {"ip": ip, "country": country}
