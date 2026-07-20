---
id: "{{nf}}@CompoundTask@{{英文名}}"
type: "CompoundTask"
name: "{{英文名}}"
name_zh: "{{步骤中文名}}"
nf: "{{nf}}"
version: "{{version}}"
command_set: ["{{CMD1}}", "{{CMD2}}"]
status: "draft"
---

# {{步骤中文名}}

> {{定位一句话}}。被引用于：[[{{nf}}@FeatureTask@{{feature_code}}]]。

## 配置方法

{{引子（1-2 句）：本步骤建什么 + 为谁提供基础}}

| 步骤 | 命令 | 关键参数 |
|---|---|---|
| {{步骤名（短）}} | `{{CMD}}` → [[{{nf}}@AtomTask@{{CMD}}]] | `{{参数1}}`=`<取值>`，`{{参数2}}`=`<取值>` |

**典型脚本**：

```
{{真实 MML 命令块，含真实参数取值}}
```

**步骤位置**：{{本 compound 在哪个上游之后、下游是谁}}

## 场景差异

> 每引用方 feature_task 一行。防假通用（R1.2）：复用时本 feature 差异必须双向回填到此。

- **{{feature_code}}（{{场景}}）**：{{差异/参数增量/专属命令/命令子集}}（被引用于 [[{{nf}}@FeatureTask@{{feature_code}}]]）

## 决策点

| 选项 | 影响（参数/命令/联动） |
|---|---|
| {{选项}} | {{影响}} |

> 无分支则显式说明"本步骤用法单一，无分支"。

## 约束

- **{{规则名}}**（{{severity}}）：{{约束}} — {{后果}}

## 边
- 组成: [[{{nf}}@AtomTask@{{CMD1}}]], [[{{nf}}@AtomTask@{{CMD2}}]]
- 被引用于: [[{{nf}}@FeatureTask@{{feature_code}}]]
