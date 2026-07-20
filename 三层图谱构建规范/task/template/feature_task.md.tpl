---
id: "{{nf}}@FeatureTask@{{feature_code}}"
type: "FeatureTask"
name: "{{feature_code}}"
name_zh: "{{特性名}}"
nf: "{{nf}}"
version: "{{version}}"
ref: "{{nf}}@Feature@{{feature_code}}"
status: "draft"
---

# {{特性名}}（{{feature_code}}）

> 特性静态知识见 [[{{nf}}@Feature@{{feature_code}}]]。本页讲配置生成实例化时怎么配。

## 配置概览

{{对象链 + 场景骨架（2-3 段，含关键差异维度）}}

## 配置流程

> 步骤 + 单命令混合编排。步骤（≥2 命令）→ compound；单命令 → 直接 atom。

1. **{{步骤A名}}**（{{一句话}}）：`{{CMD1}}` + `{{CMD2}}` → [[{{nf}}@CompoundTask@{{英文名}}]]
   - 关键参数：`{{参数1}}`=`<取值>`
2. **{{命令B名}}**（{{一句话}}）：`{{CMDB}}` → [[{{nf}}@AtomTask@{{CMDB}}]]
   - 关键参数：`{{参数}}`=`<取值>`
3. **{{步骤C名}}**（{{一句话}}）：`{{CMD3}}` + `{{CMD4}}` → [[{{nf}}@CompoundTask@{{英文名}}]]
   - 关键参数：`{{参数}}`=`<取值>`

## 决策点

> 场景影响表；多 DP 按差异独立轴分表（≥2 轴）。无分支显式说明。DP 不编号。

### DP1：{{决策点名}}
| 选项/场景 | 走法 | 关键联动 | 影响 |
|---|---|---|---|
| {{选项}} | {{compound/atom}} | {{参数}} | {{影响}} |

## 约束

- **{{规则名}}**（{{severity}}）：{{约束}} — {{后果}}

## 边
- 对应特性: [[{{nf}}@Feature@{{feature_code}}]]
- 编排: [[{{nf}}@CompoundTask@{{英文名}}]], [[{{nf}}@AtomTask@{{CMD}}]]
