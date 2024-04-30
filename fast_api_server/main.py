from fastapi import FastAPI
import uvicorn
from server.server.geoserver import geolocation_api

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


app.include_router(geolocation_api)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
