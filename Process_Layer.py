# 本程序用于修改 Process.py 生成 POS 数据 Layer 层的快速修改

import pandas as pd
import os

# 读取CSV文件
# 文件夹(当前)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 文件夹(SMT)
smt_folder = os.path.join(current_dir, 'SMT_info')
os.makedirs(smt_folder, exist_ok=True)

input_file = os.path.join(smt_folder, 'Micro_Driver_POS.csv')
data = pd.read_csv(input_file)

# 要修改的元器件名称列表
components_to_modify = ["R7", "R11", "R15","R27","R31","R36"
                        ,"T1","T2","T3","T4","U$2"]

# 修改Layer列为"B"的元器件
data.loc[data['Designator'].isin(components_to_modify), 'Layer'] = 'B'

# 文件夹(SMT_Mod)
smt_mod_folder = os.path.join(current_dir, 'SMT_Mod')
os.makedirs(smt_mod_folder, exist_ok=True)

# 保存修改后的CSV文件
# output_file_path = os.path.join(smt_mod_folder, 'Micro_Driver_POS_Mod.csv')
output_file_path = os.path.join(smt_folder, 'Micro_Driver_POS_Mod.csv')
data.to_csv(output_file_path, index=False)

print(f"修改后的文件已保存到 {output_file_path}")

