'''
Character Picture Grid   Page:103 Chapter_4
Automate the boring stuff with python.
'''


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
# Draft
# str_0 = ''
# for y in range(9):
#     str_0 += grid[y][0]
#
# print(str_0)
#
# str_1 = ''
# for y in range(9):
#     str_1 += grid[y][1]
#
# print(str_1)

new = ['']*len(grid[0])
for x in range(len(grid[0])):
    for y in range(len(grid)):
        new[x] += grid[y][x]

for i in new:
    print(i)