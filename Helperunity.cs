using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MCTS_TTT
{
    public class Helper
    {
        MemoryCopy memoryCopy = new MemoryCopy();

        public unsafe void CopyBytes(byte[] destination, byte[] source)
        {
            fixed (byte* pdes = destination, psource = source) memoryCopy.MemCpy(pdes, psource, 9);
        }

        public unsafe byte[] CopyBytes(byte[] source)
        {
            byte[] ret = new byte[source.Length];
            fixed (byte* pdes = ret, psource = source) memoryCopy.MemCpy(pdes, psource, 9);
            return ret;
        }

        public static byte[] GetBytes(string str)
        {
            return System.Text.Encoding.UTF8.GetBytes(str);
        }

        public static string GetString(byte[] bytes)
        {
            return System.Text.Encoding.UTF8.GetString(bytes);
        }
    }
}
