import pyautogui as gui
import time
import random



class WorldEditAutomationClass():
    def __init__(self):

        self.coordinates = [
            [(-1420, 95, -150), (-1408, 64, -186)],
            [(-1375, 91, -185), (-1360, 65, -211)],
            [(-1354, 65, -210), (-1342, 84, -183)],
            [(-1355, 90, -137), (-1368, 65, -121)],
            [(-1355, 90, -137), (-1340, 65, -152)],
            [(-1339, 87, -157), (-1329, 65, -132)],
            [(-1345, 90, -153), (-1315, 65, -121)],
            [(-1318, 90, -133), (-1329, 65, -159)],
            [(-1326, 85, -97), (-1315, 65, -72)],
            [(-1324, 83, -71), (-1315, 65, -44)],
        ]

        self.old_materials = [

            # Island house old materials
            # "light_blue_concrete",
            # "red_terracotta",
            # "white_terracotta",
            # "lime_terracotta",
            # "magenta_terracotta",
            # "blue_terracotta",
            # "orange_terracotta",

            "clay",
            "white_terracotta",
            "terracotta",
            "yellow_terracotta",
            "black_terracotta",
            "red_terracotta",
            "lime_terracotta",
            "pink_terracotta",


        ]

        self.new_materials = [

            # Terracottas
            "terracotta",
            "white_terracotta",
            "light_gray_terracotta",
            "gray_terracotta",
            "black_terracotta",
            "brown_terracotta",
            "red_terracotta",
            "orange_terracotta",
            "yellow_terracotta",
            "lime_terracotta",
            "green_terracotta",
            "cyan_terracotta",
            "light_blue_terracotta",
            "blue_terracotta",
            "purple_terracotta",
            "magenta_terracotta",
            "pink_terracotta",

            # Concretes
            "white_concrete",
            "light_gray_concrete",
            "gray_concrete",
            "black_concrete",
            "brown_concrete",
            "red_concrete",
            "orange_concrete",
            "yellow_concrete",
            "lime_concrete",
            "green_concrete",
            "cyan_concrete",
            "light_blue_concrete",
            "blue_concrete",
            "purple_concrete",
            "magenta_concrete",
            "pink_concrete",


            # Other materials
            "bricks",
            "cobblestone",




        ]

        # Any blocks that wish to be deleted
        self.delete_materials = [
            "dirt",
            # "gray_concrete",
            # "yellow_concrete",
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
            "spruce_stairs",
        ]

        self.new_stairs_materials = [
            "cut_copper_stairs",
        ]

        self.old_slab_materials = [
            "nether_brick_slab",
            "red_nether_brick_slab",
            "spruce_slab",
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


        self.unoxidized_copper_blocks = [
            "waxed_cut_copper",
            "cut_copper",
            "exposed_cut_copper",
            "weathered_cut_copper",
            "copper_block",
            "exposed_copper_block",
            "weathered_copper_block",

        ]

        self.unoxidized_copper_stairs = [
            "waxed_cut_copper_stairs",
            "cut_copper_stairs",
            "exposed_cut_copper_stairs",
            "weathered_cut_copper_stairs"
        ]

        self.unoxidized_copper_slabs = [
            "waxed_cut_copper_slab",
            "cut_copper_slab",
            "exposed_cut_copper_slab",
            "weathered_cut_copper_slab"
        ]

        self.old_logs = [
            "oak_log",
            # "birch_log",
        ]

        self.new_logs = [
            # "birch_log",
            "spruce_log",
            "oak_log",
            "acacia_log",
            'jungle_log',
            "dark_oak_log",
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

            # Replace old logs
            for z in range(len(self.old_logs)):
                command = "replace " + self.old_logs[z] + " " + self.new_logs[random.randint(0, len(self.new_logs)-1)]
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
            for half in self.half:
                replace_slab_command = "replace " + old_slab + "[type=" + half + "] cut_copper_slab[type=" + half + "]"
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
            for half in self.half:
                replace_slab_command = "replace " + old_slab + "[type=" + half + "] cut_copper_slab[type=" + half + "]"
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

        for unoxidized_stair in self.unoxidized_copper_stairs:
            for facing in self.facing:
                for half in self.half:
                    replace_stairs_command = "replace " + unoxidized_stair + "[facing=" + facing + ",half=" + half + "] oxidized_cut_copper_stairs[facing=" +\
                                             facing + ",half=" + half + "] "
                    self.send_command(replace_stairs_command)


        for unoxidized_slab in self.unoxidized_copper_slabs:
            replace_slab_command = "replace " + unoxidized_slab + " oxidized_cut_copper_slab"
            self.send_command(replace_slab_command)

        for unoxidized_block in self.unoxidized_copper_blocks:
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
        time.sleep(5)
        gui.press('/')
        gui.typewrite('say ' + message)
        gui.press('enter')

    def send_command(self, command): # Send WorldEdit command: //
        print(command)
        gui.press('/')
        gui.typewrite('/' + command)
        gui.press('enter')
        self.increment_times_run()

    def send_vanilla_command(self, command): # Send Vanilla command: /
        print(command)
        gui.press('/')
        gui.typewrite(command)
        gui.press('enter')
        self.increment_times_run()

    def generate_simple_house(self, pos1, length, width, height):
        # TODO: turn this into a function that allows the user to choose how many floors (default 1)
        # use a for loop and increment height so do something like pos1[1] + height*index
        self.print_to_gui("Generating a random house")
        time.sleep(10)

        # Only position 1 is given as a parameter. Position 2 is calculated
        pos1_command = "pos1 " + str(pos1[0]) + "," + str(pos1[1]) + "," + str(pos1[2])
        pos2_command = "pos2 " + str(pos1[0]+length) + "," + str(pos1[1]+height) + "," + str(pos1[2]+width)

        self.send_command(pos1_command)
        self.send_command(pos2_command)

        material = self.new_materials[random.randint(0,len(self.new_materials))]
        self.send_command("walls " + material)

        # pos2_command = "pos2 " + str(pos1[0]) + "," + str(pos1[1]+height) + "," + str(pos1[2])
        # self.send_command(pos2_command)
        # self.send_command("set " + "oak_planks")

        key_points = [
            # These work properly
            [(pos1[0],pos1[1],pos1[2]),(pos1[0],pos1[1]+height,pos1[2])],  # LH lower corner
            [(pos1[0] + length, pos1[1], pos1[2]), (pos1[0] + length, pos1[1] + height, pos1[2])],  # LH lower corner
            [(pos1[0], pos1[1], pos1[2] + width), (pos1[0], pos1[1] + height, pos1[2] + width)],  # LH upper corner
            [(pos1[0] + length, pos1[1], pos1[2] + width), (pos1[0] + length, pos1[1] + height, pos1[2] + width)],  # LH upper corner
        ]

        for i in range(len(key_points)):
            # Position 1
            pos1_command = "pos1 " + str(key_points[i][0][0]) + "," + str(key_points[i][0][1]) + "," + str(
                key_points[i][0][2])
            self.send_command(pos1_command)

            # Position 2
            pos2_command = "pos2 " + str(key_points[i][1][0]) + "," + str(key_points[i][1][1]) + "," + str(
                key_points[i][1][2])
            self.send_command(pos2_command)


            self.send_command("set oak_planks")


        self.send_command("pos1 " + str(key_points[0][1][0]) + "," + str(key_points[0][1][1]) + "," + str(
            key_points[0][1][2]))
        self.send_command("pos2 " + str(key_points[3][1][0]) + "," + str(key_points[3][1][1]) + "," + str(
            key_points[3][1][2]))
        self.send_command("replace " + material + " oak_planks")










world_edit = WorldEditAutomationClass()
world_edit.print_to_gui("Starting the WorldEdit automation process")



world_edit.replace_old_materials()

# Put copper on the roofs
# world_edit.replace_roofs_with_copper((-1618,66,76),(-1540,97,-23))
# world_edit.replace_roofs_with_copper((-1518,63,11),(-1381,119,-187))
# world_edit.replace_roofs_with_copper((-1389,127,-122),(-1302,65,-304))
# world_edit.replace_roofs_with_copper((-1304,138,-119),(-1496,66,121))

# Change all roofs
# world_edit.oxidize_copper_roofs((-1656,60,160),(-1250,143,-333))
# world_edit.clean_copper_roofs((-1656,60,160),(-1250,143,-333))

# Test undo function
# world_edit.undo_commands()


world_edit.print_to_gui("The WorldEdit automation process is now complete")
exit(1)

