using System;

 public class Gameunity
    {
        public int[,] board = new int[11,9]; 

        public void Restart()
        {
            board = new int[11,9];
        }

        public void Mark(int player, byte indexX,byte indexY)
        {
            if (board[indexY,indexX] != 0)
                throw new Exception("Tryed to mark an non empty slot");

            if (player == 1)
                board[indexY,indexX] = 1;
            else
                board[indexY,indexX] = 2;
        }

        public int[,] GetValidMoves()
        {
           int[,] moves = new int[11,9];

            for (int i = 0; i < 9; i++)
                for (int j = 0; j < 11; j++)
                        if (board[j, i] == 0)
                         moves.Add((byte)j,i);

            return moves;
        }

        public List<byte> GetValidMoves(byte[,] state)
        {
            List<byte> moves = new List<byte>();

            for (int i = 0; i < 9; i++)
                for (int j = 0; j < 11; j++)
                    if (state[j,i] == 0)
                    moves.Add((byte)j,i);

            return moves;
        }

        public int GetWinner()
        {
        if (board[7, 4] != 20)
            return 1;
        else if (board[1, 4] != 10)
            return 2;
        else return 0;
        }

        public int GetWinner(int[,] board)
        {
        if (board[7, 4] != 20)
            return 1;
        else if (board[1, 4] != 10)
            return 2;
        else return 0;
    }

        public bool IsTerminal(int[,] state)
        {
            return GetWinner(state) != 0;
        }

          }

