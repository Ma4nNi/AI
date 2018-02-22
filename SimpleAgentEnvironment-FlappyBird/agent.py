import random

class SimpleAgent:
    def __init__(self, envVariables ):
        self.env=envVariables
        print(self.env)
    
    def chooseRandomAction(self, gameState):
        #print(gameState)
        option = (int)(random.random()*2)
        if(option<1):
            #print("I JUMPED ON THE LAST STATE")
            return 119
        return None



    def shouldJump(self, gameState):
        movesUntilNextPipe = gameState['next_pipe_dist_to_player'] / 4 #Horizontal movement is 4px per frame
        if(gameState['player_y']< gameState['next_pipe_top_y']): #agent above the top pipe
            return False
        if(gameState['player_y']> gameState['next_pipe_bottom_y']):#agent below the lower pipe
            return True
        #If its here it should be in the middle
        pipeGap = gameState['next_pipe_bottom_y'] - gameState['next_pipe_top_y']
        if(movesUntilNextPipe < 7): #when jumping it takes 7 frames for the agent to stop ascending
            return True
            

    def chooseAction(self, gameState):
        if(self.shouldJump(gameState)):
            return 119
        return None
