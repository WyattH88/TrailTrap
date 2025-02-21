from graph import *
from solver import GameState, Minimax
#Create Graph
g = Graph(from_list=[(1,2,0),(1,3,0),(1,4,0),(2,3,0),(2,4,0),(3,4,0)])

g2 = Graph(from_list=[(1,2,0),(1,3,0)])

test = Minimax(GameState(g2))

print(test.winner())
