#! /usr/bin/env python3
# coding: utf-8

from game_manager import *
from tools_heroes import *


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
    macgyver = Character(Heroes.MACGYVER.value)
    guardian = Character(Heroes.GUARDIAN.value)
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
        # number of loops per second
        clock.tick(60)  
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
