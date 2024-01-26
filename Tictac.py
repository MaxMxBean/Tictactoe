#Tictactoe
#with a terrible AI
#Author: MM
#Date: 19Oct2023
print("Welcometo TicTacToe, enter square number to place, e.g. '5'")
#print("123\n456\n789")

#Global Variables
no_winner = True
turns = 0
options = ["1","2","3","4","5","6","7","8","9"]
xchoice = 0
ochoice = 0
moves = ["1","2","3","4","5","6","7","8","9"]


#Functions
def win(moves):
    if moves [0]==moves[1]==moves[2] or moves[3]==moves[4]==moves[5] or moves[6]==moves[7]==moves[8] or moves[0]==moves[3]==moves[6] or moves[1]==moves[4]==moves[7] or moves[2]==moves[5]==moves[8] or moves[0]==moves[4]==moves[8] or moves[2]==moves[4]==moves[6]:
        return True
    else:
        return False

def playermove():
    while True:
        try:
            i=input('Select a valid move:')
            if i in moves:
                return i
        except:
            pass
        print("Invalid move, try again")

def printgrid(moves):
    print(moves[0:3])
    print(moves[3:6])
    print(moves[6:10])

#Main loop: Check if Winner-->Increment turns -->Take choice--> Check choice--> Remove from grid --> Print grid --> Check for winner

while win(moves)==False: 
    turns+=1
    if turns%2==0:
        ochoice=playermove()
        moves[int(ochoice)-1]= "o"
        options.remove(ochoice) 
        print("Turn:",turns, "Options:", options)
        printgrid(moves)
    else:
        xchoice=options[-1]
        options.remove(xchoice)
        moves[int(xchoice)-1]="x"
        print("Turn:",turns, "Options:", options)
        printgrid(moves)
else:
    print("We have a winner!")