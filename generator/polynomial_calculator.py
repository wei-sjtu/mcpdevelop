import json
import random
import os
import sys
import math
from datetime import datetime

def load_numeric_values(json_file):
    """从JSON文件中加载numeric_value列表"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('groups', [])
    except Exception as e:
        print(f"加载JSON文件出错: {e}")
        sys.exit(1)

def compute_polynomial(Nmal, coefficients, x):
    """
    计算多项式值: F(x; Nmal) = Nmal + a₁x + a₂x² + ... + aₙxⁿ
    """
    result = Nmal
    for i, a in enumerate(coefficients, start=1):
        # 使用整数运算保持精度
        if isinstance(result, int) and isinstance(a, int) and isinstance(x, int):
            result += a * (x ** i)
        else:
            result += a * (x ** i)
    return int(result)

def main():
    # 1. 获取输入参数
    if len(sys.argv) < 2:
        print("用法: python polynomial_calculator.py <json_file_path> [x_value] [degree]")
        print("示例: python polynomial_calculator.py conversion_results.json 2 5")
        sys.exit(1)
    
    json_file = sys.argv[1]
    x_value = int(sys.argv[2]) if len(sys.argv) > 2 else 1  # 默认x=2
    degree = int(sys.argv[3]) if len(sys.argv) > 3 else 3       # 默认多项式阶数3
    
    min_coef=1
    max_coef=10000000

    # 2. 加载数据
    groups = load_numeric_values(json_file)
    if not groups:
        print("错误: JSON文件中未找到有效的numeric_value数据")
        sys.exit(1)
    
    # 3. 随机生成系数 (a₁到a_{t-1})
    #coefficients = [random.randint(min_coef, max_coef) for _ in range(degree)]
    coefficients=[3688103]
    
    # 4. 对每个numeric_value计算多项式
    results = []
    for i, group in enumerate(groups):
        Nmal = group.get('numeric_value', 0)
        original_instruction=group.get('original_string')

        # 处理超大数值问题
        if isinstance(Nmal, int) and Nmal > 10**100:
            # 使用对数近似处理超大数
            log_result = math.log10(abs(Nmal))
            for j, a in enumerate(coefficients, start=1):
                log_result += math.log10(abs(a) * abs(x_value) ** j)
            result = math.copysign(10**log_result, Nmal)
        else:
            result = compute_polynomial(Nmal, coefficients, x_value)
        
        results.append({
            "original_instruction":original_instruction,
            "N_malicious": Nmal,
            "inject_Segment_i": result,
            "Seg_index": i
        })
    
    # 5. 准备结果数据结构
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_data = {
        "input_file": os.path.basename(json_file),
        "calculation_time": datetime.now().isoformat(),
        "parameters": {
            "tool_id": x_value,
            "polynomial_degree(t-1)": degree,
            "coefficients": coefficients,
            "coefficient_range": {"min": min_coef, "max": max_coef}
        },
        "results": results
    }
    
    # 6. 保存结果到新JSON文件
    output_file = f".\inject_content\polynomial_results_{timestamp}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n多项式计算完成! 结果已保存到: {os.path.abspath(output_file)}")
    print(f"参数配置:")
    print(f"  x值 = {x_value}")
    print(f"  多项式阶数(t-1) = {degree}")
    print(f"  系数 = {coefficients}")
    
    # 显示部分结果预览
    print("\n结果预览 (前3组):")
    for i, res in enumerate(results[:3]):
        print(f"组 {res['Seg_index']+1}:")
        print(f"  原始指令: {res['original_instruction']}")
        print(f"  原始值: {res['N_malicious']}")
        print(f"  注入值: {res['inject_Segment_i']}")
        if i < 2:
            print("-" * 60)

if __name__ == "__main__":
    main()