from graphics import *
from enum import Enum
import random


class STATUS(Enum):
    DEAD = 0
    ALIVE = 1

class cell:
    def __init__(self, square, status):
        self.square = square
        self.status = status
        self.next_state = 0       

def check_neighbors(x, y, squares):
    live_neighbors = 0
    
    if (x != 0):
        live_neighbors += squares[x-1][y].status
        if (y != 0):
            live_neighbors += squares[x-1][y-1].status
            live_neighbors += squares[x][y-1].status
        if (y != len(squares)-1):
            live_neighbors += squares[x-1][y+1].status
            live_neighbors += squares[x][y+1].status
                    
    if (x != len(squares)-1):
        live_neighbors += squares[x+1][y].status
        if (y != 0):
            live_neighbors += squares[x+1][y-1].status
        if (y != len(squares)-1):
            live_neighbors += squares[x+1][y+1].status 
    
    return live_neighbors

def tick_update(cell, neighbors):
    if cell.status == 1:
        if (neighbors >=2 and neighbors <= 3):
            cell.square.setFill("orange")
            cell.next_state = 1
        else:
            cell.square.setFill("white")
            cell.next_state = 0
    else:
        if (neighbors == 3):
            cell.next_state = 1
            cell.square.setFill("orange")

        
def main():
    win = GraphWin("My Circle", 500, 500)
    s_arr = []
    s_cols = []
    
    for i in range(50):
        s_cols = []
        
        for j in range(50):
            color = random.randrange(0, 5, 1)
            s_cols.append(cell(Rectangle(Point(10*i,10*j), Point(10+10*i,10+10*j)), color == 1))
            
            if (color == 1):    
                s_cols[-1].square.setFill('orange')
                s_cols[-1].status = 1
            else:
                s_cols[-1].status = 0
                 
        s_arr.append(s_cols)
        
    for i in range(50):
        for j in range(50):
            s_arr[i][j].square.draw(win)
            
    while 1:        
        for i in range(50):
            for j in range(50): 
                neighbors = check_neighbors(i, j, s_arr)
                tick_update(s_arr[i][j], neighbors)   
        for i in range(50):
            for j in range(50):
                s_arr[i][j].status = s_arr[i][j].next_state

    win.getMouse() # pause for click in window
    win.close()
main()
