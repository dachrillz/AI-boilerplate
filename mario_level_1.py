#!/usr/bin/env python
__author__ = 'justinarmstrong'

"""
This is an attempt to recreate the first level of
Super Mario Bros for the NES.
"""

import sys
import pygame as pg
from data.main import main
import cProfile


def start_game(reference_to_container):
    main(reference_to_container)
    pg.quit()
    sys.exit()
