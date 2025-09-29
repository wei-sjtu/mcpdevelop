import json
import os
import sys

file_path = "Val_Instruction\ChartoNum_20250802_165539.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
       
# 提取groups数据
groups = data.get("groups", [])
       
# 提取numeric_value字段
numeric_values = []
for group in groups:
    # 检查每个组是否有numeric_value字段
    if "numeric_value" not in group:
        print(f"警告: 在组数据中找不到'numeric_value'字段: {group}")
        continue
            
    value = group["numeric_value"]
    numeric_values.append(value)
    
print(f"\n成功从 '{file_path}' 中提取 {len(numeric_values)} 个数值:")
print(numeric_values)
    
    
 
   
        


