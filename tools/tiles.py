def _get_tile_path(t_type: str, x: int, y: int, z: int):
    from STATIC import IMAGES_PATH
    from os.path import join
    return join(IMAGES_PATH, 'tiles', t_type, str(x), str(y), f'{z}.png')


def get_tile_response(t_type: str, *coords: [int]):
    from fastapi.responses import FileResponse

    path = _get_tile_path(t_type, *coords)
    print(path)
    from os.path import exists
    if exists(path):
        return FileResponse(path)
    else:
        return {}
