"""
This module holds all cards and all their classes and attributes.
"""

from super_library import *


class Hillary_Clinton(Group, Personality):
    def __init__(self):
        self.name = 'Hillary Clinton'
        self.flavor_text = ''
        self.rules_text = 'Gives +2 to any attempt to control Bill Clinton, Congressional Wives, or Democrats. +6 to take direct control of any of these groups.'
        self.power = 2
        self.resistance = 4
        self.alignments = ['Liberal']
        self.attributes = None
        self.puppet_arrows = ['top']
        self.master_arrows = ['left']