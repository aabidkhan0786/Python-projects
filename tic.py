board=[" " for x in range(10)]

def insertLetter(letter,pos):
    board[pos]=letter

def isSpaceFree(pos):
    return board[pos]==" "

def printBoard(board):

    print("   "+"|"+"   "+"|")
    print(" "+board[1]+" "+"|"+" "+board[2]+" "+"|"+" "+board[3]+" ")
    print("   "+"|"+"   "+"|")
    print("-----------")
    print("   "+"|"+"   "+"|")
    print(" "+board[4]+" "+"|"+" "+board[5]+" "+"|"+" "+board[6]+" ")
    print("   "+"|"+"   "+"|")
    print("-----------")
    print("   "+"|"+"   "+"|")
    print(" "+board[7]+" "+"|"+" "+board[8]+" "+"|"+" "+board[9]+" ")
    print("   "+"|"+"   "+"|")

def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True    

def isWinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or
    (b[4]==l and b[5]==l and b[6]==l) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l) or
    (b[1]==l and b[5]==l and b[9]==l) or
    (b[7]==l and b[5]==l and b[3]==l)) 


def playerMove():
     run = True
     while run:
        move=input("Enter a number from 1 to 9: ") 
        try:
            move=int(move)
            if move > 0 and  move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter("X",move) 
                else:
                    print("Sorry !! This space is occupied...")
            else:
                print("Please Enter a num from 1 to 9: ")   
        except:
            print("Please.. Type a number: ")

def compMove():
    possibleMoves= [x for x, letter in enumerate(board) if letter==" " and x!=0] 
    move=0

    for let in ["o", "X"]: 
        for i in possibleMoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if isWinner(boardcopy,let):
                    move = i
                    return move

    corner=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            corner.append(i)

    if len(corner) > 0:
        move = random(corner)
        return move
    if 5 in possibleMoves:
        move = 5
        return move

    edge=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            edge.append(i)

    if len(edge) > 0:
        move = random(edge)
        return move

def random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]    

def main():
    print(" Welcome to the Game !!") 
    printBoard(board)

    while not(isBoardFull(board)):
         if not(isWinner(board,"o")):
            playerMove()
            printBoard(board)
           
         else:
            print("Sorry !! U loss the game..")
            break
         if not(isWinner(board,"X")):
             move=compMove()
             if move == 0:
                 print("game tie ")
             else:
                 insertLetter("o",move)
                 print(" Computer Has Entered at " , move , ":")   
                 printBoard(board)
        
         else:
              print("Congo !! U won the game..")
              break
   

    if isBoardFull(board):
        print(" Game is Tie !! ")      



while True:
      x=input("Do u wanna play (y/n): ")
      if x.lower()=="y":
            board = [" " for x in range(10)]
            print("_____________________________")
            main()
      else:
            break      
