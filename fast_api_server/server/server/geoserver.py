import datetime
import logging
from typing import List

from fastapi import APIRouter

from server.database.utils import insert_information_to_db, select_ips_from_country, get_top_five_values, \
    get_server_connection_cursor
from server.server.utils import convert_ip_to_country, GeoValues

geolocation_api = APIRouter(
    prefix='/geolocation'
)

server_cursor = get_server_connection_cursor()
logging.basicConfig(filename='fast_api_server.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(values)s')
server_logger = logging.getLogger('fast_api_server')


@geolocation_api.get('/ip')
async def country_finder(ip: str = '8.8.8.8') -> str:
    server_logger.info("Recieved an ip", extra={"values": ip})
    country = convert_ip_to_country(ip, server_logger)
    geo_values = GeoValues(ip=ip, country=country).dict()
    insert_information_to_db(geo_values, server_cursor)
    server_logger.info("Added row to DB", extra={'values': geo_values})
    return country


@geolocation_api.get("/country")
async def country_finder(country: str = 'United States', start_time: str = str(datetime.date.min),
                         end_time: str = str(datetime.datetime.now())) -> List:
    server_logger.info(f"Recieved request for IPs from {country}", extra={'values': f'{start_time}-{end_time}'})
    ips = select_ips_from_country(country, start_time, end_time, server_cursor)
    server_logger.info("Finished receiving relevant IPs", extra={'values': ips})
    return ips


@geolocation_api.get("/topfive")
async def top_five_values() -> List[List]:
    server_logger.info(f"Recieved request to get top five hit countries", extra={'values': ''})
    top_five_countries = get_top_five_values(server_cursor)
    server_logger.info('Finished receiving top five values', extra={'values': top_five_countries})
    return top_five_countries
