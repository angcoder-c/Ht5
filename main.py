'''
Hoja de trabajo 5
Fecha 24/02/2025
'''

import simpy
import random

# enviroment
env = simpy.Environment()

# container
container = simpy.Container(env, init=100, capacity=100)

var = random.expovariate(1/25)
print(container)
print(var)