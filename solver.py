


class GameState(object):

    def __init__(self):
        pass

    def isTerminal(self)->bool:
        pass 

    def currentPlayer(self)->bool:
        """Returns true for player 1 and false for player 2"""
        pass

    def moves(self)->list[str]:
        pass

    def makeMove(self,move:str)->object:
        pass 


class Minimax(object):

    def __init__(self):
        self.state = None


    def minimax(self,state:GameState)->str:

        for move in  state.moves():
            winner = self.minimax(state.makeMove(move))

