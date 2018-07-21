import personObject
import stateOfTheWorld
import random

world = stateOfTheWorld.make_world()

turnNumber = 0

alive = []

alive.append(personObject.make_person(False))
while len(alive) <= world.influentialSize:
    alive.append(personObject.make_person(True))

world.print_world_state()

#while alive[0].alive:

