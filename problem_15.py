# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
###
###
grid = []
for i in range(20):
    if i == 0:
        grid.append([1])
    else:
        grid.append([0])
    for j in range(20):
        if j == 0:
            grid[i].append([1])
        else:
            grid[i].append([0])
for i in range(20):
    print(grid[i])
