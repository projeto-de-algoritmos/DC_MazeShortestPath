import pygame

import networkx as nx

import random

import time

import heapq

try:
    pygame.init()
except:
    print("Erro. Programa não inicializado")


WIDTH = 500
HEIGHT = 600
FPS = 30

tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("MazegenPRIM")


# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
RED = (255, 0, 0)

w=20

# build the grid
def build_grid(x, y, w):
    x = 0
    y = 0 
    for i in range(1,21):
        x = 20                                                            
        y = y + 20                                                        
        for j in range(1, 21):
            pygame.draw.line(tela, WHITE, [x, y], [x + w, y])           
            pygame.draw.line(tela, WHITE, [x + w, y], [x + w, y + w])   
            pygame.draw.line(tela, WHITE, [x + w, y + w], [x, y + w])   
            pygame.draw.line(tela, WHITE, [x, y + w], [x, y])           
            x = x + 20                                                    


def up(y, x):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, GREEN, (x + 1, y - 20 + 1, 19, 39), 0)        
    pygame.display.update()                                              
    #time.sleep(2)

def down(y, x):   
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, GREEN, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()
    #time.sleep(2)


def left(y, x):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, GREEN, (x - 20 +1, y +1, 39, 19), 0)
    pygame.display.update()
    #time.sleep(2)


def right(y, x):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, GREEN, (x +1, y +1, 39, 19), 0)
    pygame.display.update()
    #time.sleep(2)


def redup(y, x):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, RED, (x + 1, y - 20 + 1, 19, 39), 0)        
    pygame.display.update()                                              
    #time.sleep(2)

def reddown(y, x):   
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, RED, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()
    #time.sleep(2)


def redleft(y, x):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, RED, (x - 20 +1, y +1, 39, 19), 0)
    pygame.display.update()
    #time.sleep(2)


def redright(y, x):
    x=20*(x+1)
    y=20*(y+1)
    pygame.draw.rect(tela, RED, (x +1, y +1, 39, 19), 0)
    pygame.display.update()
    #time.sleep(2)

#Random DFS

G = nx.grid_2d_graph(20,20)
#Graph of the mst(edge = 1 means it connects the two nodes)
GMST = nx.grid_2d_graph(20,20)

for (x, y) in GMST.edges():
    GMST.edges[x, y]['weight'] = 0

def randUnvisitedNeighbor(vertex):
    unvNeigh = []
    neigh = G[vertex]
    for (x, y) in neigh:
        if G.nodes[(x, y)] != {'visited': 1} :
            unvNeigh.append((x, y))

    if len(unvNeigh) >= 1:
        chosenVertex = random.choice(unvNeigh)

    else:
        chosenVertex = False

    return chosenVertex

def moveCell(vertex, nextVertex):
    (x, y) = vertex
    (x2, y2) = nextVertex

    if x == x2:
        if y < y2:
            time.sleep(.05)
            right(x, y)
        else:
            time.sleep(.05)
            left(x, y)
    else:
        if x < x2:
            time.sleep(.05)
            down(x, y)
        else:
            time.sleep(.05)
            up(x, y)

#Instead of iterating through the neigbors it chooses one randomly
def randomDFS(vertex):
    G.nodes[vertex]['visited'] = 1
    nextVertex = randUnvisitedNeighbor(vertex)

    while nextVertex:
        moveCell(vertex, nextVertex)
        randomDFS(nextVertex)
        nextVertex = randUnvisitedNeighbor(vertex)
    
#MST MAZE
def randomEdgesWeight():
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(0,100)
#=====================================================================================
def Prim():
    h = []
    s = []
    a = []
    i =0
    rep=-1
    temp = []
    for (x, y) in G.nodes():
        a.append(101)
        heapq.heappush(h, (a[20*x + y], (x, y)))

    while(h != []):
        heapq.heapify(h)
        u = heapq.heappop(h)
        if rep == -1:
            u = (0, (0,0))
        if rep != -1:
            for (x, y) in G[u[1]]:
                if (x ,y) in s:
                    temp.append((x, y))

            lesser = -1
            lesserxy = 0
            for (x, y) in temp:
                if lesser < a[20*x + y]:
                    lesser = a[20*x + y]
                    lesserxy = (x, y)
            moveCell(u[1], lesserxy)
            GMST.edges[u[1], lesserxy]['weight'] = 1
            temp = []

        rep = 1
        s.append(u[1])
        neigh = G[u[1]]
        for (x, y) in neigh:
            if (x, y) not in s:
                if G.edges[u[1],(x, y)]['weight'] < a[20*x + y]:
                    a[20*x + y] = G.edges[u[1],(x, y)]['weight']
                    for i in range(len(h)):
                        if h[i][1] == (x, y):
                            h[i] = (a[20*x + y], (x, y))      
                            break          
#====================================================================================
def DCShortestPath(N, xo, yo, xd, yd, xf, yf, contr, distance=0):
    print("xo")
    print(xo)
    print("yo")
    print(yo)
    print("xd")
    print(xd)
    print("yd")
    print(yd)
    print("contr")
    print(contr)
    if xd > 19 or yd > 19:
        return 400
    
    if xd < 0 or yd < 0:
        return 400

    if xo > 19 or yo > 19:
        return 400
    
    if xo < 0 or yo < 0:
        return 400
    
    if xd == 19 and yd == 19:
        return distance
    
    if (xo != xd or yo != yd) and GMST.edges[(xo, yo),(xd, yd)]['weight'] == 0:
        return 400

    else:

        if contr == -1:
            return min(DCShortestPath(N, xd, yd, xd+1, yd, xf, yf, 0, distance +1), DCShortestPath(N, xd, yd, xd, yd+1, xf, yf, 1,distance +1), DCShortestPath(N, xd, yd, xd-1, yd, xf, yf, 2,distance +1), DCShortestPath(N, xd, yd, xd, yd-1, xf, yf, 3,distance +1))    
        
        if contr == 0:
            return min(DCShortestPath(N, xd, yd, xd+1, yd, xf, yf, 0, distance +1), DCShortestPath(N, xd, yd, xd, yd+1, xf, yf, 1,distance +1), DCShortestPath(N, xd, yd, xd, yd-1, xf, yf, 3,distance +1))    

        if contr == 1:
            return min(DCShortestPath(N, xd, yd, xd+1, yd, xf, yf, 0, distance +1), DCShortestPath(N, xd, yd, xd, yd+1, xf, yf, 1,distance +1), DCShortestPath(N, xd, yd, xd-1, yd, xf, yf, 2,distance +1))    
          
        if contr == 2:
            return min(DCShortestPath(N, xd, yd, xd, yd+1, xf, yf, 1,distance +1), DCShortestPath(N, xd, yd, xd-1, yd, xf, yf, 2,distance +1), DCShortestPath(N, xd, yd, xd, yd-1, xf, yf, 3,distance +1))    

        if contr == 3:
            return min(DCShortestPath(N, xd, yd, xd+1, yd, xf, yf, 0, distance +1), DCShortestPath(N, xd, yd, xd-1, yd, xf, yf, 2,distance +1), DCShortestPath(N, xd, yd, xd, yd-1, xf, yf, 3,distance +1))    


def createMaze():
    startVertex = (0, 0)
    randomDFS(startVertex)

build_grid(40, 0, 20) 
#createMaze()
randomEdgesWeight()
Prim()
print(DCShortestPath(20, 0, 0, 0, 0, 19, 19, -1, distance))

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    pygame.display.update()

pygame.quit()