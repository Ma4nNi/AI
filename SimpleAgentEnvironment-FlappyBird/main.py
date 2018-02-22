from ple import PLE
from ple.games.flappybird import FlappyBird
from agent import SimpleAgent

game = FlappyBird()
p = PLE(game, fps=30, display_screen=True, force_fps=False)
p.init()

print(p.getActionSet())
myAgent = SimpleAgent(p.getActionSet())

nb_frames = 1000

for f in range(nb_frames):
	if p.game_over(): #check if the game is over
		p.reset_game()
	obs = p.getScreenRGB()
	action = myAgent.chooseAction(game.getGameState())
	#print(action)
	p.act(action)
