#AI Map game
#help from tic tac toe game https://www.youtube.com/watch?v=5s_lGC2sxwQ&t=96s

#define board for game
board=['  ' for x in range(21)]

#define current position and position of coins
board[1]=" . "
board[2]=" . "
board[3]=" x "
currentPosition=3
board[4]=" . "
board[5]=" o "
board[6]=" o "
board[7]=" . "
board[8]=" . "
board[9]=" . "
board[10]=" . "
board[11]=" o "
board[12]=" . "
board[13]=" . "
board[14]=" . "
board[15]=" o "
board[16]=" . "
board[17]=" . "
board[18]=" o "
board[19]=" . "
board[20]=" . "

#winning variable
coinsFound=0

#-----------------------------------------------------------------------------------------

#Methods
def printboard():
    print('---------------------')
    print('|'+board[1]+'|'+board[2]+'|'+board[3]+'|'+board[4]+'|'+board[5]+'|')
    print('---------------------')
    print('|'+board[6]+'|'+board[7]+'|'+board[8]+'|'+board[9]+'|'+board[10]+'|')
    print('---------------------')
    print('|'+board[11]+'|'+board[12]+'|'+board[13]+'|'+board[14]+'|'+board[15]+'|')
    print('---------------------')
    print('|'+board[16]+'|'+board[17]+'|'+board[18]+'|'+board[19]+'|'+board[20]+'|')
    print('---------------------')

def coinFound():
    global coinsFound
    board[currentPosition]=" ~ "
    coinsFound=coinsFound+1
    print('coin found\n')
    print('Total coins found', coinsFound)    
    printboard()
    
def invalidMove(previousPosition):
    global currentPosition
    currentPosition=previousPosition
    print('invalid move')
    print('Current position is',currentPosition)
    playGame()
    
def playGame():
    global coinsFound
    while coinsFound!=5:
        print('Choose direction (UP, Down, Right, Left)')
        direction=input()
        
        global currentPosition,previousPosition
        previousPosition=currentPosition
        if(direction=="Up"):
            currentPosition=currentPosition-5
        elif(direction=="Down"):
           currentPosition=currentPosition+5
        elif(direction=="Right"):
            currentPosition=currentPosition+1
        elif(direction=="Left"):
            currentPosition=currentPosition-1
            
        print('current position is ',currentPosition)
        
        #invalid move
        if(currentPosition<=0):
            invalidMove(previousPosition)
            
        #if coin found
        if(board[currentPosition]==" o "):
            coinFound()
           
        else:
            #if coin not found
            print('coin not found\n enter direction again')
            playGame()
            
     #when while loop breaks  
    print('All coins found! congratulations')     

#-----------------------------------------------------------------------------------------    
#main    
if __name__ == "__main__":
   
    print('\n~~~~Game started~~~~\n')
    printboard()
    playGame()        
    print('exit game')
    input()
            
    





















