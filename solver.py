


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

    def __init__(self,start: GameState):
        self.state = start


    def minimax(self,state:GameState)->bool:
        if state.currentPlayer():
            #player 1's turn
            for move in  state.moves():

                winner = self.minimax(state.makeMove(move))
                if winner:
                    return True

            #none of player 1's moves are winning moves
            return False    

        else:        
            #player 2's turn
            for move in  state.moves():
                winner = self.minimax(state.makeMove(move))
                if not(winner):
                    #player 2 can win from this position
                    return False

            #none of player 2's moves are winning moves
            return False    


