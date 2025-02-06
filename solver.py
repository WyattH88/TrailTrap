from graph import *


class GameState(object):
    
    def __init__(graph):
        """pass in a graph for the game."""
        self.graph = graph
        self.round = 0
        self.P1Pos
        self.P2Pos

    
    def isTerminal(self)->bool:
        """returns true if no moves are available."""
        return self.moves == []

    def currentPlayer(self)->bool:
        """Returns true for player 1 and false for player 2"""
        if(self.round%2==1):
            return True
        else:
            return False

    def moves(self)->list[str]:
        """Returns a list of available edges that the current player can take"""
        #No moves made
        if(self.P1Pos == null):
            return self.graph.edges()
        else:
            #P1 turn
            Moves
            if(self.currentPlayer):
                Moves =  self.graph.edges(from_node=P1Pos)
            #P2 turn
            else:
                Moves = self.graph.edges(from_node=P2Pos)
        
        #filter used edges (edge value is 0 for not used and 1 for used)
            returns = []
            #makes a array of edges you can take
            for i in Moves:
                 if Moves[i] == 0:
                    returns.append(Moves[i])
            return returns
        

    def makeMove(self,move:str)->object:
        """returns the gamestate with the move taken"""
        
        #incrment the turn conuter
        self.round += 1
        
        #Update player position
        if(self.currentPlayer):
            #p1 turn 
            self.P1pos = move.charAt(1)
        else:
            #p2 turn
            self.P2pos = move.charAt(1)
        
        #change the used edge to a 1 for used
        self.graph.add_edge(move.charAt(0),move.charAt(1),value=1)
        #return the new gamestate object
        return self


class Minimax(object):

    def __init__(self):
        self.state = None


    def minimax(self,state:GameState)->str:

        for move in  state.moves():
            winner = self.minimax(state.makeMove(move))

