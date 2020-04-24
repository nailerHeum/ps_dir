from sys import stdin

N, M = [int(x) for x in stdin.readline().split(' ')]
maze = []
for i in range(N):
	maze.append([int(x) for x in map(int, stdin.readline()[:-1])])

def maze_runner(rowIdx, colIdx, count, preposition):
    if rowIdx == N - 1 and colIdx == M - 1:
        return count
    results = []
    routes = [(rowIdx + 1, colIdx), (rowIdx - 1, colIdx), (rowIdx, colIdx + 1), (rowIdx, colIdx - 1)]
    routes = list(filter(lambda x: N > x[0] >= 0 and M > x[1] >= 0 and maze[x[0]][x[1]] == 1, routes))
    for route in routes:
        if route[0] == preposition[0] and route[1] == preposition[1]:
            continue
        results.append(maze_runner(route[0], route[1], count + 1, (rowIdx, colIdx)))
    if len(results) == 0:
        return 100
    return min(results)
    

preposition = (0, 0)
result = maze_runner(0, 0, 0, preposition)
print(result + 1)