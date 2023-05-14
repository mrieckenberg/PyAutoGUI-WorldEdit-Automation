import pyautogui as gui
import time
import random
import tkinter as tk



class WorldEditAutomationClass():
    def __init__(self):

        self.coordinates = [
            # Test coordinates *************************
            # [(646, 66, 2029), (621, 75, 2082)],
            # [(588, 71, 2056), (570, 82, 2077)],
            # ******************************************

            # Row house coordinates
            [(-1207, 113, -153), (-1227, 65, -271)],
            [(-1194, 113, -275), (-1171, 65, -156)],
        ]

        self.old_materials = [
            # Test materials *************************
            # "red_sand",
            # "orange_terracotta",
            # "terracotta",
            # ****************************************

            # Row house old materials
            "chiseled_red_sandstone",
            "red_terracotta",
            "stripped_jungle_log",
            "green_terracotta",
            "bricks",

        ]

        self.new_materials = [
            # Test materials *************************
            # "gold_block",
            # "bricks",
            # "acacia_planks",
            # "oak_planks",
            # ****************************************

            # Row house new materials
            "terracotta",
            "blue_terracotta",
            "brown_terracotta",
            "light_blue_terracotta",
            "purple_terracotta",
            "chiseled_sandstone",
            "bricks",


        ]

        # Any blocks that wish to be deleted
        self.delete_materials = [
            "dirt",
            "gray_concrete",
            "yellow_concrete",
        ]

        self.facing = [
            "north",
            "south",
            "east",
            "west"
        ]

        self.half = [
            "top",
            "bottom",
        ]

        self.old_stairs_materials = [
            "nether_brick_stairs",
            "red_nether_brick_stairs",

        ]

        self.new_stairs_materials = [
            "cut_copper_stairs",
        ]

        self.old_slab_materials = [
            "nether_brick_slab",
            "red_nether_brick_slab"
        ]

        self.new_slab_materials = [
            "cut_copper_slab"
        ]

        self.old_copper_stairs = [
            "exposed_cut_copper_stairs",
            "weathered_cut_copper_stairs",
            "oxidized_cut_copper_stairs",
        ]

        self.old_copper_slabs = [
            "exposed_cut_copper_slab",
            "weathered_cut_copper_slab",
            "oxidized_cut_copper_slab"
        ]

        self.old_copper_blocks = [
            "exposed_cut_copper",
            "weathered_cut_copper",
            "oxidized_cut_copper"
        ]


    def replace_old_materials(self):
        print("Replacing old materials")
        time.sleep(10) # Time to open Minecraft
        # Loop through the list of coordinate pairs
        for i in range(len(self.coordinates)):
            # Position 1
            pos1 = "pos1 " + str(self.coordinates[i][0][0]) + "," + str(self.coordinates[i][0][1]) + "," + str(
                self.coordinates[i][0][2])
            # print(pos1)
            gui.press('/')
            gui.typewrite('/' + pos1)
            gui.press('enter')

            # Position 2
            pos2 = "pos2 " + str(self.coordinates[i][1][0]) + "," + str(self.coordinates[i][1][1]) + "," + str(
                self.coordinates[i][1][2])
            # print(pos2)
            gui.press('/')
            gui.typewrite('/' + pos2)
            gui.press('enter')


            # Replace the old material with a random new material
            for x in range(len(self.old_materials)):
                gui.press('/')
                command = "replace " + self.old_materials[x] + " " + \
                          self.new_materials[random.randint(0, len(self.new_materials))-1]
                print(command)
                gui.typewrite('/' + command)
                gui.press('enter')

            # Destroy (replace with air) scaffolding materials
            for y in range(len(self.delete_materials)):
                gui.press('/')
                command = "replace " + self.delete_materials[y] + " air"
                print(command)
                gui.typewrite('/' + command)
                gui.press('enter')

    def replace_roofs_with_copper(self, pos1, pos2):
        time.sleep(10)

        pos1_command = "pos1 " + str(pos1[0]) + "," + str(pos1[1]) + "," + str(pos1[2])
        pos2_command = "pos2 " + str(pos2[0]) + "," + str(pos2[1]) + "," + str(pos2[2])

        # Test commands
        print(pos1_command)
        print(pos2_command)

        # Set position 1
        gui.press('/')
        gui.typewrite('/' + pos1_command)
        gui.press('enter')

        # Set position 2
        gui.press('/')
        gui.typewrite('/' + pos2_command)
        gui.press('enter')

        for old_stair in self.old_stairs_materials:
            for new_stair in self.new_stairs_materials:
                for facing in self.facing:
                    for half in self.half:
                        replace_stairs_command = "replace " + old_stair + "[facing=" + facing + ",half=" + half + "] " + \
                                          new_stair + "[facing=" + facing + ",half=" + half + "] "
                        print(replace_stairs_command)
                        gui.press('/')
                        gui.typewrite('/' + replace_stairs_command)
                        gui.press('enter')

        for old_slab in self.old_slab_materials:
            for new_slab in self.new_slab_materials:
                replace_slab_command = "replace " + old_slab + " " + new_slab
                gui.press('/')
                gui.typewrite('/' + replace_slab_command)
                gui.press('enter')

    def clean_copper_roofs(self, pos1, pos2):
        time.sleep(10)

        pos1_command = "pos1 " + str(pos1[0]) + "," + str(pos1[1]) + "," + str(pos1[2])
        pos2_command = "pos2 " + str(pos2[0]) + "," + str(pos2[1]) + "," + str(pos2[2])

        # Test commands
        print(pos1_command)
        print(pos2_command)

        # Set position 1
        gui.press('/')
        gui.typewrite('/' + pos1_command)
        gui.press('enter')

        # Set position 2
        gui.press('/')
        gui.typewrite('/' + pos2_command)
        gui.press('enter')


        for old_stair in self.old_copper_stairs:
            for facing in self.facing:
                for half in self.half:
                    replace_stairs_command = "replace " + old_stair + "[facing=" + facing + ",half=" + half + "] cut_copper_stairs[facing=" +\
                                             facing + ",half=" + half + "] "
                    print(replace_stairs_command)
                    gui.press('/')
                    gui.typewrite('/' + replace_stairs_command)
                    gui.press('enter')

        for old_slab in self.old_copper_slabs:
            replace_slab_command = "replace " + old_slab + " cut_copper_slab"
            print(replace_slab_command)
            gui.press('/')
            gui.typewrite('/' + replace_slab_command)
            gui.press('enter')

        for old_block in self.old_copper_blocks:
            replace_slab_command = "replace " + old_block + " cut_copper"
            print(replace_slab_command)
            gui.press('/')
            gui.typewrite('/' + replace_slab_command)
            gui.press('enter')


world_edit = WorldEditAutomationClass()
# world_edit.replace_old_materials()
world_edit.replace_roofs_with_copper((-1618,66,76),(-1540,97,-23))
world_edit.replace_roofs_with_copper((-1518,63,11),(-1381,119,-187))
world_edit.clean_copper_roofs((-1636,66,87),(-1390,134,-191))