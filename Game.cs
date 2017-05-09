using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MCTS_TTT
{
    public class Game
    {
        public byte[,] board = new byte[11,9]; 
        public void Restart()
        {
            board = new byte[11,9];
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

        public List<byte> GetValidMoves()
        {
            List<byte> moves = new List<>();

            for (int i = 0; i < 9; i++ )
                for (int j=0;j<11;j++)
                    if (board[j,i] == 0)
                        moves.Add((byte)i,j);    
            return moves;
        }

        public List<byte> GetValidMoves(byte[,] state)
        {
            List<byte> moves = new List<byte[,]>();

            for (int i = 0; i < 9; i++)
                for(int j=0;i<11;j++)
                 if (state[j,i] == 0)
                    moves.Add((byte)i,j);

            return moves;
        }

        public int GetWinner()
        {
           /*
            * 
            * 
            * 
            */
        }

        public int GetWinner(byte[,] board)
        {
           /*
            * 
            * 
            * 
            */
        }

        public bool IsTerminal(byte[,] state)
        {
            return GetWinner(state) != 0;
        }

        public void Draw()
        {
           /*
            Console.WriteLine("--------------------");

            for (int i = 0; i < 3; i++)
                for (int j=0;j<11;j++)
                Console.Write(board[j,i].ToString() + "-");

            Console.Write("\r\n");

            for (int i = 3; i < 6; i++)
                for (int j=0;j<11;j++)
                Console.Write(board[j,i].ToString() + "-");

            Console.Write("\r\n");

            for (int i = 6; i < 9; i++)
                for (int j=0;j<11;j++)
                Console.Write(board[j,i].ToString() + "-");

            Console.WriteLine("\r\n--------------------");
            */
        }
    }
}
