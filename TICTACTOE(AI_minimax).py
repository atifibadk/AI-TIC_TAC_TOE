from collections import deque
from copy import deepcopy
import os
global best
import timeit
best=0
board=[[None,None,None],[None,None,None],[None,None,None]]
q=deque()

def minimax(board,player,i=0,k=0):

    if CheckVictory(board,i,k):
        if player==True:
            return (-1,None)
        elif player==False:
            return (1,None)
    elif checkFinsh(board):
        return (0,None)
    elif(player==True):
        best=(-10,None)
        for x in range(3):
            for y in range(3):
                if board[x][y]==None:
                    Assignmove(board,x,y,player)
                    value=minimax(board,not player,x,y)[0]
                    board=q.pop()
                    if value>best[0]:
                        best=(value,(x,y))
    else:
        best=(10,None)
        for x in range(3):
            for y in range(3):
                if board[x][y]==None:
                    Assignmove(board,x,y,player)
                    value=minimax(board,not player,x,y)[0]
                    board=q.pop()
                    if value<best[0]:
                        best=(value,(x,y))

    return best
def Assignmove(Board,x,y,player):
    q.append(deepcopy(Board))
    Board[x][y]=player
def checkFinsh(l):
        for i in range(len(l)):
            for k in range(len(l[i])):
                if l[i][k] == None:
                    return False
                else:
                    gameFinshed=True
            if l[i][k]==None:
                break
        return gameFinshed
def CheckVictory(board, x, y):


        if board[x][0] == board[x][1] == board [x][2]:

            return True
        if board[0][y] == board[1][y] == board [2][y]:

            return True

        #check if previous move was on the main diagonal and caused a win
        if x == y and board[0][0] == board[1][1] == board [2][2]:

            return True

        #check if previous move was on the secondary diagonal and caused a win
        if x + y == 2 and board[0][2] == board[1][1] == board [2][0]:
            return True

        return False
def TakeInput(board):
    inputt=True
    while(inputt==True):
        move=raw_input("Human Move,Enter Cordinates\n")
        move=move.split()
        x=int(move[0])
        y=int(move[1])
        if board[x][y]==None:
            board[x][y]=True
            return board,x,y
        else:
            print "already filled"
def printBoard(a):
        print str(str(a[0])+'\n'+str(a[1])+'\n'+str(a[2]))
        print "-----------------------------------------------------"
def final():
    f=True
    while(f):
        l=raw_input("GAME FINSHED")
        f=True
if __name__ == '__main__':
    print '       /\\'   "  +====+ " "   x     x   ""  0 0 0 "
    print '      /  \\'   "  +====+" "      x      ""0 0 0 0 0"
    print '     /    \\'   "  +====+" "    x     x   ""  0 0 0  "
    print '    /      \\'   "  +====+" "    x  x  x   ""  0 0 0  "
    print '   / ====== \\'   "  +====+" "   x      x    ""  0 0 0  "
    print '  / ======== \\'   "  +====+" "    x  x  x   ""  0 0 0  "
    print ' /            \\'   "  +====+" "       x       ""  0 0 0  "
    print '/              \\'   "  +====+" "    x  x  x   ""  0 0 0  "
    while(True):

        board,i,k=TakeInput(board)
        printBoard(board)
        gameW=CheckVictory(board,i,k)

        if(gameW):
            print "HUMAN WON"
            raw_input("Press enter to exit ;)")

        gameD=checkFinsh(board)
        if(gameD):
            print "A DRAW"
            raw_input("Press enter to exit ;)")

        gameboard=deepcopy(board)
        start=timeit.timeit()
        V=minimax(board,False,i,k)
        end=timeit.timeit()
        print end-start
        print V
        board=gameboard
        moves=V[1]
        u=moves[0]
        v=moves[1]
        Assignmove(board,u,v,False)
        print "\n" * 10
        print '       /\\'   "  +====+ " "   x     x   ""  0 0 0 "
        print '      /  \\'   "  +====+" "      x      ""0 0 0 0 0"
        print '     /    \\'   "  +====+" "    x     x   ""  0 0 0  "
        print '    /      \\'   "  +====+" "    x  x  x   ""  0 0 0  "
        print '   / ====== \\'   "  +====+" "   x      x    ""  0 0 0  "
        print '  / ======== \\'   "  +====+" "    x  x  x   ""  0 0 0  "
        print ' /            \\'   "  +====+" "       x       ""  0 0 0  "
        print '/              \\'   "  +====+" "    x  x  x   ""  0 0 0  "

        print " AI MOVE"
        printBoard(board)

        comp=CheckVictory(board,u,v)
        if(comp):
            print "A.I WON"
            o=raw_input("Press enter to exit ;)")
            break


        gameD=checkFinsh(board)
        if(gameD):
            print "A DRAW"
            raw_input("Press enter to exit ;)")









