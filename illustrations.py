#! /usr/bin/env python3
# coding: utf-8

import pygame

sprite_size = 38

DARK_BLUE = (43, 48, 62)
background = pygame.Surface([15, 15])

window_width = 17 * sprite_size
window_height = 18 * sprite_size

ground_img = "floor_tile.png"
wall_img = "stone.png"

ether_img = "ether_bottle.png"
needle_img = "needle.png"
syringe_img = "syringe.png"
plastictube_img = "pipe.png"

macgyver_img = "MacGyver.png"
guardian_img = "gardian.png"
slot_img = "square.png"

you_win_img = "youwin.png" #266x76 : in sprite -> (38*7 / 38*2) 38*6 =  38
you_lose_img = "youlose.png"

make_syringe_img = "syringe_panel.png" #190x38 : in sprite -> (38*5 / 38*1)
