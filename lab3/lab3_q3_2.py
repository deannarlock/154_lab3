### Implementing and simulating multiplexers in PyRTL ###

import pyrtl

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare data inputs
# < add your code here >

a = pyrtl.Input(bitwidth=1, name='a')
b = pyrtl.Input(bitwidth=1, name='b')
c = pyrtl.Input(bitwidth=1, name='c')
d = pyrtl.Input(bitwidth=1, name='d')
e = pyrtl.Input(bitwidth=1, name='e')

# Declare control inputs
# < add your code here >

s = pyrtl.Input(bitwidth=3, name='s')
#s1 = pyrtl.Input(bitwidth=1, name='s1')
#s2 = pyrtl.Input(bitwidth=1, name='s2')

# Declare outputs 
# < add your code here >

o = pyrtl.Output(bitwidth=1, name='o')


# Describe your 5:1 MUX implementation
# < add your code here >

sel0 = s[2]
sel1 = s[1]
sel2 = s[0]

temp1 = ((~sel0) & (~sel1) & (~sel2)) & a
temp2 = ((~sel0) & (~sel1) & (sel2)) & b
temp3 = ((~sel0) & (sel1) & (~sel2)) & c
temp4 = ((~sel0) & (sel1) & (sel2)) & d
temp5 = ((sel0) & (~sel1) & (~sel2)) & e

o <<= temp1 | temp2 | temp3 | temp4 | temp5

# Simulate and test your design for 16 cycles using random inputs
# < add your code here >


sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

import random
for cycle in range(16):
    sim.step({
        'a': random.choice([0,1]),
        'b': random.choice([0,1]),
        'c': random.choice([0,1]),
        'd': random.choice([0,1]),
        'e': random.choice([0,1]),
        's': random.choice([0,1,2,3,4])
        })


print('--- 3-bit 5:1 MUX Simulation ---')
sim_trace.render_trace()
