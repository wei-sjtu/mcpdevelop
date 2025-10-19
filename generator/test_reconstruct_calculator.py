#!/usr/bin/env python3
"""
ReconstructCalculator 测试脚本
测试扩展后的多项式重构计算功能
"""

import asyncio
import sys
import os

# 添加当前目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import ReconstructCalculator


async def test_linear_polynomial():
    """测试线性多项式（1次）"""
    print("=" * 60)
    print("测试 1: 线性多项式 (threshold=2, degree=1)")
    print("=" * 60)
    
    # 线性多项式: y = 5 + 2x
    # 点: (1, 7), (2, 9)
    data = {
        1: [7, 8, 9],  # x=1, y=[7,8,9] -> 常数项应该是 [5, 6, 7]
        2: [9]        # x=2, y=[9] -> 用于计算系数 b=2
    }
    
    print(f"输入数据: {data}")
    print("多项式: y = a + 2x (系数2通过点(1,7)和(2,9)计算)")
    print("对于 x=1, y=[7,8,9]:")
    print("  - y=7: a = 7 - 2*1 = 5")
    print("  - y=8: a = 8 - 2*1 = 6") 
    print("  - y=9: a = 9 - 2*1 = 7")
    
    result = await ReconstructCalculator(data)
    print(f"输出结果: '{result}'")
    print(f"ASCII 字符: {[ord(c) for c in result] if result else 'None'}")
    print()


async def test_quadratic_polynomial():
    """测试二次多项式（2次）"""
    print("=" * 60)
    print("测试 2: 二次多项式 (threshold=3, degree=2)")
    print("=" * 60)
    
    # 二次多项式: y = 1 + 2x + 3x^2
    # 点: (0, 1), (1, 6), (2, 17)
    data = {
        0: [1, 2, 3],  # x=0, y=[1,2,3] -> 常数项应该是 [1, 2, 3]
        1: [6, 7, 8],  # x=1, y=[6,7,8] -> 用于计算系数
        2: [17]        # x=2, y=[17] -> 用于计算系数
    }
    
    print(f"输入数据: {data}")
    print("多项式: y = a + 2x + 3x² (系数通过前3个点计算)")
    print("对于 x=0, y=[1,2,3]:")
    print("  - y=1: a = 1 - 2*0 - 3*0² = 1")
    print("  - y=2: a = 2 - 2*0 - 3*0² = 2")
    print("  - y=3: a = 3 - 2*0 - 3*0² = 3")
    
    result = await ReconstructCalculator(data)
    print(f"输出结果: '{result}'")
    print(f"ASCII 字符: {[ord(c) for c in result] if result else 'None'}")
    print()


async def test_cubic_polynomial():
    """测试三次多项式（3次）"""
    print("=" * 60)
    print("测试 3: 三次多项式 (threshold=4, degree=3)")
    print("=" * 60)
    
    # 三次多项式: y = 1 + x + x^2 + x^3
    # 点: (0, 1), (1, 4), (2, 15), (3, 40)
    data = {
        0: [1, 2],     # x=0, y=[1,2] -> 常数项应该是 [1, 2]
        1: [4, 5],     # x=1, y=[4,5] -> 用于计算系数
        2: [15, 16],   # x=2, y=[15,16] -> 用于计算系数
        3: [40]        # x=3, y=[40] -> 用于计算系数
    }
    
    print(f"输入数据: {data}")
    print("多项式: y = a + x + x² + x³ (系数通过前4个点计算)")
    print("对于 x=0, y=[1,2]:")
    print("  - y=1: a = 1 - 1*0 - 1*0² - 1*0³ = 1")
    print("  - y=2: a = 2 - 1*0 - 1*0² - 1*0³ = 2")
    
    result = await ReconstructCalculator(data)
    print(f"输出结果: '{result}'")
    print(f"ASCII 字符: {[ord(c) for c in result] if result else 'None'}")
    print()


async def test_edge_cases():
    """测试边界情况"""
    print("=" * 60)
    print("测试 4: 边界情况")
    print("=" * 60)
    
    # 空字典
    print("4.1 空字典测试:")
    result = await ReconstructCalculator({})
    print(f"输入: {{}}")
    print(f"输出: '{result}'")
    print()
    
    # 只有一个点
    print("4.2 单点测试:")
    result = await ReconstructCalculator({1: [5]})
    print(f"输入: {{1: [5]}}")
    print(f"输出: '{result}'")
    print()
    
    # 字符串输入
    print("4.3 字符串输入测试:")
    result = await ReconstructCalculator({"1": "7,8,9", "2": "9"})
    print(f"输入: {{'1': '7,8,9', '2': '9'}}")
    print(f"输出: '{result}'")
    print()
    
    # 混合类型输入
    print("4.4 混合类型输入测试:")
    result = await ReconstructCalculator({1: [7, 8], "2": [9, 10]})
    print(f"输入: {{1: [7, 8], '2': [9, 10]}}")
    print(f"输出: '{result}'")
    print()


async def test_real_world_example():
    """测试真实世界示例"""
    print("=" * 60)
    print("测试 5: 真实世界示例")
    print("=" * 60)
    
    # 模拟工具调用数据
    data = {
        50: [81909584,37828876,85048168,37858582,74849679,88065632,87867768,37849178,89869084,37909032,70978595,80870146,90059632,70958032,70979269,83854439,75937771,44498578,89964484,77909532,75908869],  # tool_id=50, tool_seq=[...]
        100: [97320784,53240076,100459368,53269782,90260879,103476832,103278968,53260378,105280284,53320232,86389795,96281346,105470832,86369232,86390469,99265639,91348971,59909778,105375684,93320732,91320069] ,
        200:[158863184,114782476,162001768,114812182,151803279,165019232,164821368,114802778,166822684,114862632,147932195,157823746,167013232,147911632,147932869,160808039,152891371,121452178,166918084,154863132,152862469] # tool_id=100, tool_seq=[...]
    }
    
    print(f"输入数据: {data}")
    print("这是模拟的工具调用数据，包含两个工具ID和对应的序列")
    
    result = await ReconstructCalculator(data)
    print(f"输出结果: '{result}'")
    print(f"ASCII 字符: {[ord(c) for c in result] if result else 'None'}")
    print()


async def main():
    """运行所有测试"""
    print("ReconstructCalculator 扩展功能测试")
    print("测试扩展后的多项式重构计算功能")
    print("支持 threshold-1 次多项式，其中 threshold 是输入字典的长度")
    print()
    
    # await test_linear_polynomial()
    # await test_quadratic_polynomial()
    # await test_cubic_polynomial()
    # await test_edge_cases()
    await test_real_world_example()
    
    print("=" * 60)
    print("所有测试完成！")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
