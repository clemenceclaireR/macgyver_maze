#! /usr/bin/env python3
# coding: utf-8

from maze_architecture import *
from models import *


def display_window(width, height):
    """
    Initialization of pygame and displaying screen
    """
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill(DARK_BLUE)
    return screen


def load_maze_file():
    """
    Import maze model from extern file
    """
    maze_file = "maze.txt"
    return Level(maze_file)


def place_items(level):
    """
    Initialization of the three items and place it in the level
    """
    ether = Item("ether")
    needle = Item("needle")
    plastic_tube = Item("tube")
    ether.place(level)
    needle.place(level)
    plastic_tube.place(level)


def end_game(event, screen):
    """
    find out if macgyver triumphs over the guardian :
    if the inventory is full, win
    otherwise, lose
    """
    message = None
    message_x = sprite_size * 5
    message_y = sprite_size * 6
    folder = "macgyver_ressources/ressource/"
    if event == "win":
        message = pygame.image.load(folder + you_win_img).convert()
    if event == "lose":
        message = pygame.image.load(folder + you_lose_img).convert()
    screen.blit(message, (message_x, message_y))
    pygame.display.flip()


def replay():
    """
    at the end of the game, the player can choose if he wants to replay or not
    press the key according to his choice
    """
    gamers_choice = False
    while not gamers_choice:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_n:
                    return False
                elif event.key == K_y:
                    return True
