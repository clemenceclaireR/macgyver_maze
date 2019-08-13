#! /usr/bin/env python3
# coding: utf-8

import pygame

sprite_size = 38

BLACK = (0, 0, 0)
GREY = (47, 79, 79)
DARK_BLUE = (43, 48, 62)
background = pygame.Surface([15, 15])


window_width = 17 * sprite_size
window_height = 18 * sprite_size

ground_img = "floor_tile.png"
wall_img = "brique.png"

ether_img = "ether_bottle.png"
needle_img = "aiguille.png"
syringe_img = "syringe.png"
plastictube_img = "pipe.png"

macgyver_img = "MacGyver.png"
guardian_img = "Gardien.png"
slot_img = "square.png"

you_win_img = "youwin.png" #266x76 (38*7 / 38*2)
you_lose_img = "youlose.png"

replay_img = "replay.png" #266x190 (38*7 / 38*5)

