from tkinter import *
from tkinter import font
import random
import copy
import operator
class Info(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=500, height=100)
        police = font.Font(self, size=20, family='Arial')
        self.t = Label(self, text="Yellows' turn", font=police)
        self.t.grid(sticky=NSEW, pady=20)

class Piont(object):
    def __init__(self, x, y, can, colour="white", bg="red"):
        self.can = can
        self.x = x
        self.y = y
        self.colour = colour

        self.tour = 1
        
        self.r = 30
        self.piont = self.can.create_oval(self.x+10,self.y+10,self.x+61,self.y+61,fill=colour,outline="blue")
        
        

    def changecoloureur(self, colour):
        self.can.itemconfigure(self.piont, fill=colour)
        self.colour = colour

class Terrain(Canvas):
    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=500, height=400, bg="blue")

        self.player = 1
        self.colour = "yellow"
        self.p = []
        self.perm = True
        
        for i in range(0, 340, int(400/6)):
            liste_rangee = []
            for j in range(0, 440, int(500/7)):
                liste_rangee.append(Piont(j, i ,self))
                
            self.p.append(liste_rangee)
        
        self.bind("<Button-1>", self.detCol)

    def detCol(self, event):
        if self.perm:
            col = int(event.x/71)
            if(self.player==2):
                print("£££REEEDDDDD TUURRRNRNNNNNNNN$$$$$$\n\n")
                col = minimax2(self.p)#minimax returns the column in which to use our move
            row = 0
            
            row = 0
            while row < len(self.p):            
                if self.p[0][col].colour == "red" or self.p[0][0].colour == "yellow":
                    break
                
                if self.p[row][col].colour == "red" or self.p[row][col].colour == "yellow":
                    self.p[row-1][col].changecoloureur(self.colour)
                    break
                
                elif row == len(self.p)-1:
                    self.p[row][col].changecoloureur(self.colour)
                    break

                
                if self.p[row][col].colour != "red" and self.p[row][col].colour != "yellow":
                    row+=1

            endgaame = checkWinCondition(self.p)
            if(endgaame[0]):
                info.t.config(text = endgaame[1]+"is the winner!")
                return

            if self.player == 1:
                self.player = 2
                info.t.config(text="Reds turn")
                self.colour = "red"

            elif self.player == 2:
                self.player = 1
                info.t.config(text="Yellows turn")
                self.colour = "yellow"

def emulateMove(newMatrix, move, color): ##THIS SHOULDONLY BE CALLED WITH THE COMPUTER MOVES
    for row in range(len(newMatrix)-1,0,-1):
        if newMatrix[row][move].colour == "white":
            newMatrix[row][move].colour = color
            break
    return newMatrix

def copyMatrix(matrix):
    newList = []
    for i in range(len(matrix)):
        newList.append([])
        for j in range(len(matrix[i])):
            newList[i].append(type('',(object,),{'colour':matrix[i][j].colour})() ) 
    return newList
    
def checkWinCondition(matrix):
    for row in matrix:#iterate over the rows
        hor = hasHorizontalWinCondition(row)
        if(hor[0]):
            break
    for i in range(7):
        ver = hasVerticalWinCondition(matrix,i)
        if(ver[0]):
            break
    #print("HORIZONTAL", hor)
    #print("VERTICAL", ver)
    return hor if hor[0] else (ver if ver[0] else hor)

def hasVerticalWinCondition(matrix, columnNo):
    redCounter=0
    yellowCounter=0
    winner= "none"
    conditionMet = False
    for row in matrix:
        if row[columnNo].colour == "red":
            redCounter+=1
            yellowCounter = 0
        elif row[columnNo].colour=="yellow":
            redCounter =0
            yellowCounter+=1
        else:
            redCounter = 0
            yellowCounter = 0
        if(redCounter==4):
            conditionMet = True
            winner = "red"
            break
        elif(yellowCounter == 4):
            conditionMet = True
            winner = "yellow"
            break
    return (conditionMet, winner)

def hasHorizontalWinCondition(row):
    redCounter=0
    yellowCounter=0
    winner= "none"
    conditionMet = False
    for cell in row:
        if cell.colour == "red":
            redCounter+=1
            yellowCounter = 0
        elif cell.colour=="yellow":
            redCounter =0
            yellowCounter+=1
        else:
            redCounter = 0
            yellowCounter = 0
        if(redCounter==4):
            conditionMet = True
            winner = "red"
            break
        elif(yellowCounter == 4):
            conditionMet = True
            winner = "yellow"
            break
    return (conditionMet, winner)

def hasDiagonalWinCondition(grid): #TODO
    redCounter=0
    yellowCounter=0
    for row in range(0,2): # right diagonals
        grid[row]
    return False

def getScore(winTuple, currentColor): #wintuple is (bool, string)
    if(winTuple[0]):
        if(currentColor==winTuple[1]):
            return 10
        else:
            return -10
    return 0

def minimax2(matrix, player="red"):
    availableMoves = []
    for i in range(7): ##GET AVAILABLE MOVES WITH THIS LOOP- possible moves are a column from 0 to 6
        if matrix[0][i].colour == "white":
            availableMoves.append(i)
    print("available:",availableMoves);
    bestMoves = bestImmediateMoves(matrix,availableMoves, "red")
    print("Bes red moves:",bestMoves)
    moveDict = {}
    for move in bestMoves[0]:
        moveDict[move] = bestMoves[1]
    print("First moveset: ",moveDict)
    yellowMoves = []
    maxYScore=0
    for move in bestMoves[0]:
        yellowMoves =[]
        nMax= emulateMove(copyMatrix(matrix), move, "red")
        newAvailables = []
        for i in range(7): ##GET AVAILABLE MOVES WITH THIS LOOP- possible moves are a column from 0 to 6
            if nMax[0][i].colour == "white":
                newAvailables.append(i)
        bestYellows = bestImmediateMoves(nMax,newAvailables,"yellow")
        if(bestYellows[1] > maxYScore):
            yellowMoves = bestYellows[0]
            maxYScore = bestYellows[1]
        elif(maxYScore==bestYellows[1]):
            for mv in bestYellows[0]:
                if(mv not in yellowMoves):
                    yellowMoves.append(mv)
        #print("Best Yellow moves for red:",bestYellows)
    print("final yellows: ",yellowMoves)
    for movimiento in yellowMoves:
        if movimiento in moveDict.keys():
            moveDict[movimiento] +=maxYScore
        else:
            moveDict[movimiento] = maxYScore
    print("Final moveset",moveDict)
    bestMoves = [k for k,v in moveDict.items() if v == max(moveDict.values())]
    print("bestMoves",bestMoves)
    return random.choice(bestMoves)

def bestImmediateMoves(matrix, moves, color):
    #print("available:",moves)
    maxScore = 0
    bestMoves = []
    for move in moves:
        currScore = getScore(checkWinCondition(emulateMove(copyMatrix(matrix), move, color)),color)
        #print(currScore," for move",move)
        if(currScore>maxScore):
            bestMoves = [move]
            maxScore=currScore
        elif(currScore==maxScore):
            bestMoves.append(move)
    #print("BESTS",bestMoves)
    return (bestMoves, maxScore)

def minimax(matrix, player="red", level=0):
    print("\t MINIMAX LEVEL:",level)
    moves = {}
    availableMoves = []
    otherplayer = "yellow" if player=="red" else "red"
    for i in range(7): ##GET AVAILABLE MOVES WITH THIS LOOP- possible moves are a column from 0 to 6
        if matrix[0][i].colour == "white":
            availableMoves.append(i)
    print("DISPoNIBLES:",availableMoves)
    for move in availableMoves:
        print("\move: ",move)
        newMatrix =  emulateMove(copyMatrix(matrix), move,"red")
        moves[move] = getScore(checkWinCondition(newMatrix),player) 
        if(level<2):
            moves[move] +=  minimax(newMatrix,otherplayer, level+1)[1]
    print(moves)
    bestMove = 0
    if player=="red":
        bestMove = max(moves.items(), key=operator.itemgetter(1))[0]
    else:
        bestMove = min(moves.items(), key=operator.itemgetter(1))[0]
    if(level==0):
        print("MOVES",moves)
        print("BESTMOV:",bestMove)
    return (bestMove, moves[bestMove])  #possible moves are 0 to 7 and includes the score


root = Tk()
root.geometry("500x550")
root.title("Puissance 4 - V 1.0 -- Romain VAUSE")

info = Info(root)
info.grid(row=0, column=0)


t = Terrain(root)
t.grid(row=1, column=0)

def rein():
    global info
    info.t.config(text="")
    
    info = Info(root)
    info.grid(row=0, column=0)

    t = Terrain(root)
    t.grid(row=1, column=0)

Button(root, text="Play again", command=rein).grid(row=2, column=0, pady=30)

root.mainloop()

