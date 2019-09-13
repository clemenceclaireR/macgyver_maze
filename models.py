#! /usr/bin/env python3
# coding: utf-8

import pygame.display
from pygame.locals import *
from tools import Tools
from illustrations import *


class Character:
    """
    attributes line and col show the position of the sprites
    name shows the given sprite
    inventory is the list which will contain the game items
    """
    def __init__(self, name):
        self.line = 1
        self.col = 1
        self.name = name
        self.inventory = ["slot", "slot", "slot", "slot"]

    def fight(self, enemy):
        """
        Check hero's inventory when meeting enemy
        """
        if enemy == "guardian":
            if Tools.SYRINGE.value in self.inventory:
                return "win"
            else:
                return "lose"
        else:
            return ""

    def display_inventory(self, level, window):
        """
        place inventory's slot and fill it
        if the three items are in inventory, then display syringe
        """

        if Tools.SYRINGE.value in self.inventory:
            x = sprite_size * (10 + 1)
            y = sprite_size * (15 + 1.5)
            window.blit(level.picture[Tools.SYRINGE.value], (x, y))
        else:
            i = 0
            for line in [15]:
                for col in [6, 7, 8, 10]:
                    x_slot = sprite_size * (col + 1)
                    y_slot = sprite_size * (line + 1.5)
                    window.blit(level.picture[self.inventory[i]], (x_slot, y_slot))
                    i += 1
        if Tools.ETHER.value in self.inventory and \
                Tools.NEEDLE.value in self.inventory and \
                Tools.TUBE.value in self.inventory:
            folder = "macgyver_ressources/ressource/"
            message = pygame.image.load(folder + make_syringe_img).convert()
            message_x = sprite_size * 5
            message_y = sprite_size * 6
            self.inventory = [Tools.SYRINGE.value]
            window.blit(message, (message_x, message_y))

        pygame.display.flip()

    def move(self, level, key=None):
        """
        3 cases :
        - if no wall, item or enemy : move
        - if wall, no move
        - if no wall but item, move + pick up item
        - if guardian : fight
        """
        x = self.col
        y = self.line
        dx = dy = 0
        if key == K_UP and y > 0:
            dy = -1
        if key == K_RIGHT and x < 14:
            dx = +1
        if key == K_DOWN and y < 14:
            dy = +1
        if key == K_LEFT and x > 0:
            dx = -1
        if level.floor[y + dy][x + dx] == "guardian":
            return self.fight("guardian")
        elif level.floor[y + dy][x + dx] != "#":
            self.search_items(level, y + dy, x + dx)
            level.floor[y][x] = '.'
            self.line = y + dy
            self.col = x + dx
            level.floor[self.line][self.col] = self.name
        return ""

    def place(self, level):
        """
        place the characters on a border empty ground
        """
        self.line, self.col = level.find_entry()
        level.floor[self.line][self.col] = self.name

    def search_items(self, level, line, col):
        """
        update inventory when character encounter an item
        items are placed in order
        """
        floor = level.floor[line][col]
        if floor in ["ether", "needle", "tube"]:
            i = 0
            while self.inventory[i] != "slot" and i < 4:
                i += 1
            self.inventory[i] = floor


class Items:

    def __init__(self, name):

        self.line = 0
        self.col = 0
        self.name = name

    def place(self, level):
        self.line, self.col = level.find_empty_floor('.')
        level.floor[self.line][self.col] = self.name


if __name__ == "__main__":
    pass
