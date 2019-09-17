# línur eru skilbreindar sem 1, 2, 3 og dálkar 5, 6, 7 
# myndum hafa max left sem 5 og max right sem 7 ef náð er 7 eða 5 verður talan bara 5 eða 7
# hafa max up sem 1 og max down sem 3 ef náð er 1 eða 3 verður talan 1 eða 3 

#check ef x skipun er innan marka
position_x =0
def limit_check_x(input):
    max_left = 5
    max_right = 7
    if input < max_left:
        input = max_left
    elif input > max_right:
        input = max_right
    return input 

# check ef y skipun er innan marka
def limit_check_y(input):
    max_up= 3
    max_down = 1
    if input < max_down:
        input = max_down
    elif input > max_up:
        input = max_up
    return input
    
# check if in victory position
def victory_check(input_x, input_y):
    max_x= 7
    max_y= 3
    if input_x == max_x and input_y == max_y:
        print('Voctory!')       


def direction(pos_x, pos_y, direction):
    if direction.lower == "w":
        pos_x -= 1
    elif direction.lower == "e":
        pos_x +=1
    elif direction.lower == "n":
        pos_y += 1
    elif direction.lower == "":
        pos_y -= 1
    else:
        print("Not a valid direction!")
    return pos_x, pos_y

#op= original position
op_x = 5
op_y = 1

direction= input("You can travel: ")