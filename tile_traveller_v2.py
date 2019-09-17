# Ask for input
# Validate
# Call Check walls in validation method
# Move
# Check for victory
# 
# 
NORTH = "(N)orth"
SOUTH = "(S)outh"
WEST = "(W)est"
EAST = "(E)ast"

pos_x, pos_y = 1, 1
game = True
direction = ""

# Returning constants depending on location
def guidance(pos_x, pos_y):
    guidance_string = ""
    if pos_y == 1:
        guidance_string = NORTH
    elif pos_x == 2 and pos_y == 2:
        guidance_string = WEST + " or " + SOUTH
    elif pos_x == 2 and pos_y == 3:
        guidance_string = WEST + " or " + EAST
    elif pos_x == 3 and pos_y == 2:
        guidance_string = NORTH + " or " + SOUTH
    else:
        if pos_x == 1:
            guidance_string = NORTH
        elif pos_y == 2:
            guidance_string = NORTH + " or " + EAST + " or " + SOUTH
        elif pos_y == 3:
            if pos_x == 1:
                guidance_string = SOUTH + " or " + EAST
            elif pos_x == 2:
                guidance_string = WEST + " or " + EAST
            else:
                guidance_string = WEST + " or " + SOUTH
    return "You can travel: " + guidance_string + "."
# Tries moving if check for walls succeeds, no walls are found in the way.
# Will return same values if pos_x or pos_y will go out of bounds
def move(pos_x, pos_y, direction):
    if direction.lower() == "n":
        if(check_wall(pos_x, pos_y, direction)):
            pos_x, pos_y = check_boundaries(pos_x, pos_y, direction)

    elif direction.lower() == "s":
        if(check_wall(pos_x, pos_y, direction)):
            pos_x, pos_y = check_boundaries(pos_x, pos_y, direction)

    elif direction.lower() == "w":
        if(check_wall(pos_x, pos_y, direction)):
            pos_x, pos_y = check_boundaries(pos_x, pos_y, direction)

    elif direction.lower() == "e":
        if(check_wall(pos_x, pos_y, direction)):
            pos_x, pos_y = check_boundaries(pos_x, pos_y, direction)
    return pos_x, pos_y

    
        
        
# returns True if there is no wall, False if there is
def check_wall(pos_x, pos_y, direction):    
    
    if direction.lower() == "n":
        if pos_x == 2 and pos_y == 2:
            print("Not a valid direction!")
            return False
        else:
            return True
    elif direction.lower() == "s":
        if pos_x == 2 and pos_y == 3:
            print("Not a valid direction!")
            return False
        else:
            return True
    elif direction.lower() == "w":
        if pos_x == 2 and pos_y == 1:
            print("Not a valid direction!")
            return False
        elif pos_x == 3 and pos_y == 1:
            print("Not a valid direction!")
            return False
        elif pos_x == 3 and pos_y == 2:
            print("Not a valid direction!")
            return False
        else:
            return True
    elif direction.lower() == "e":
        if pos_x == 1 and pos_y == 1:
            print("Not a valid direction!")
            return False
        elif pos_x == 2 and pos_y == 1:
            print("Not a valid direction!")
            return False
        elif pos_x == 2 and pos_y == 2:
            print("Not a valid direction!")
            return False
        else:
            return True
    
 # Checks and moves player if direction will not send them out of bounds
def check_boundaries(pos_x, pos_y, direction):
    if direction.lower() == "n":
        if pos_y != 3:
            pos_y += 1
        else:
            print("Not a valid direction!")
    elif direction.lower() == "s":
        if pos_y != 1:
            pos_y -= 1
        else:
            print("Not a valid direction!")
    elif direction.lower() == "w":
        if pos_x != 1:
            pos_x -= 1
        else:
            print("Not a valid direction!")
    elif direction.lower() == "e":
        if pos_x != 3:
            pos_x += 1
        else:
            print("Not a valid direction!")
    return pos_x, pos_y

# Checks if player is on the victory tile, if so then then changes the game bool value
def check_victory(pos_x, pos_y):
    game = True
    if pos_x == 3 and pos_y == 1:
        game = False
        print("Victory")
    return game

while game:
     print(guidance(pos_x, pos_y))
     direction = input("Direction: ")
     pos_x, pos_y = move(pos_x, pos_y, direction)
     game = check_victory(pos_x, pos_y)