using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MCTS_TTT
{
    public class MCTS
    {
        Helper helper = new Helper();
        Random r = new Random(1337);

        //THE EXECUTING FUNCTION
        public unsafe byte GetBestMove(Game game, int player, TreeView tv)
        {
            //Setup root and initial variables
            Node root = new Node(null, 0, Opponent(player),0);
            int startPlayer = player;

            helper.CopyBytes(root.state, game.board);

            //four phases: descent, roll-out, update and growth done iteratively X times
            //-----------------------------------------------------------------------------------------------------
            for (int iteration = 0; iteration < 1000; iteration++)
            {
                Node current = Selection(root, game);
                int value = Rollout(current, game, startPlayer);
                Update(current, value);
            }

            //Restore game state and return move with highest value
            helper.CopyBytes(game.board, root.state);

            //Draw tree
            DrawTree(tv, root);

            //return root.children.Aggregate((i1, i2) => i1.visits > i2.visits ? i1 : i2).action;
            return BestChildUCB(root, 0).action;
        }

        //#1. Select a node if 1: we have more valid feasible moves or 2: it is terminal 
        public Node Selection(Node current, Game game)
        {
            while (!game.IsTerminal(current.state))
            {
                List<byte> validMoves = game.GetValidMoves(current.state);

                if (validMoves.Count > current.children.Count)
                    return Expand(current, game);
                else
                    current = BestChildUCB(current, 1.44);
            }

            return current;
        }

        //#1. Helper
        public Node BestChildUCB(Node current, double C)
        {
            Node bestChild = null;
            double best = double.NegativeInfinity;

            foreach (Node child in current.children)
            {
                double UCB1 = ((double)child.value / (double)child.visits) + C * Math.Sqrt((2.0 * Math.Log((double)current.visits)) / (double)child.visits);

                if (UCB1 > best)
                {
                    bestChild = child;
                    best = UCB1;
                }
            }

            return bestChild;
        }

        //#2. Expand a node by creating a new move and returning the node
        public Node Expand(Node current, Game game)
        {
            //Copy current state to the game
            helper.CopyBytes(game.board, current.state);

            List<byte> validMoves = game.GetValidMoves(current.state);

            for (int i = 0; i < validMoves.Count; i++)
            {
                //We already have evaluated this move
                if (current.children.Exists(a => a.action == validMoves[i]))
                    continue;

                int playerActing = Opponent(current.PlayerTookAction);

                Node node = new Node(current, validMoves[i], playerActing, current.depth+1);
                current.children.Add(node);

                //Do the move in the game and save it to the child node
                game.Mark(playerActing, validMoves[i],validMoves[i]);
                helper.CopyBytes(node.state, game.board);

                //Return to the previous game state
                helper.CopyBytes(game.board, current.state);

                return node;
            }

            throw new Exception("Error");
        }

        //#3. Roll-out. Simulate a game with a given policy and return the value
        public int Rollout(Node current, Game game, int startPlayer)
        {
            helper.CopyBytes(game.board, current.state);

            //If this move is terminal and the opponent wins, this means we have previously made a move where the opponent can always find a move to win.. not good
            if (game.GetWinner() == Opponent(startPlayer))
            {
                current.parent.value = int.MinValue;
                return 0;
            }

            int player = Opponent(current.PlayerTookAction);

            //Do the policy until a winner is found for the first (change?) node added
            while (game.GetWinner() == 0)
            {
                //Random
                List<byte> moves = game.GetValidMoves();
                byte move = moves[r.Next(0, moves.Count)];
                game.Mark(player, move,move);
                player = Opponent(player);
            }

            if (game.GetWinner() == startPlayer || game.GetWinner() == 3)
                return 1;

            return 0;

        }

        //#4. Update
        public unsafe void Update(Node current, int value)
        {
            do
            {
                current.visits++;
                current.value += value;
                current = current.parent;
            }
            while (current != null);
        }

        public void DrawTree(TreeView tv, Node root)
        {
            tv.Nodes.Clear();
            int ch = AddChildrenTree(null, root, tv);
            tv.Nodes[0].Text += "(" + ch + ")";
        }

        public int AddChildrenTree(TreeNode parent, Node node, TreeView tv)
        {
            int ret = 0;

            if (parent == null)
                parent = tv.Nodes.Add(Helper.GetString(node.state), node.ToString());
            else
                parent = parent.Nodes.Add(Helper.GetString(node.state), node.ToString());

            foreach (Node child in node.children)
                ret+=AddChildrenTree(parent, child, tv);

            return node.children.Count+ret;
        }

        public int Opponent(int player)
        {
            if (player == 1)
                return 2;
            return 1;
        }

        public class Node
        {
            public Node parent = null;
            public List<Node> children = new List<Node>();
            public int value = 0;
            public int visits = 0;
            public byte action = 0;
            public byte PlayerTookAction = 0;
            public int depth = 0;
            public bool ignore = false;

            //Game specific
            public byte[,] state = new byte[11,9];

            public unsafe Node(Node parent, byte action, int PlayerTookAction, int depth)
            {
                this.parent = parent;
                this.action = action;
                this.PlayerTookAction = (byte)PlayerTookAction;
                this.depth = depth;
            }

            public override string ToString()
            {
                if (parent == null)
                    return "Root Node";

                return "Action: " + action + " Vi/Va: " + visits + "/" + value + " (Took Action: p" + PlayerTookAction + ") depth: " + depth;
            }
        }
    }
}
