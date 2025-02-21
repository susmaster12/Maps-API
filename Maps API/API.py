import sys
import pygame
import requests
from geopy.distance import geodesic

def make_mapBr(server_address_maps, map_params):
    response = requests.get(server_address_maps, map_params)
    if not response:
        return None
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


toponym_to_find = " ".join(sys.argv[1:])
ll, spn = toponym_to_find.split()
STATIC_MAPS_KEY = 'ef67d706-4387-4517-8b08-50f4c0929dd7'
map_params = {
    "ll": ll,
    "spn": spn,
    "apikey": STATIC_MAPS_KEY,
}

server_address_maps = 'https://static-maps.yandex.ru/v1?'
map_file = make_mapBr(server_address_maps, map_params)

if map_file:
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()