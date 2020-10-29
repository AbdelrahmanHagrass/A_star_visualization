from Node import Node
import pygame
import math
import queue
import Colors
def h(p1,p2):
    x1,y1=p1;
    x2,y2=p2;
    return abs(x2-x1)+abs(y1-y2);
def make_grid(rows,width):
    grid=[];
    gap=width//rows;
    for i in range(rows):
        grid.append([]);
        for j in range(rows):
            node=Node(i,j,gap,rows);
            grid[i].append(node);

    return grid;
def draw_grid(Window,rows,width):
    gap=width//rows;
    for i in range(rows):
        pygame.draw.line(Window,Colors.Grey2,(0,i*gap),(width,i*gap));
        for j in range(rows):
            pygame.draw.line(Window,Colors.Grey2,(j*gap,0),(j*gap,width))
def draw(Window,grid,rows,width):

    for row in grid:
        for node in row:
          node.draw(Window);
    draw_grid(Window,rows,width);
    pygame.display.update();

def get_clicked_pos(pos,rows,width):
    gap=width//rows;
    y,x=pos;
    row=y//gap;
    col=x//gap;
    return row,col;
def main(Window,width):
    rows=50;
    grid=make_grid(rows,width);
    start=None;
    end=None;
    run=True;
    started=False;
    while run:

        draw(Window,grid,rows,width);

        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                run=False;
            if started:
                continue;
            pos = pygame.mouse.get_pos();
            row, col = get_clicked_pos(pos, rows, width)
            node = grid[row][col];
            if(pygame.mouse.get_pressed()[0]):
                if not start:
                    start=node;
                    start.make_start();
                elif not end:
                    end=node
                    end.make_end();
                elif node!=start and node !=end:
                    node.make_barrier();
            elif(pygame.mouse.get_pressed()[2]):
                node.reset();
                if(node==start):
                    start=None;
                elif node==end:
                    end=None;
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_SPACE and not started):
                    for row in grid :
                        for node in row:
                            node.update_adj(grid);
                    #started=True;
                    algorithm(lambda : draw(Window,grid,rows,width),grid,start,end);



    pygame.quit();
def algorithm(draw,grid,start,end):
    count=0;
    open_set=queue.PriorityQueue();
    open_set.put((0,count,start));
    parent={};
    g_score={node:float("inf") for row in grid for node in row};
    g_score[start]=0;
    f_score = {node: float("inf") for row in grid for node in row};
    f_score[start] = h(start.get_pos(),end.get_pos());
    open_set_hash={start};
    while(not open_set.empty()):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit();

        current = open_set.get()[2];
        open_set_hash.remove(current);

        if(current==end):
            reconstruct_path(parent,current,draw);
            return True;
        for adj in current.adj:
            temp_g_score=g_score[current]+1;
            if(temp_g_score<g_score[adj]):
                parent[adj]=current;
                g_score[adj]=temp_g_score;
                f_score[adj]=temp_g_score+h(adj.get_pos(),end.get_pos());
                if(adj not in open_set_hash):
                    count+=1;
                    open_set.put((f_score[adj],count,adj));
                    open_set_hash.add(adj);
                    adj.Turn_on();
        draw();
        if(current!=start):
            current.Turn_off();
    return False;
def reconstruct_path(parent,current,draw):
    while current in parent:
        current=parent[current];
        current.Make_Path();
        draw();