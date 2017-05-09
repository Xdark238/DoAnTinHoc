using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;

namespace MCTS_TTT
{
    unsafe public class MemoryCopy
    {
        public delegate void MemCpyFunction(void* des, void* src, uint bytes);
        public readonly MemCpyFunction MemCpy;

        public MemoryCopy()
        {
            #region generate most efficient memory copy
            var dynamicMethod = new DynamicMethod
             (
                 "MemCpy",
                 typeof(void),
                 new[] { typeof(void*), typeof(void*), typeof(uint) },
                 typeof(Program)
             );

            var ilGenerator = dynamicMethod.GetILGenerator();

            ilGenerator.Emit(OpCodes.Ldarg_0);
            ilGenerator.Emit(OpCodes.Ldarg_1);
            ilGenerator.Emit(OpCodes.Ldarg_2);

            ilGenerator.Emit(OpCodes.Cpblk);
            ilGenerator.Emit(OpCodes.Ret);

            MemCpy = (MemCpyFunction)dynamicMethod
                        .CreateDelegate(typeof(MemCpyFunction));
            #endregion
        }
           
    }
}
