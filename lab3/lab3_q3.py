### Implementing and simulating multiplexers in PyRTL ###

import pyrtl

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare data inputs
# < add your code here >

a = pyrtl.Input(bitwidth=3, name='a')
b = pyrtl.Input(bitwidth=3, name='b')
c = pyrtl.Input(bitwidth=3, name='c')
d = pyrtl.Input(bitwidth=3, name='d')
e = pyrtl.Input(bitwidth=3, name='e')

# Declare control inputs
# < add your code here >

s = pyrtl.Input(bitwidth=3, name='s')

# Declare outputs 
# < add your code here >

o = pyrtl.Output(bitwidth=3, name='o')


# Describe your 5:1 MUX implementation
# < add your code here >

sel0 = s[2]
sel1 = s[1]
sel2 = s[0]


with pyrtl.conditional_assignment:
    with ((~sel0) & (~sel1) & (~sel2)):
        o |= a
    with ((~sel0) & (~sel1) & (sel2)):
        o |= b
    with ((~sel0) & (sel1) & (~sel2)):
        o |= c
    with ((~sel0) & (sel1) & (sel2)):
        o |= d
    with ((sel0) & (~sel1) & (~sel2)):
        o |= e


#o <<= temp1 | temp2 | temp3 | temp4 | temp5

# Simulate and test your design for 16 cycles using random inputs
# < add your code here >


sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

import random
for cycle in range(16):
    sim.step({
        'a': random.choice([0,1,2,3,4,5,6,7]),
        'b': random.choice([0,1,2,3,4,5,6,7]),
        'c': random.choice([0,1,2,3,4,5,6,7]),
        'd': random.choice([0,1,2,3,4,5,6,7]),
        'e': random.choice([0,1,2,3,4,5,6,7]),
        's': random.choice([0,1,2,3,4])
        })


print('--- 3-bit 5:1 MUX Simulation ---')
sim_trace.render_trace()
