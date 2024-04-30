import uvicorn
from fastapi import FastAPI

from server.server.geoserver import geolocation_api

app = FastAPI()

app.include_router(geolocation_api)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
