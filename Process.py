import csv
import os

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 创建SMT文件夹
smt_folder = os.path.join(current_dir, 'SMT_info')
os.makedirs(smt_folder, exist_ok=True)

# 输入文件和输出文件的相对路径
input_file = os.path.join(current_dir, 'Partlist_test.txt')
output_file_bom = os.path.join(smt_folder, 'Partlist_BOM.csv')
output_file_pos = os.path.join(smt_folder, 'Partlist_Positions.csv')

# 初始化数据列表
bom_data = []
pos_data = []

# 读取并解析文件
with open(input_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        # 忽略空行、标题行和包含特定关键字的行
        if line.strip() and not (line.startswith('Part') or 
                                 line.startswith('Exported') or 
                                 line.startswith('EAGLE Version') or 
                                 line.startswith('Assembly variant')):
            parts = line.split()
            # 确保行中有足够的元素
            if len(parts) >= 6:
                designator = parts[0]
                value = parts[1]
                package = parts[2]
                
                # 提取位置和方向
                position = parts[-3:-1]  # 提取位置坐标
                x = position[0].strip('(')
                y = position[1].strip(')')
                orientation = parts[-1][1:]  # 移除R字符
                
                # 添加到BOM数据
                bom_data.append([value, designator, package])
                
                # 添加到位置信息数据
                # pos_data.append([part, f"{x}mm", f"{y}mm", 'T', orientation]) #添加mm单位版本
                pos_data.append([designator, f"{x}", f"{y}", 'T', orientation])

# 写入BOM CSV文件
with open(output_file_bom, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # 写入标题行 
    writer.writerow(['Value', 'Designator', 'Footprint'])   # 'Value', 'Designator(位号)', 'Footprint(封装)'
    for row in bom_data:
        writer.writerow(row)

# 写入CPL CSV文件 (位置信息)
with open(output_file_pos, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # 写入标题行
    writer.writerow(['Designator', 'Mid X', 'Mid Y', 'Layer', 'Rotation'])
    for row in pos_data:
        writer.writerow(row)

print("转换完成，CSV文件已生成：", output_file_bom, "和", output_file_pos)
