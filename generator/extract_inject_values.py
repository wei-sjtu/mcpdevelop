import json
import os

# 定义JSON文件路径
json_file_path = os.path.join('inject_content', 'polynomial_results_20250903_113423.json')

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建完整的JSON文件路径
#full_json_path = os.path.join(script_dir, json_file_path)
full_json_path="D:\\mcpdevelop\\generator\\inject_content\\polynomial_results_20250903_113423.json"

try:
    # 读取JSON文件
    with open(full_json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 提取tool_id字段
    tool_id = None
    if 'parameters' in data and 'tool_id' in data['parameters']:
        tool_id = data['parameters']['tool_id']
    
    # 提取所有inject_Segment_i的值
    inject_values = []
    if 'results' in data:
        for item in data['results']:
            if 'inject_Segment_i' in item:
                inject_values.append(str(item['inject_Segment_i']))
    
    # 用分号连接所有inject_Segment_i值
    inject_values_str = ';'.join(inject_values)
    
    # 按照指定格式构建结果字符串
    result_string = f"tool_id: {tool_id}\ntool_seq: {inject_values_str}"
    
    # 打印结果
    print("提取的结果：")
    print(result_string)
    
    # 将结果保存到文件中
    output_file = os.path.join(script_dir, 'extracted_inject_values.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result_string)
    print(f"\n结果已保存到：{output_file}")
    
except FileNotFoundError:
    print(f"错误：找不到文件 {full_json_path}")
except json.JSONDecodeError:
    print(f"错误：JSON文件格式无效 {full_json_path}")
except Exception as e:
    print(f"发生错误：{str(e)}")