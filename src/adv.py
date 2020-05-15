import time
import sys
import os
from room import Room
from player import Player
from item import Item, Food, Weapon
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

logo = '''\t\n\n
                    ___           ___           ___                                               
     _____         /\  \         /\  \         /|  |                                              
    /::\  \       /::\  \       /::\  \       |:|  |                                              
   /:/\:\  \     /:/\:\  \     /:/\:\__\      |:|  |                                              
  /:/  \:\__\   /:/ /::\  \   /:/ /:/  /    __|:|  |                                              
 /:/__/ \:|__| /:/_/:/\:\__\ /:/_/:/__/___ /\ |:|__|____                                          
 \:\  \ /:/  / \:\/:/  \/__/ \:\/:::::/  / \:\/:::::/__/                                          
  \:\  /:/  /   \::/__/       \::/~~/~~~~   \::/~~/~                                              
   \:\/:/  /     \:\  \        \:\~~\        \:\~~\                                               
    \::/  /       \:\__\        \:\__\        \:\__\                                              
     \/__/         \/__/         \/__/         \/__/                                              
                    ___           ___           ___           ___           ___                   
     _____         /\__\         /\__\         /\__\         /\__\         /\  \                  
    /::\  \       /:/ _/_       /:/ _/_       /:/  /        /:/ _/_        \:\  \         ___     
   /:/\:\  \     /:/ /\__\     /:/ /\  \     /:/  /        /:/ /\__\        \:\  \       /\__\    
  /:/  \:\__\   /:/ /:/ _/_   /:/ /::\  \   /:/  /  ___   /:/ /:/ _/_   _____\:\  \     /:/  /    
 /:/__/ \:|__| /:/_/:/ /\__\ /:/_/:/\:\__\ /:/__/  /\__\ /:/_/:/ /\__\ /::::::::\__\   /:/__/     
 \:\  \ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\  \ /:/  / \:\/:/ /:/  / \:\~~\~~\/__/  /::\  \     
  \:\  /:/  /   \::/_/:/  /   \::/ /:/  /   \:\  /:/  /   \::/_/:/  /   \:\  \       /:/\:\  \    
   \:\/:/  /     \:\/:/  /     \/_/:/  /     \:\/:/  /     \:\/:/  /     \:\  \      \/__\:\  \   
    \::/  /       \::/  /        /:/  /       \::/  /       \::/  /       \:\__\          \:\__\  
     \/__/         \/__/         \/__/         \/__/         \/__/         \/__/           \/__/ '''

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

time.sleep(2)
print(logo)

intro = '\n\nI was a young teen, in search of finding a real demon!' + \
    ' I was told that this house was haunted by one!\n\n'

for char in intro:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.15)

name = input('\tWhat is your name, charmed one? \t')

player = Player(name, room['outside'])
print(f'\nWelcome {name}, you start your adventure from {player.current_room}')

while True:

    direction = input(
        '\nWhat direction would you like to go: N(orth), S(outh), E(ast), W(est), Q to quit! ').lower()

    if direction == 'n':
        next = player.current_room.n_to
        if next == None:
            print((f'\n\tYou can not go North, please choose a different direction!\n'))
        else:
            player = Player(name, next)
            print(player)

    elif direction == 's':
        next = player.current_room.s_to
        if next == None:
            print((f'\n\tYou can not go South, please choose a different direction!\n'))
        else:
            player = Player(name, next)
            print(player)

    elif direction == 'e':
        next = player.current_room.e_to
        if next == None:
            print((f'\n\tYou can not go East, please choose a different direction!\n'))
        else:
            player = Player(name, next)
            print(player)

    elif direction == 'w':
        next = player.current_room.w_to
        if next == None:
            print((f'\n\tYou can not go West, please choose a different direction!\n'))
        else:
            player = Player(name, next)
            print(player)

    elif direction == 'q':
        print('\nThe lurky demon of the mansion hears your wimpy footsteps. As you start to run away, the demons whispers chilling haunts luring you back ....... \n\n')
        break

    elif direction != 'n' or 's' or 'w' or 'e' or 'q':
        print('\n\tInvalid, try again using N, S, E, W')
