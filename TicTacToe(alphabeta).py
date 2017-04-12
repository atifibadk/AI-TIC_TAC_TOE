from collections import deque
from copy import deepcopy
import timeit
import os
global best
best=0
board=[[None,None,None],[None,None,None],[None,None,None]]
q=deque()

def minimax(board,player,alpha=-10,beta=10,i=0,k=0):

    if CheckVictory(board,i,k):
        if player==True:
            return (-1,None)
        elif player==False:
            return (1,None)
    elif checkFinsh(board):
        return (0,None)
    elif(player==True):
        best=(alpha,None)
        for x in range(3):
            for y in range(3):
                if board[x][y]==None:
                    Assignmove(board,x,y,player)
                    value=minimax(board,not player,alpha,10,x,y)[0]
                    board=q.pop()
                    if value>alpha:
                        alpha=value
                        best=(alpha,(x,y))
                    if best[0] >= beta:
                        return beta,(x,y)



    else:
        best=(beta,None)
        for x in range(3):
            for y in range(3):
                if board[x][y]==None:
                    Assignmove(board,x,y,player)
                    value=minimax(board,not player,-10,beta,x,y)[0]
                    board=q.pop()
                    if value<beta:
                        beta=value
                        best=(beta,(x,y))
                    if beta <= alpha:
                        return alpha,(x,y)





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
        move=raw_input("Enter Cordinates")
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
def game(board):
    while(True):
        print '       /\\'   "  +====+ " "   x     x   ""  0 0 0 "
        print '      /  \\'   "  +====+" "      x      ""0 0 0 0 0"
        print '     /    \\'   "  +====+" "    x     x   ""  0 0 0  "
        print '    /      \\'   "  +====+" "    x  x  x   ""  0 0 0  "
        print '   / ====== \\'   "  +====+" "   x      x    ""  0 0 0  "
        print '  / ======== \\'   "  +====+" "    x  x  x   ""  0 0 0  "
        print ' /            \\'   "  +====+" "       x       ""  0 0 0  "
        print '/              \\'   "  +====+" "    x  x  x   ""  0 0 0  "
        board,i,k=TakeInput(board)
        printBoard(board)
        gameW=CheckVictory(board,i,k)

        if(gameW):
            print "HUMAN WON"
            break
        gameD=checkFinsh(board)
        if(gameD):
            print "A DRAW"
            break
        gameboard=deepcopy(board)
        start=timeit.timeit()
        V=minimax(board,False,-2,2,i,k)
        end=timeit.timeit()
        print end-start
        print V
        board=gameboard
        moves=V[1]
        u=moves[0]
        v=moves[1]
        Assignmove(board,u,v,False)
        print "\n" * 100
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
            break

        gameD=checkFinsh(board)
        if(gameD):
            print "A DRAW"
            break
    return

game(board)
raw_input("Any Key to Exit")



