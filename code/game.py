#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Self

import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))


    def run(self):
        while True:
            menu = Menu(Self.window)
            menu.run()
            pass

            # Check for all events
            #   for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()  # Close Window
            #        quit()  # End Pygame





