import pyautogui as gui
import time
import random



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

        self.old_cut_copper_stairs = [
            "exposed_cut_copper_stairs",
            "weathered_cut_copper_stairs",
            "oxidized_cut_copper_stairs",
        ]

        self.old_cut_copper_slabs = [
            "exposed_cut_copper_slab",
            "weathered_cut_copper_slab",
            "oxidized_cut_copper_slab"
        ]

        self.old_cut_copper_blocks = [
            "exposed_cut_copper",
            "weathered_cut_copper",
            "oxidized_cut_copper"
        ]


        self.unoxidized_cut_copper_blocks = [
            "waxed_cut_copper",
            "cut_copper",
            "exposed_cut_copper",
            "weathered_cut_copper",
        ]

        self.unoxidized_cut_copper_stairs = [
            "waxed_cut_copper_stairs",
            "cut_copper_stairs",
            "exposed_cut_copper_stairs",
            "weathered_cut_copper_stairs"
        ]

        self.unoxidized_cut_copper_slabs = [
            "waxed_cut_copper_slab",
            "cut_copper_slab",
            "exposed_cut_copper_slab",
            "weathered_cut_copper_slab"
        ]

        # For undoing processes
        self.num_times_run = 0

    def increment_times_run(self):
        self.num_times_run += 1

    def decrement_times_run(self):
        self.num_times_run += -1

    def replace_old_materials(self):
        print("Replacing old materials")
        self.print_to_gui("Replacing old materials in selected areas")
        time.sleep(10) # Time to open Minecraft
        # Loop through the list of coordinate pairs
        for i in range(len(self.coordinates)):
            # Position 1
            pos1 = "pos1 " + str(self.coordinates[i][0][0]) + "," + str(self.coordinates[i][0][1]) + "," + str(
                self.coordinates[i][0][2])
            self.send_command(pos1)

            # Position 2
            pos2 = "pos2 " + str(self.coordinates[i][1][0]) + "," + str(self.coordinates[i][1][1]) + "," + str(
                self.coordinates[i][1][2])
            self.send_command(pos2)


            # Replace the old material with a random new material
            for x in range(len(self.old_materials)):

                command = "replace " + self.old_materials[x] + " " + \
                          self.new_materials[random.randint(0, len(self.new_materials))-1]
                print(command)
                self.send_command(command)

            # Destroy (replace with air) scaffolding materials
            for y in range(len(self.delete_materials)):
                command = "replace " + self.delete_materials[y] + " air"
                self.send_command(command)

        self.print_to_gui("Done replacing materials")

    def replace_roofs_with_copper(self, pos1, pos2):
        time.sleep(10)

        pos1_command = "pos1 " + str(pos1[0]) + "," + str(pos1[1]) + "," + str(pos1[2])
        pos2_command = "pos2 " + str(pos2[0]) + "," + str(pos2[1]) + "," + str(pos2[2])

        # Test commands
        # print(pos1_command)
        # print(pos2_command)

        # Set position 1
        self.send_command(pos1_command)

        # Set position 2
        self.send_command(pos2_command)

        for old_stair in self.old_stairs_materials:
            for new_stair in self.new_stairs_materials:
                for facing in self.facing:
                    for half in self.half:
                        replace_stairs_command = "replace " + old_stair + "[facing=" + facing + ",half=" + half + "] " + \
                                          new_stair + "[facing=" + facing + ",half=" + half + "] "
                        self.send_command(replace_stairs_command)

        for old_slab in self.old_slab_materials:
            for new_slab in self.new_slab_materials:
                replace_slab_command = "replace " + old_slab + " " + new_slab
                self.send_command(replace_slab_command)

    def clean_copper_roofs(self, pos1, pos2):
        self.print_to_gui("Cleaning the copper roofs")
        time.sleep(10)

        pos1_command = "pos1 " + str(pos1[0]) + "," + str(pos1[1]) + "," + str(pos1[2])
        pos2_command = "pos2 " + str(pos2[0]) + "," + str(pos2[1]) + "," + str(pos2[2])

        # Test commands
        print(pos1_command)
        print(pos2_command)

        # Set position 1
        self.send_command(pos1_command)


        # Set position 2
        self.send_command(pos2_command)


        for old_stair in self.old_cut_copper_stairs:
            for facing in self.facing:
                for half in self.half:
                    replace_stairs_command = "replace " + old_stair + "[facing=" + facing + ",half=" + half + "] cut_copper_stairs[facing=" +\
                                             facing + ",half=" + half + "] "
                    self.send_command(replace_stairs_command)

        for old_slab in self.old_cut_copper_slabs:
            replace_slab_command = "replace " + old_slab + " cut_copper_slab"
            self.send_command(replace_slab_command)

        for old_block in self.old_cut_copper_blocks:
            replace_block_command = "replace " + old_block + " cut_copper"
            self.send_command(replace_block_command)

        self.print_to_gui("Done cleaning the copper roofs")

    def oxidize_copper_roofs(self, pos1, pos2):
        self.print_to_gui("Oxidizing the copper roofs")
        time.sleep(10)

        pos1_command = "pos1 " + str(pos1[0]) + "," + str(pos1[1]) + "," + str(pos1[2])
        pos2_command = "pos2 " + str(pos2[0]) + "," + str(pos2[1]) + "," + str(pos2[2])

        # Test commands
        print(pos1_command)
        print(pos2_command)

        # Set position 1
        self.send_command(pos1_command)

        # Set position 2
        self.send_command(pos2_command)

        for unoxidized_stair in self.unoxidized_cut_copper_stairs:
            for facing in self.facing:
                for half in self.half:
                    replace_stairs_command = "replace " + unoxidized_stair + "[facing=" + facing + ",half=" + half + "] oxidized_cut_copper_stairs[facing=" +\
                                             facing + ",half=" + half + "] "
                    self.send_command(replace_stairs_command)


        for unoxidized_slab in self.unoxidized_cut_copper_slabs:
            replace_slab_command = "replace " + unoxidized_slab + " oxidized_cut_copper_slab"
            self.send_command(replace_slab_command)

        for unoxidized_block in self.unoxidized_cut_copper_blocks:
            replace_block_command = "replace " + unoxidized_block + " oxidized_cut_copper"
            self.send_command(replace_block_command)

        self.print_to_gui("Done oxidizing the copper roofs")

    # This function will run and undo all changes in 120 seconds if the user does not stop the script.
    # This function is intended to undo any erroneous changes.
    def undo_commands(self):
        print("Commands will undo in 60 seconds if you do not stop the script.")
        self.print_to_gui("Commands will undo in 60 seconds if you do not stop the script.")
        time.sleep(120) # Give a minute rest for blocks to render
        n = self.num_times_run
        for i in range(n):
            # Commands are not run through self.send_command() since it includes the self.increment_times_run() function
            gui.press('/')
            gui.typewrite('/undo')
            gui.press('enter')
            self.decrement_times_run()
        self.print_to_gui("Done undoing commands.")
        print("Times run: " + str(self.num_times_run))

    def print_to_gui(self, message):
        time.sleep(10)
        gui.press('/')
        gui.typewrite('say ' + message)
        gui.press('enter')

    def send_command(self, command):
        print(command)
        gui.press('/')
        gui.typewrite('/' + command)
        gui.press('enter')
        self.increment_times_run()

    def generate_house(self, pos1, length, width, height):
        self.print_to_gui("Generating a random house")
        time.sleep(10)

        # Only position 1 is given as a parameter. Position 2 is calculated
        pos1_command = "pos1 " + str(pos1[0]) + "," + str(pos1[1]) + "," + str(pos1[2])

        # Set position 1
        print(pos1_command)
        self.send_command(pos1_command)




world_edit = WorldEditAutomationClass()
world_edit.print_to_gui("Starting the WorldEdit automation process ")

# Testing Area ****************************************************************
# world_edit.replace_old_materials()
# world_edit.replace_roofs_with_copper((-1618,66,76),(-1540,97,-23))
# world_edit.replace_roofs_with_copper((-1518,63,11),(-1381,119,-187))
# world_edit.clean_copper_roofs((-1636,66,87),(-1390,150,-191))
# world_edit.oxidize_copper_roofs((-1636,66,87),(-1390,150,-191))
# *****************************************************************************

# Sunday, May 14, 2023 ********************************************************

# Put copper on the roofs
# world_edit.replace_roofs_with_copper((-1618,66,76),(-1540,97,-23))
# world_edit.replace_roofs_with_copper((-1518,63,11),(-1381,119,-187))
# world_edit.replace_roofs_with_copper((-1389,127,-122),(-1302,65,-304))
# world_edit.replace_roofs_with_copper((-1304,138,-119),(-1496,66,121))
#
# # Clean up all roofs
# world_edit.clean_copper_roofs((-1618,66,76),(-1540,97,-23))
# world_edit.clean_copper_roofs((-1518,63,11),(-1381,119,-187))
# world_edit.clean_copper_roofs((-1389,127,-122),(-1302,65,-304))
# world_edit.clean_copper_roofs((-1304,138,-119),(-1496,66,121))

# Testing oxidation
# world_edit.oxidize_copper_roofs((-1656,60,160),(-1250,143,-333))
# world_edit.clean_copper_roofs((-1656,60,160),(-1250,143,-333))

# Test undo function
# world_edit.undo_commands()
# *****************************************************************************

world_edit.print_to_gui("The WorldEdit automation process is now complete ")
exit(1)

