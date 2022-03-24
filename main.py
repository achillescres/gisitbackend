import orjson
from fastapi import FastAPI
from fastapi.responses import FileResponse, ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

# import tools
from tools.tiles import get_tile_response
from tools.apitools import get_mlk
app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', response_class=ORJSONResponse)
async def home():
    return {'Route': 'home'}


@app.get('/aytal')
async def aytal():
    return FileResponse('./images/Untitled.gif')


@app.get('/tiles/ice/{x}/{y}/{z}')
async def tiles(x: int, y: int, z: int):
    return get_tile_response('ice', x, y, z)


@app.get('/mlk', response_class=ORJSONResponse)
async def mlk():
    with open('./images/newmlk.geojson', 'rb') as f:
        res = orjson.loads(f.read())
        return res



@app.get('/fire')
async def fire():
    return FileResponse('./images/fire.tif')


@app.get('/water')
async def water():
    return FileResponse('./images/water.tif')
