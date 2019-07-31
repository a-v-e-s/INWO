"""
This module holds all cards and all their classes and attributes.
"""

from super_library import *


class Adepts_of_Hermes(Group, Illuminati):
    def __init__(self):
        self.name = 'Adepts of Hermes'
        self.rules_text = '''
            If you fail an attack to control against a group from your own hand, you do not lose the group...just return the card to your hand. The adepts of Hermes have a +6 on any attempt to control or destroy a Magic group.
            '''
        self.goal_text = '''
            Each magic resource you control counts as one group toward the Basic Goal.
            '''
        self.power = 7
        self.global_power = 7
        self.master_arrows = ['top', 'bottom', 'left', 'right']


class Bermuda_Triangle(Group, Illuminati):
    def __init__(self):
        self.name = 'Bermuda Triangle'
        self.rules_text = '''
            You may reorganize your groups freely at the end of your turn.
            '''
        self.goal_text = '''
            Control a total Power of at least 35, counting Bermuda's own Power, and at least one group of each alignment. A group with more than one alignment counts for all its alignments.
            '''
        self.power = 8
        self.global_power = 8
        self.master_arrows = ['top', 'bottom', 'left', 'right']


class Discordian_Society(Group, Illuminati):
    def __init__(self):
        self.name = 'Discordian Society'
        self.rules_text = '''
            You have a +4 on any attempt to control Weird groups. Your power structure is immune to attacks from Government or Straight groups, and to all special abilities of these groups.
            '''
        self.goal_text = '''
            Any weird group with a Power of 3 or more counts double toward your total number of groups controlled.
            '''
        self.power = 7
        self.global_power = 7
        self.master_arrows = ['top', 'bottom', 'left', 'right']


class Gnomes_of_Zurich(Group, Illuminati):
    def __init__(self):
        self.name = 'Gnomes of Zurich'
        self.rules_text = '''
            You may hold 6 Plot cards in your hand, rather than the usual 5. You have a +4 on any attempt to control Corporate groups or Banks.
            '''
        self.goal_text = '''
            Any Corporate group or Bank with a Power of 4 or more counts double toward your total number of groups controlled.
            '''
        self.power = 9
        self.global_power = 9
        self.master_arrows = ['top', 'bottom', 'left', 'right']


class The_Network(Group, Illuminati):
    def __init__(self):
        self.name = 'The Network'
        self.rules_text = '''
            You start your turn by drawing two plot cards, rather than one.
            '''
        self.goal_text = '''
            Any Computer group with a Power of 3 or more counts double toward your total number of groups controlled.
            '''
        self.power = 8
        self.global_power = 8
        self.master_arrows = ['top', 'bottom', 'left', 'right']


class Servants_of_Cthulu(Group, Illuminati):
    def __init__(self):
        self.name = 'Servants of Cthulu'
        self.rules_text = '''
            You have a +4 on any attempt to destroy, even with Disasters and Assassinations. Draw a Plot card whenever you destroy a group!'''
        self.goal_text = '''
            For every group you destroy, reduce by 1 the number of groups you need to control in order to win. You may also count rival Illuminati which you destroy by removing their last group. If you destroy 8 groups, you win, regardless of how many you control!'''
        self.power = 9
        self.global_power = 9
        self.master_arrows = ['top', 'bottom', 'left', 'right']


class Shangri_La(Group, Illuminati):
    def __init__(self):
        self.name = 'Shangri-La'
        self.rules_text = '''
            Any group in your power structure has an extra +5 to defend against any attack. You cannot destroy any groups except Violent ones and rival Illuminati.'''
        self.goal_text = '''
            Have Peaceful groups with a total Power of 30 in play, regardless of who controls them! If this happens, all Shangri-La players share the victory.'''
        self.power = 7
        self.global_power = 7
        self.master_arrows = ['top', 'bottom', 'left', 'right']


class Bavarian_Illuminati(Group, Illuminati):
    def __init__(self):
        self.name = 'Bavarian Illuminati'
        self.rules_text = '''
            Each turn, you may declare one of your attacks privileged.
            '''
        self.goal_text = '''
            Control a total Power of 50 or more, counting Bavaria's own Power.
            '''
        self.power = 10
        self.global_power = 10
        self.master_arrows = ['top', 'bottom', 'left', 'right']


class UFOs(Group, Illuminati):
    def __init__(self):
        self.name = 'UFOs'
        self.rules_text = '''
            The UFOs have two actions per turn -- they get two tokens! These may not be used in the same attack.
            '''
        self.goal_text = '''
            The UFOs can have up to 3 different Goal cards in play, and win with any of them.
            '''
        self.power = 6
        self.global_power = 6
        self.master_arrows = ['top', 'bottom', 'left', 'right']


class Society_of_Assassins(Group, Illuminati):
    def __init__(self):
        self.name = 'Society of Assassins'
        self.rules_text = '''
            When one of your Fanatic groups attacks or defends, you may treat its Fanatic alignment as the same as that of any other Fanatic group. Your Fanatic groups also have Global Power equal to their Power.
            '''
        self.goal_text = '''
            Any Secret group counts double for you as long as none of your rivals control a Secret group with more power.
            '''
        self.power = 7
        self.global_power = 7
        self.master_arrows = ['top', 'bottom', 'left', 'right']


class Hillary_Clinton(Group, Personality):
    def __init__(self):
        self.name = 'Hillary Clinton'
        self.rules_text = '''
            Gives +2 to any attempt to control Bill Clinton, Congressional Wives, or Democrats. +6 to take direct control of any of these groups.
            '''
        self.power = 2
        self.resistance = 4
        self.alignments = ['Liberal']
        self.attributes = None
        self.puppet_arrows = ['top']
        self.master_arrows = ['left']