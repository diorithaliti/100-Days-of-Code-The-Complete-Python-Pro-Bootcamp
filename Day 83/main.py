#tic tac toe

import random
import pandas

restart_game = {'x': {0: '-', 1: '-', 2: '-'}, 'y': {0: '-', 1: '-', 2: '-'}, 'z': {0: '-', 1: '-', 2: '-'}}

colums = ["x","y","z"]
data =pandas.read_csv("table.csv",index_col='Id')
data_dict = data.to_dict()
print(data)

can_continue = True
while can_continue == True:



    #user
    is_blank = True
    while is_blank == True:
        # input
        user_column = input("Please input the column (x,y,z):\n")
        user_row = input("Please input row(0,1,2):\n")
        if data.loc[int(user_row)][str(user_column)] == "-":
            data.loc[int(user_row)][str(user_column)] = 'x'
            is_blank = False


    #chech if user win
    if data['x'][0] == 'x' and data['x'][1] =='x' and data['x'][2] == 'x':
        print("You win")
        can_continue = False
        break
    elif data['y'][0] == 'x' and data['y'][1] =='x' and data['y'][2] == 'x':
        print("You win")
        can_continue = False
        break
    elif data['z'][0] == 'x' and data['z'][1] =='x' and data['z'][2] == 'x':
        print("You win")
        can_continue = False
        break
    elif data['x'][0] == 'x' and data['y'][0] =='x' and data['z'][0] == 'x':
        print("You win")
        can_continue = False
        break
    elif data['x'][1] == 'x' and data['y'][1] =='x' and data['z'][1] == 'x':
        print("You win")
        can_continue = False
        break
    elif data['x'][2] == 'x' and data['y'][2] =='x' and data['z'][2] == 'x':
        print("You win")
        can_continue = False
        break
    elif data['x'][0] == 'x' and data['y'][1] =='x' and data['z'][2] == 'x':
        print("You win")
        can_continue = False
        break
    elif data['x'][2] == 'x' and data['y'][1] =='x' and data['z'][0] == 'x':
        print("You win")
        can_continue = False
        break


    #robot
    is_blank_r = True
    while is_blank_r == True:
        random_row = random.randint(0, 2)
        random_column = random.choice(colums)
        if data.loc[int(random_row)][str(random_column)] == "-":
            data.loc[int(random_row)][str(random_column)] = 'o'
            is_blank_r = False
        print(data)

    #chech if robot win
    if data['x'][0] == 'o' and data['x'][1] =='o' and data['x'][2] == 'o':
        print("Robot win")
        can_continue = False
        break
    elif data['y'][0] == 'o' and data['y'][1] =='o' and data['y'][2] == 'o':
        print("Robot win")
        can_continue = False
        break
    elif data['z'][0] == 'o' and data['z'][1] =='o' and data['z'][2] == 'o':
        print("Robot win")
        can_continue = False
        break
    elif data['x'][0] == 'o' and data['y'][0] =='o' and data['z'][0] == 'o':
        print("Robot win")
        can_continue = False
        break
    elif data['x'][1] == 'o' and data['y'][1] =='o' and data['z'][1] == 'o':
        print("Robot win")
        can_continue = False
        break
    elif data['x'][2] == 'o' and data['y'][2] =='o' and data['z'][2] == 'o':
        print("Robot win")
        can_continue = False
        break
    elif data['x'][0] == 'o' and data['y'][1] =='o' and data['z'][2] == 'o':
        print("Robot win")
        can_continue = False
        break
    elif data['x'][2] == 'o' and data['y'][1] =='o' and data['z'][0] == 'o':
        print("Robot win")
        can_continue = False
        break

    if  data['x'][0] != '-' and data['x'][1] !='-' and data['x'][2] == '-' and data['z'][0] != '-' and data['z'][1] !='-' and data['z'][2] == '-'and data['y'][0] != '-' and data['y'][1] !='-' and data['y'][2] == '-':
        print("Draw")
        can_continue = False
        break