from graph import *
from GraphPractice import GameState
#Create Graph
g = Graph()


#node = vertex
# dict vtx: {vtxs edges to}
#this is C3 to do testing on
g.from_list([(1,2,0), (2,3, 0), (3,1, 0)])

game1 = GameState(g)

#tests
print("test 1: currentPlayer should be 1, Output true")
if(game1.currentPlayer()):
    print("true")
else:
    print("false")

print("test 2: isTerminal sould be false, Output false")
if(game1.isTerminal()):
    print("true")
else:
    print("false")

print("test 3: returning the list of moves, Output (1,2,0), (2,3, 0), (3,1, 0)]")
print(game1.moves(game1))

print("test 4: Updates current player when advancing the gamestate, Output false")
game2 = game1.makeMove(game1, "12")
if(game2.currentPlayer()):
    print("true")
else:
    print("false")

print("test 5: Updates moves when advancing the gamestate, Output [(2,3, 0), (3,1, 0)]")
print(game2.moves(game2))

print("test 6: Updates currentplayer when updating the gamestate again, Output True")
game3 = game2.makeMove(game2, "23")
if(game3.currentPlayer()):
    print("true")
else:
    print("false")

print("test 7: Updates moves when gamestate advances Output none")
if(game3.moves(game3)==""):
    print("none")
else:
    print(game3.moves(game3))

print("test 8: returns true when games state is termial Output true")
if(game3.isTerminal()):
    print("true")
else:
    print("false")