from typing import Dict
from logging import Logger
from geolite2 import geolite2


def convert_ip_to_country(ip: str, server_logger: Logger) -> str:
    geo = geolite2.reader()
    try:
        return geo.get(ip).get('country').get('names').get('en')
    except ValueError:
        server_logger.warning("Couldn't find country for given IP", extra={'ip': ip})
        return "Unknown"


def get_geo_values(ip: str, country: str) -> Dict:
    return {"ip": ip, "country": country}
