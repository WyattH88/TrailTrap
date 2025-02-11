from graph import *


class GameState(object):
    
    def __init__(self, graph):
        """pass in a graph for the game."""
        self.graph = graph
        self.round = 1
        self.P1Pos = -1
        self.P2Pos = -1

    
    def isTerminal(self)->bool:
        """returns true if no moves are available."""
        return self.moves() == []

    def currentPlayer(self)->bool:
        """Returns true for player 1 and false for player 2"""
        if(self.round%2==1):
            return True
        else:
            return False

    def moves(self)->list[str]:
        """Returns a list of available edges that the current player can take"""
        #No starting position
        Moves = []
        if(self.P1Pos == -1 or self.P2Pos == -1):
            Moves = self.graph.edges()
        else:
            #P1 turn
            if(self.currentPlayer()):
                Moves =  self.graph.edges(from_node=self.P1Pos)
            #P2 turn
            else:
                Moves = self.graph.edges(from_node=self.P2Pos)
        
        #filter used edges (edge value is 0 for not used and 1 for used)
        returns = []
            #makes a array of edges you can take
        for i in Moves:
            if i[2] == 0:
                returns.append(i)
        return returns
        

    def makeMove(self,move:str)->object:
        """returns the gamestate with the move taken, returns false if the move is invalid"""
        #change the move string into a more useful tuple
        move =  move.strip("()").split(',')
        move = (int(move[0]), int(move[1]))

        #Check the move is valid
        error = False
        #Check move is from the players position
        if(self.currentPlayer()):
            #P1
            if(move[0]!=self.P1Pos and self.P1Pos != -1):
                error = True
        else:
            #P2
            if(move[0]!=self.P2Pos and self.P2Pos != -1):
                error = True
        #check the edge is not already used or does not exist
        if(self.graph.edge(move[0],move[1]) != 0):
            error = True
        #TODO use error

        #Update player position
        if(self.currentPlayer()):
            #p1 turn 
            self.P1Pos = int(move[1])
        else:
            #p2 turn
            self.P2Pos = int(move[1])
        
        #change the used edge to a 1 for used (add changes to replace if the edge is to and from the same nodes)
        self.graph.add_edge(int(move[0]),int(move[1]),value=1)
        # #incrment the turn conuter
        self.round += 1
        #return the new gamestate object
        return self


class Minimax(object):

    def __init__(self):
        self.state = None


    def minimax(self,state:GameState)->str:

        for move in  state.moves():
            winner = self.minimax(state.makeMove(move))

