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


def move(keys, ll, spn):
    if keys[pygame.K_UP] and float(spn.split(",")[0]) < 2:
        spn = ",".join([str(float(spn.split(",")[0]) + 0.01), str(float(spn.split(",")[1]) + 0.01)])
    if keys[pygame.K_DOWN] and float(spn.split(",")[0]) > 0.001:
        spn = ",".join([str(float(spn.split(",")[0]) - 0.01), str(float(spn.split(",")[1]) - 0.01)])
    if keys[pygame.K_d]:
        ll = ",".join([str(float(ll.split(",")[0]) + (float(spn.split(",")[0]))), str(ll.split(",")[1])])
    if keys[pygame.K_a]:
        ll = ",".join([str(float(ll.split(",")[0]) - (float(spn.split(",")[0]))), str(ll.split(",")[1])])
    if keys[pygame.K_w]:
        ll = ",".join([str(ll.split(",")[0]), str(float(ll.split(",")[1]) + (float(spn.split(",")[0])))])
    if keys[pygame.K_s]:
        ll = ",".join([str(ll.split(",")[0]), str(float(ll.split(",")[1]) - (float(spn.split(",")[0])))])
    return ll, spn


ll = "37.677751,55.757718"
spn = "0.01,0.01"
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
        keys = pygame.key.get_pressed()
        ll, spn = move(keys, ll, spn)
        map_params = {
            "ll": ll,
            "spn": spn,
            "apikey": STATIC_MAPS_KEY,
        }
        map_file = make_mapBr(server_address_maps, map_params)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()  # Обновление экрана
pygame.quit()
