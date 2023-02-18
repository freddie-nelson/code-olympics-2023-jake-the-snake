
def find_char(maze, char):
  for row in range(len(maze)):
    for col in range(len(maze[row])):
      if maze[row][col] == char:
        return (row, col)

def find_neighbours(maze, row, col, path, dead_ends):
  neighbours = []

  for i in range(row-1, row+2):
    for j in range(col-1, col+2):
      if i < 0 or j < 0:
        continue

      if i >= len(maze) or j >= len(maze[i]):
        continue

      if i == row and j == col:
        continue

      # don't include diagonals
      if i == row-1 and j == col-1:
        continue
      if i == row-1 and j == col+1:
        continue
      if i == row+1 and j == col-1:
        continue
      if i == row+1 and j == col+1:
        continue

      # exclude walls
      if maze[i][j] != " " and maze[i][j] != "F":
        continue
      
      # exclude path and dead ends
      if (i, j) in path or (i, j) in dead_ends:
        continue

      neighbours.append((i, j))
  
  return neighbours

def solve(maze):
  jake = find_char(maze, "$")
  food = find_char(maze, "F")
  # print(jake, food)

  path = [jake]
  dead_ends = []

  while jake != food:
    neighbours = find_neighbours(maze, jake[0], jake[1], path, dead_ends)
    closest_to_food = None
    closest_distance = float("inf")

    # if hit a dead end, backtrack
    if len(neighbours) == 0:
      dead_ends.append(jake)
      jake = path.pop()
      maze[jake[0]][jake[1]] = "$"

    # find neighbour closest to food
    for neighbour in neighbours:
      # get the distance from the neighbour to the food
      distance = abs(food[0] - neighbour[0]) + abs(food[1] - neighbour[1])

      if distance < closest_distance:
        closest_distance = distance
        closest_to_food = neighbour
    
    path.append(closest_to_food)
    jake = closest_to_food
    maze[jake[0]][jake[1]] = "$"
  
  return path


def path_to_dirs(path):
  dirs = []

  for i in range(len(path)-1):
    row_diff = path[i+1][0] - path[i][0]
    col_diff = path[i+1][1] - path[i][1]

    if row_diff == -1:
      dirs.append("up")
    elif row_diff == 1:
      dirs.append("down")
    elif col_diff == -1:
      dirs.append("left")
    elif col_diff == 1:
      dirs.append("right")
  
  return ", ".join(dirs)



maze = [['+', '-', '+', '-', '+', '-', '+'],
['|', ' ', ' ', ' ', ' ', ' ', '|'],
['+', ' ', '+', '-', '+', ' ', '+'],
['|', ' ', ' ', 'F', '|', ' ', '|'],
['+', '-', '+', '-', '+', ' ', '+'],
['|', '$', ' ', ' ', ' ', ' ', '|'],
['+', '-', '+', '-', '+', '-', '+']]

path = solve(maze)
dirs = path_to_dirs(path)
# print(path)
print(dirs)
