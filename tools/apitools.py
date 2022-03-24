# import orjson
import geojson as geoj
import orjson


def get_mlk():
    from orjson import loads
    path = "C:\\work\\hackathon\\gisit2022\\project\\backend3\\images\\mlk.geojson"
    with open(path, "rb") as f:
        return orjson.loads(f.read())


def divide(coords):
    return [coords[0] / 1000000, coords[1] / 1000000]


if __name__ == '__main__':
    with open('../images/mlk2.geojson', 'rb') as f:
        res = geoj.loads(f.read())
        for k, feature in enumerate(res.features):
            for i1, coord in enumerate(feature.geometry.coordinates):
                for i2, coord1 in enumerate(coord):
                    for i3, coord2 in enumerate(coord1):
                        res.features[k].geometry.coordinates[i1][i2][i3] = divide(coord2)

    with open('../images/mlkd.geojson', 'w') as f:
        geoj.dump(res, f)
