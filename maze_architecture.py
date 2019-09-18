#! /usr/bin/env python3
# coding: utf-8

from random import randint
from models import *
from tools_heroes import Tools


class Level:
    """
    floor shows the 15*15 squares of the maze, each square is a string
    picture associate the image attached to the sprite or string
    """
    def __init__(self, filename):
        self.floor = [["."] * 15] * 15
        self.load_level(filename)
        self.picture = dict()

    def design_sprite(self):
        folder = "macgyver_ressources/ressource/"
        self.picture[Heroes.MACGYVER.value] = pygame.image.load(folder + macgyver_img).convert_alpha()
        self.picture[Heroes.GUARDIAN.value] = pygame.image.load(folder + guardian_img).convert_alpha()

    def design_items(self):
        folder = "macgyver_ressources/ressource/"
        self.picture[Tools.ETHER.value] = pygame.image.load(folder + ether_img).convert_alpha()
        self.picture[Tools.NEEDLE.value] = pygame.image.load(folder + needle_img).convert_alpha()
        self.picture[Tools.TUBE.value] = pygame.image.load(folder + plastictube_img).convert_alpha()

    def display(self, screen):
        """
        display the maze according to self.floor and display the associated picture
        """
        folder = "macgyver_ressources/ressource/"
        self.picture = {
            ".": pygame.image.load(folder + ground_img).convert(),
            "#": pygame.image.load(folder + wall_img).convert(),
            "ether": pygame.image.load(folder + ether_img).convert_alpha(),
            "needle": pygame.image.load(folder + needle_img).convert_alpha(),
            "tube": pygame.image.load(folder + plastictube_img).convert_alpha(),
            "slot": pygame.image.load(folder + slot_img).convert_alpha(),
            "macgyver": pygame.image.load(folder + macgyver_img).convert_alpha(),
            "guardian": pygame.image.load(folder + guardian_img).convert_alpha(),
            "syringe": pygame.image.load(folder + syringe_img).convert_alpha()
        }

        for line in range(15):
            for col in range(15):
                x_tile = sprite_size * (col + 1)
                y_tile = sprite_size * (line + 1)
                floor_type = self.floor[line][col]
                screen.blit(self.picture[floor_type], (x_tile, y_tile))

        pygame.display.flip()

    def find_entry(self):
        """
        find an empty ground "." on the border of the maze :
        there are two places where the characters can be placed
        """
        for line in [0, 14]:
            for col in range(0, 14):
                if self.floor[line][col] == '.':
                    return line, col
        for col in [0, 14]:
            for line in range(0, 14):
                if self.floor[line][col] == '.':
                    return line, col

    def find_empty_floor(self, floor_type):
        """
        find a ground identical to the given parameter
        in this case, it will be an empty ground to place the items and
        avoiding placing them on a wall
        items are placed randomly on empty ground
        """
        line = 0
        col = 0
        while self.floor[line][col] != floor_type:
            line = randint(0, 14)
            col = randint(0, 14)
        return line, col

    def load_level(self, filename):
        """
        read the maze file composed of "." for the ground and "#" for the walls
        each line is appended as a list to the floor list
        """
        with open(filename, "r") as maze_file:
            for line in range(15):
                self.floor[line] = maze_file.readline().strip().split(" ")


if __name__ == "__main__":
    pass
