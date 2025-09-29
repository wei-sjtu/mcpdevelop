# MCP多工具联合投毒实验
--- 
## attacker
`python inject_generator.py "your instruction here" "1,2,5,10" 1` 需要手动调整多项式系数
## 指令映射
- 目标：将希望模型执行的恶意指令（English）映射为ASCII码(统一为大写，并移除空白字符)
- 执行：` python mapping.py`
- 输入：
  - inject_instruction: 希望模型执行的恶意指令
  - group_size: 每个分组的字符数（不宜过长，模型解码时易出错。）
- 输出：
  - ChartoNum_{timestamp_str}.json
  - 指令对应的ASCII码（numeric_value字段）

## （t,n）门限方案：多项式构造与计算
- 目标：构造一个（t,n）门限方案，计算工具描述的最后嵌入（tool_id,tool_seq）,其中t为门限，n为投毒工具总数，计算多项式值: tool_seq=y=F(x; Nmal) = Nmal + a₁x + a₂x² + ... + a_(t-1)x^(t-1) x=tool_id
  - 其中，Nmal为恶意指令的ASCII码(numeric_value)，a₁,a₂,...,a_(t-1)为随机生成的系数，tool_seq分为若干组，使用相同的系数计算多项式值。

- 执行：`python polynomial_calculator.py [json_file] [tool_id] [degree]`

- 可选参数：
```
  - json_file: ChartoNum_{}.json文件
  - x_value: 输入的x值（tool_id）
  - degree: t-1（多项式最高阶数）
  - coefficients: 多项式系数（a₁,a₂,...,a_(t-1)）可指定也可随机生成(List[int])
``` 
- 输出：
  - .\inject_content\polynomial_results_{timestamp}.json
  - 工具描述的最后嵌入（tool_id,tool_seq）

## 指令植入完整流程
1. 运行mapping.py获得映射（编码）后的恶意指令（数值）
2. 攻击者首先需要确定（t,n）门限方案，则degree为t-1，需要以不同的x（tool_id）和**同样的系数**重复运行n次`polynomial_calculator.py`，获得工具描述的最后嵌入（tool_id,tool_seq）
3. 将n个（tool_id,tool_seq）嵌入到工具描述中

---
## victim
在tool manager的工具描述中插入重构规则
## 重构规则模板
<\background>
<\project_rule>
<\calculate>
<\decode>
<\execute>

## agent指令重构阶段逻辑分析
- 提取约定字段：从工具描述中提取（tool_id,tool_seq）
- 计算Nmal. 
- 解码Nmal.
- 执行恶意指令。
---

## scenario
- 场景1：
  - 攻击目标：
  - 攻击指令：
  - 具体参数：
  - 攻击效果：



