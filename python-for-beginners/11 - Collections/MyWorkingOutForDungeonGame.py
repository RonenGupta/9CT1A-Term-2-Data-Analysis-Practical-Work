# Define the dimensions of the dungeon
rows = 3
cols = 3

# Create a dungeon grid using a list of lists
grid = [['-' for _ in range(cols)] for _ in range(rows)]

# Initialize player position
x_row = 2
x_col = 2
grid[x_row][x_col] = 'X'  # Player represented by 'X'

# Initialize visited rooms counter
visited_rooms = 2

# Function to print the dungeon grid with player's current location
def print_dungeon_with_player():
    for r in range(rows):
        for c in range(cols):
            if r == x_row and c == x_col:
                print('X', end=' ')
            else:
                print(grid[r][c], end=' ')
        print()

# Print the initial dungeon with player's current location
print("Initial Dungeon:")
print_dungeon_with_player()

# Function to move the player and explore rooms
def explore_dungeon(direction):
    global x_row, x_col, visited_rooms

    # Check if all rooms have been visited
    if visited_rooms == (rows * cols):
        print("\nCongratulations! You have visited all rooms and won the game.")
        exit()

    # Clear current player position
    grid[x_row][x_col] = '*'

    # Update player position based on direction
    if direction == 'left' and x_col > 0:
        x_col -= 1
    elif direction == 'right' and x_col < cols - 1:
        x_col += 1
    elif direction == 'up' and x_row > 0:
        x_row -= 1
    elif direction == 'down' and x_row < rows - 1:
        x_row += 1

    # Check if the new position is a room
    if grid[x_row][x_col] == '-':
        visited_rooms += 1
        grid[x_row][x_col] = '*'

    # Print updated dungeon with player's current location
    print("\nAfter Move:")
    print_dungeon_with_player()

# Dungeon exploration loop
while True:
    direction = input("\nEnter direction (left/right/up/down) or 'exit' to quit: ").lower()
    if direction == 'exit':
        break
    elif direction in ['left', 'right', 'up', 'down']:
        explore_dungeon(direction)
    else:
        print("Invalid direction! Please enter left/right/up/down or 'exit'.")
