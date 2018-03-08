from ple import PLE
from ple.games.flappybird import FlappyBird
from agent import SimpleAgent
import DFS.DFS as dfs

game = FlappyBird()
game.pipe_gap=150
p = PLE(game, fps=30, display_screen=True, force_fps=False)
p.init()

print(p.getActionSet())

flappyVariables= {"player_height":game.player.height, "pipe_gap":game.pipe_gap,"game_max_drop":game.player.MAX_DROP_SPEED,
	"game_gravity":game.player.GRAVITY,"game_flap_power":game.player.FLAP_POWER}
myAgent = SimpleAgent(flappyVariables)

nb_frames = 1000


for f in range(nb_frames):
	if p.game_over(): #check if the game is over
		exit()
		p.reset_game()
	obs = p.getScreenRGB()
	# if f == 1 :
	# 	steps = dfs.get_steps_by_frame(game.getGameState());
	# 	print("\n STEPS",steps)
	action = myAgent.chooseAction(game.getGameState())
	p.act(action)
#	p.act(None)