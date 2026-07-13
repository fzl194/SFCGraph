---
id: UNC@20.15.2@MMLCommand@MOD USRLOCATIONGRP
type: MMLCommand
name: 修改用户位置组
status: inferred
---

# 修改用户位置组（MOD USRLOCATIONGRP）

> **★ 命令静态知识待补全**（UNC pre-build 阶段命令 wiki 资产缺失）：本 md 由 Lint R6 反向校验自动生成最小占位骨架。完整命令参数表/约束/决策点/联动命令族请补全。
>
> **所在族**：用户位置组 CRUD（ADD/MOD/RMV/LST USRLOCATIONGRP，配套配置对象 `USRLOCATIONGRP`）
>
> **证据出处**：[0-00211.md 配套组段](task/UNC/20.15.2/0-00211.md) 提及"MOD USRLOCATIONGRP（★R1.5 命令名待核）"，归属 WSFD-106003 用户接入控制特性。

## 命令骨架

| 元素 | 说明 |
|---|---|
| 命令名 | `MOD USRLOCATIONGRP` |
| 命令族 | 用户位置组 CRUD（ADD/MOD/RMV/LST）|
| 配置对象 | [USRLOCATIONGRP](configobject/UNC/20.15.2/USRLOCATIONGRP.md) |
| 被引用于 | [1-00019 配置用户位置与模板绑定](task/UNC/20.15.2/1-00019.md) · [2-00013 基于初始接入位置的策略控制](task/UNC/20.15.2/2-00013.md) |
| 前置依赖 | [ADD USRLOCATION](task/UNC/20.15.2/0-00210.md)（位置前置）|

## ★ 待补内容（v1.3 P1 专项）

- [ ] 命令参数表（USRLOCATIONGRPNAME 字符串 1~63 等）
- [ ] 配置维度（按位置类型分叉 / 优先级 / 时段 / 区域限定等）
- [ ] 决策点表（位置策略 → 用户模板组绑定走法）
- [ ] 约束（关键约束 + License + 限制条件）
- [ ] 典型脚本
- [ ] evidence 命令 wiki 拷贝到 `evidence/UNC/20.15.2/MOD-USRLOCATIONGRP/`

## 关联

- 配置对象 wiki：[USRLOCATIONGRP](configobject/UNC/20.15.2/USRLOCATIONGRP.md)
- 配套组（CRUD）：
  - [ADD USRLOCATIONGRP](command/UNC/20.15.2/ADD-USRLOCATIONGRP.md)
  - [MOD USRLOCATIONGRP](command/UNC/20.15.2/MOD-USRLOCATIONGRP.md)（本命令）
  - [RMV USRLOCATIONGRP](command/UNC/20.15.2/RMV-USRLOCATIONGRP.md)
  - [LST USRLOCATIONGRP](command/UNC/20.15.2/LST-USRLOCATIONGRP.md)