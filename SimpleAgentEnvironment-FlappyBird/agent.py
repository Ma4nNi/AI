import random

class SimpleAgent:
    def __init__(self,envState=None):
        self.env=envState
    
    def chooseAction(self, gameState):
        #print("jumpiinngg", gameState)
        option = (int)(random.random()*10)
        if(option<1):
            return 119
        return None


