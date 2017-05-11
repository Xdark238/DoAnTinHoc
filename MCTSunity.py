import copy
import math
class MCTSunity:
    class Node:
		parent = Node();
		parent = None;
                children = ;
                value = 0;
                visits = 0;
                action = [][];
                PlayerTookAction = 0;
                depth = 0;
                ignore = False;

		state= [][];

        def Node(parent, action,PlayerTookAction, depth):
            this.parent = parent;
            this.action = action;
            this.PlayerTookAction = PlayerTookAction;
            this.depth = depth;

	def Opponent( player):
			return (3 - player);
 
	def getInitNode():
			root = Node();
			root = Node(null, null, 1, 0);
			root.state[9, 4] = 20;
			root.state[1, 4] = 10;
			for  j in range(0,9):
				root.state[0, j] = 10 + j + 1;
				root.state[10, j] = 20 + 9 - j;
			root.action = copy.deepcopy(root.state);
			return root;
		
	def GetBestMove(Gameunity game, int player):
			Node root = getInitNode();
			startPlayer = player;

			root.state = copy.deepcopy(game.board);

			
			for  iteration in range(0,100):
				Node current = Selection(root, game);
				value = Rollout(current, game, startPlayer);
				Update(current, value);
				
			helper.CopyBytes(game.board, root.state);

			return BestChildUCB(root, 0).action;
		
		//#1. Select a node if 1: we have more valid feasible moves or 2: it is terminal 
		def Selection( current, Gameunity.game)
			while (!game.IsTerminal(current.state)):
				validMoves = game.GetNewValidBoards(current.state, current.PlayerTookAction);

				if (validMoves.Count > current.children.Count):
					return Expand(current, game);
				else:
					current = BestChildUCB(current, 1.44);
			return current;
		def SelectionIfNonStike(Node current, Gameunity game):
			while (!game.IsTerminal(current.state)):
				validMoves = game.GetNewValidBoards(ref current.state, current.PlayerTookAction);

				if (validMoves.Count > current.children.Count):
					return Expand(current, game);
				else:
					current = BestChildUCB(current, 1.44);
			return current;
		
		//#1. Helper
		def BestChildUCB(current, C):
			Node bestChild = null;
			double best = double.NegativeInfinity;

			for child in current.children:
			 UCB1 = ((double)child.value / (double)child.visits) + C * math.sqrt((2.0 * math.log((double)current.visits)) / (double)child.visits);

				if (UCB1 > best):
					bestChild = child;
					best = UCB1;
					return bestChild;

		//#2. Expand a node by creating a new move and returning the node
		def Expand(Node current, Gameunity game)
			helper.CopyBytes(game.board, current.state);

			validMoves = game.GetNewValidBoards(ref current.state, current.PlayerTookAction);

			for i in range(0,validMoves.math.count()):
				if (current.children.Exists(a => a.action == validMoves[i]))
					continue;
					playerActing = Opponent(current.PlayerTookAction);
					node = node();
					node = new Node(current, validMoves[i], playerActing, current.depth + 1);
					current.children.Add(node);

					game.setBoard(validMoves[i], playerActing);
					node.state = (int[,])validMoves[i].Clone();
					helper.CopyBytes(game.board, current.state);

					return node;
			
		#3. Roll-out. Simulate a game with a given policy and return the value
		def Rollout(current, game, startPlayer):
			helper.CopyBytes(game.board, current.state);
			if (game.GetWinner() == Opponent(startPlayer)):
				current.parent.value = int.MinValue;
				return 0;
				player = Opponent(current.PlayerTookAction);

				while (game.GetWinner() == 0)
				moves = game.GetNewValidBoards();
				 move = moves[r.Next(0, moves.Count)];
				player = Opponent(player);
				game.setBoard(move, player);            
				if (game.GetWinner() == startPlayer || game.GetWinner() == 3):
				return 1;


		def Update(current, value)
			do:
				current.visits++;
				current.value += value;
				current = current.parent;
			while (current != null);
