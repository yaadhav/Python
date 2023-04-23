# FUNCTION TO DISPLAY BOARD
def display_board(board):

    print('\n'*100)

    for ind in range(7,0,-3):
        print(f"           {board[ind]} | {board[ind+1]} | {board[ind+2]} ")

        if ind>3 :
            print("          -----------")
    print('')


# FUNCTION TO GET PLAYER DETAILS
def player_input():

    print("\n       WELCOME TO TIC-TAC-TOE\n")
    player1_name=input("Player 1 - Enter Your Name : ").capitalize()
    player2_name=input("Player 2 - Enter Your Name : ").capitalize()

    player1=''

    print('')    
    while player1 not in ['X','O']:
        player1=input(f"{player1_name} - Do You Want Be X or O : ")
    
        if player1 not in ['X','O']:
            print("\nPlease Enter X or O !")

    if player1=='X':
        players=[player1_name, player2_name, 0, 0]
    else:
        players=[player2_name, player1_name, 0, 0]

    print(f"{players[0]} will be X and {players[1]} will be O")

    return players


# FUNCTION TO PLACE THE MARKER
def place_marker( chance, filled, players):
    position=''

    if chance%2==1:
        print(f"{players[0]}'s TURN")
    else:
        print(f"{players[1]}'s TURN")

    while position.isdigit()==False or int(position) not in range(1,10) or int(position) in filled:
        position=input(f"Choose Your Postion (1-9): ")
    
        if position.isdigit()==False:
            print("\nYou Are Allowed ONLY to Enter NUMBERS !")

        if position.isdigit() and int(position) not in range(1,10):
            print("\nPlease Enter a Number WITHIN THE RANGE 1 to 9 !")

        if int(position) in filled:
            print("\nThat Position is Already Filled !")

    return int(position)


# FUNCTION TO CHECK A WINNER
def check_list( board, checklist):

    for ind in range(1,10,3):
        if board[ind:ind+3]==checklist:
            return True
    for ind in range(1,4):
        if board[ind::3]==checklist:
            return True
    if board[1:10:4]==checklist or board[3:8:2]==checklist:
        return True
    
    return False

def check_winner( board, players):

    winner=''
    xlist=['X','X','X']
    olist=['O','O','O']

    if check_list( board, xlist):
        winner=players[0]
        players[2]+=1
    elif check_list( board, olist):
        winner=players[1]
        players[3]+=1

    if len(winner)>0 :
        print(f"GAME OVER ! {winner} WINS THE GAME !\n{players[0]}:{players[2]} & {players[1]}:{players[3]}\n")
        return True
    if chance==9 :
        print(f"THE GAME ENDED IN DRAW !\n{players[0]}:{players[2]} & {players[1]}:{players[3]}\n")
    
    return False


# FUNCTION TO MAKE CHANGES IN THE BOARD
def change_board( board, chance):
    if chance%2==1 :
        board[position]='X'
    else:
        board[position]='O'


# FUNCTION TO START THE GAME
def start_the_game(players):
    print(f"\n{players[0]} Will Start The Game")
    input("Press Enter When You Are Ready ! ")

# FUNCTION TO CONTINUE THE GAME
def game_on():
    choice=''

    print('')
    while choice not in ['1','2', '3']:
        choice=input(f"Do You Want to do :\n1.Continue Next Round\n2.Change Players\n3.Exit\nChoose 1,2,3 : ")
    
        if choice not in ['1','2', '3']:
            print("\nPlease Enter Only 1, 2, 3 !")

    return int(choice)
    

# PROGRAM BEGINS
cont=2

while cont==2:
    players=player_input()
    cont=1

    while cont==1:
        board=['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        filled=[]
        over=False

        start_the_game(players)
        display_board(board)

        for chance in range(1,10) :        
            position=place_marker( chance, filled, players)
            change_board( board, chance)
            display_board(board)
            filled.append(position)

            over=check_winner( board, players)
            if over:
                break

        cont=game_on()

        players=[players[1], players[0], players[3], players[2]]

    