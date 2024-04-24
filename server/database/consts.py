CREATE_GEOLOCATION_TABLE = """CREATE TABLE geolocation
    ( ID INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, country TEXT )
 """

CREATE_DATETIME_TABLE = """CREATE TABLE datetime_storage
    (ID INTEGER, time_stamp TEXT)
"""

INSERT_GEOLOCATION_ROW = 'INSERT INTO geolocation (ip, country) VALUES (:ip,:country)'

RETRIEVE_TUPLE_ID = 'SELECT ID from geolocation WHERE ip = :ip and country = :country'

INSERT_DATETIME_ROW = 'INSERT INTO datetime_storage VALUES (:ID, :datetime)'

CONNECT_DB = 'tests.db'

GET_TOP_FIVE_VALUES = """ SELECT count(*) as max_hits, country FROM geolocation 
    FULL JOIN datetime_storage On geolocation.ID = datetime_storage.ID 
    GROUP BY country 
    ORDER BY max_hits DESC 
    LIMIT 5
"""

GEOLOCATION_TABLE = ('geolocation',)

GET_IPS_BY_DATETIME = """ SELECT DISTINCT ip FROM geolocation 
    FULL JOIN datetime_storage On geolocation.ID = datetime_storage.ID 
    where country = :country and time_stamp > :start_time and time_stamp < :end_time
"""
