"""
There are three towers: Origin, Buffer, and Destination
The task is to move all disks from Origin to Buffer (in the same ascending order as in the beginning)

Algorithm:
    1. Move top (n-1) disks from Origin to Buffer
    2. Move top from Origin to Destination
    3. Move top (n-1) disks from Buffer to Destination

- All three steps are done recursively for each n and finally we get the result
"""


def steps_tower_hanoi(num_disks, origin, destination, buffer):
    if num_disks == 1:
        print(f'Move top disk from {origin} to {destination}')
        return

    steps_tower_hanoi(num_disks-1, origin, buffer, destination)
    print(f'Move top disk from {origin} to {destination}')
    steps_tower_hanoi(num_disks-1, buffer, destination, origin)


origin, destination, buffer = 'Origin', 'Destination', 'Buffer'
steps_tower_hanoi(4, origin, destination, buffer)
