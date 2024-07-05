import csv
import os

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 输入文件和输出文件的相对路径
input_file = os.path.join(current_dir, 'Partlist_test.txt')
output_file = os.path.join(current_dir, 'Partlist_JLCPCB.csv')

# 初始化数据列表
data = []

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
                part = parts[0]
                value = parts[1]
                package = parts[2]
                # 提取位置和方向
                position = f"({parts[-4]} {parts[-3]})"
                orientation = parts[-1][1:]  # 移除R字符
                data.append([part, value, package, position, orientation])

# 写入CSV文件
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # 写入标题行
    writer.writerow(['Designator', 'Value', 'Footprint', 'Mid X', 'Mid Y', 'Layer', 'Rotation'])
    for row in data:
        # 拆分位置成X和Y坐标
        x, y = row[3][1:-1].split()
        writer.writerow([row[0], row[1], row[2], x, y, 'Top', row[4]])

print("转换完成，CSV文件已生成：", output_file)
