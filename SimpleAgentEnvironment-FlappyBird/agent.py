import random

class SimpleAgent:
    def __init__(self, envVariables ):
        self.env=envVariables
        print(self.env)
    
    def chooseRandomAction(self, gameState):
        option = (int)(random.random()*2)
        if(option<1):
            #print("I JUMPED ON THE LAST STATE")
            return 119
        return None



    def shouldJump(self, gameState):
        movesUntilNextPipe = gameState['next_pipe_dist_to_player'] / 4 #Horizontal movement is 4px per frame
        if(gameState['player_y']< gameState['next_pipe_top_y']): #agent above the top pipe
            print("above the pipe : ",gameState['player_y']," pipe ", gameState['next_pipe_top_y'])
            return False
        if(gameState['player_y']> gameState['next_pipe_bottom_y']):#agent below the lower pipe
            print("Below the pipe: ",gameState['player_y']," pipe ", gameState['next_pipe_bottom_y'])
            return True
        #If its here it should be in the middle
        pipeGap = gameState['next_pipe_bottom_y'] - gameState['next_pipe_top_y']
        print("In the middle of both pipes: ",gameState['player_y']," pipe ", gameState['next_pipe_bottom_y'],gameState['next_pipe_top_y']," with speed: ",gameState['player_vel'])
        if(gameState['player_y']+2*gameState['player_vel'] > gameState['next_pipe_bottom_y']-20):
            print("current thing: ",gameState['player_y']," bottom pipe ", gameState['next_pipe_bottom_y'],"top pipe ", gameState['next_pipe_top_y'])
            return True
            

    def chooseAction(self, gameState):
        print(gameState)
        if(self.shouldJump(gameState)):
            return 119
        return None
