# Inputs
num = 3
containers = [3, 1, 2]
itemSize = 3
itemsPerContainer = [1, 2, 3]
cargoSize = 4
together = []

# Output: 9
for i, items in enumerate(containers):
    for _ in range(items):
        together.append(itemsPerContainer[i])

print(together)
print(sum(sorted(together[-cargoSize:])))