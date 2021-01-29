import math

num = 5 
power = [4, 2, 8, 3, 5]
tasks = 19

time = 0
while tasks > 0:
    max_power = max(power)
    index = power.index(max_power)
    tasks -= max_power
    time += 1
    power[index] = math.floor(max_power/2)

print(time)