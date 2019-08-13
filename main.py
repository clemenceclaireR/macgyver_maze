#! /usr/bin/env python3
# coding: utf-8

from maze_architecture import *
from graphic import *


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
    maze_file = "labyrinthe.txt"
    return Level(maze_file)


def place_items(level):
    """
    Initialization of the three items and place it in the level
    """
    ether = Items("ether")
    needle = Items("needle")
    plastic_tube = Items("tube")
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
    if event == "You managed to escape !":
        message = pygame.image.load(folder + you_win_img).convert()
    if event == "You weren't ready !":
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


def main():
    """
    Initialization of all the objects needed in the game loop
    """

    # initialization of the game window
    game_window = display_window(window_width, window_height)
    pygame.display.flip()
    # initialization of the maze
    maze = load_maze_file()
    maze.display(game_window)
    # initalization of the place_items
    place_items(maze)
    maze.design_items()
    # Initalization of the hero and villain
    macgyver = Sprite("macgyver")
    guardian = Sprite("guardian")
    macgyver.place(maze)
    guardian.place(maze)
    maze.design_sprite()
    # displaying maze, place_items and characters
    maze.display(game_window)
    macgyver.display_inventory(maze, game_window)
    # Game loop
    playing_game = True

    while playing_game:
        clock = pygame.time.Clock()
        clock.tick(60)  # Maximum 60 loops by second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                confront_result = macgyver.move(maze, event.key)
                if confront_result != "":
                    end_game(confront_result, game_window)
                    playing_game = replay()
                    if playing_game:
                        main()
                else:
                    maze.display(game_window)
                    macgyver.display_inventory(maze, game_window)


if __name__ == "__main__":
    main()
