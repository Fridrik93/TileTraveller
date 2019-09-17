# línur eru skilgreindar sem 1, 2, 3 og dálkar 5, 6, 7 
# myndum hafa max left sem 5 og max right sem 7 ef náð er 7 eða 5 verður talan bara 5 eða 7
# hafa max up sem 1 og max down sem 3 ef náð er 1 eða 3 verður talan 1 eða 3 

#check ef x skipun er innan marka

direction = ""
def limit_check_x(input_x, input_y):
    max_left = 1
    max_right = 3
    
    if input_x < max_left:
        input_x = max_left
    elif input_x > max_right:
        input_x = max_right
    max_up= 3
    max_down = 1
    if input_y < max_down:
        input_y = max_down
    elif input_y > max_up:
        input_y = max_up
    return input_x, input_y

   
# check if in victory position
#  def victory_check(input_x, input_y):
#      max_x= 3
#      max_y= 3
#      if input_x == max_x and input_y == max_y:
#         print('Voctory!')       

def direction(pos_x, pos_y, direction):
    if direction.lower() == "w":
        if pos_x == 3 and pos_y == 2:
            pos_x = pos_x
        elif pos_x == 3 and pos_y == 3:
            pos_x = pos_x
        else:
            pos_x -= 1
    elif direction.lower() == "e":
        if pos_x == 1 and pos_y == 3:
            pos_x = pos_x
        elif pos_x == 2 and pos_y == 3:
            pos_x = pos_x
        elif pos_x == 2 and pos_y == 2:
            pos_x = pos_x
        else:
            pos_x +=1
    elif direction.lower() == "n":
        if pos_x == 2 and pos_y == 2:
            pos_y = pos_y
        else:
            pos_y += 1
    elif direction.lower() == "s":
        if pos_x == 2 and pos_y == 1:
            pos_y = pos_y
        pos_y -= 1
    else:
        print("Not a valid direction!")
    return pos_x, pos_y

#op= original position
op_x = 1
op_y = 1

dire = input("You can travel: ")

new_x, new_y = direction(op_x, op_y, dire)

x, y = limit_check_x(new_x, new_y)

print(x, y)

while True:
    dire = input("You can travel: ")
    new_x, new_y = direction(op_x, op_y, dire)
    x, y = limit_check_x(new_x, new_y)
    print(x, y)
