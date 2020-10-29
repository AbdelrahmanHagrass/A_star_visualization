import Colors
import pygame
import math
import queue
class Node:
    def __init__(self,row,col,width,TRow):
            self.row=row;
            self.col=col;
            self.x=row*width;
            self.y=col*width;
            self.adj=[];
            self.width=width
            self.TRow=TRow;
            self.color=Colors.Black;
    def get_pos(self):
        return self.row,self.col;
    def is_off(self):
        return self.color==Colors.Blue;
    def is_on(self):
        return self.color==Colors.Orange;
    def is_barrier(self):
        return self.color==Colors.Grey;
    def is_start(self):
        return self.color==Colors.Green;
    def is_end(self):
        return self.color==Colors.Cyan
    def reset(self):
        self.color=Colors.Black;
    def Turn_off(self):
        self.color=Colors.Blue;
    def Turn_on(self):
        self.color=Colors.Orange
    def make_barrier(self):
        self.color=Colors.Grey;
    def make_start(self):
        self.color=Colors.Orange;
    def make_end(self):
        self.color=Colors.Red;
    def Make_Path(self):
        self.color=Colors.Green;
    def draw(self,Window):
        pygame.draw.rect(Window,self.color,(self.x,self.y,self.width,self.width));
    def update_adj(self,grid):
        self.adj=[];
        if(self.row<self.TRow-1 and not grid[self.row+1][self.col].is_barrier()):
            self.adj.append(grid[self.row+1][self.col]);
        if (self.row >0 and not grid[self.row -1][self.col].is_barrier()):
            self.adj.append(grid[self.row - 1][self.col]);
        if (self.col < self.TRow - 1 and not grid[self.row][self.col+1].is_barrier()):
            self.adj.append(grid[self.row][self.col+1]);
        if (self.row >0  and not grid[self.row ][self.col-1].is_barrier()):
            self.adj.append(grid[self.row][self.col-1]);


    def __lt__(self, other):
        return False;






