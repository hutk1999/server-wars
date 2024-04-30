import sqlite3
from datetime import datetime
from sqlite3 import Cursor
from typing import List, Tuple, Union

from server.database.consts import (INSERT_GEOLOCATION_ROW,
                                    GET_IPS_BY_DATETIME,
                                    RETRIEVE_TUPLE_ID,
                                    INSERT_DATETIME_ROW,
                                    CREATE_GEOLOCATION_TABLE,
                                    CREATE_DATETIME_TABLE,
                                    CONNECT_DB,
                                    GET_TOP_FIVE_VALUES,
                                    GEOLOCATION_TABLE
                                    )


def parse_tuples_from_list(list_of_tuples: List[Tuple]) -> List:
    return [item[0] for item in list_of_tuples]


def parse_item_from_tuple(item_tuple: Tuple) -> int:
    return item_tuple[0]


def check_if_id_exists(geo_values: dict, c: Cursor) -> Tuple:
    return c.execute(RETRIEVE_TUPLE_ID, geo_values).fetchone()


def insert_information_to_db(geo_values: dict, c: Cursor) -> None:
    geo_id = check_if_id_exists(geo_values, c)
    if not geo_id:
        c.execute(INSERT_GEOLOCATION_ROW, geo_values)
        geo_id = c.lastrowid
    else:
        geo_id = parse_item_from_tuple(geo_id)
    c.execute(INSERT_DATETIME_ROW, {'ID': geo_id, 'datetime': str(datetime.now())})
    c.connection.commit()


def select_ips_from_country(country: str, start_time: str, end_time: str, c: Cursor) -> Union[List, None]:
    response = c.execute(GET_IPS_BY_DATETIME, {'country': country, 'start_time': start_time, 'end_time': end_time})
    ips = response.fetchall()
    return parse_tuples_from_list(ips)


def get_top_five_values(c: Cursor) -> List[List]:
    top_five_values = c.execute(GET_TOP_FIVE_VALUES)
    return top_five_values.fetchall()


def check_existing_tables(server_cursor: Cursor) -> bool:
    server_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = server_cursor.fetchall()
    return GEOLOCATION_TABLE in tables


def get_server_connection_cursor() -> Cursor:
    conn = sqlite3.connect(CONNECT_DB)
    server_cursor = conn.cursor()
    if not check_existing_tables(server_cursor):
        server_cursor.execute(CREATE_GEOLOCATION_TABLE)
        server_cursor.execute(CREATE_DATETIME_TABLE)
    return server_cursor
