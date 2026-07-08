---
id: UNC@20.15.2@MMLCommand@RMV PCCPOLICYGRP
type: MMLCommand
name: RMV PCCPOLICYGRP（删除PCC策略组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCCPOLICYGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- PCC策略组
status: active
---

# RMV PCCPOLICYGRP（删除PCC策略组）

## 功能

**适用NF：PGW-C、SMF**

此命令用于删除PCC策略组。

不输入条件，表示删除所有未被引用的PCC策略组。当配置量较大时单次执行可能无法删除全部记录，需要执行多次。

## 注意事项

- 该命令执行后立即生效。
- 通过命令LST RULE查询Rule记录，如果有引用了该PccPolicyGrp的Rule的记录存在，则不允许删除该PccPolicyGrp记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：可选参数<br>参数含义：设置PCC策略组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [PCC策略组（PCCPOLICYGRP）](configobject/UNC/20.15.2/PCCPOLICYGRP.md)

## 使用实例

删除名称为TestPccPolicyGrpName的PCC策略组：

```
RMV PCCPOLICYGRP:PCCPOLICYGRPNM ="TestPccPolicyGrpName";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除PCC策略组（RMV-PCCPOLICYGRP）_09897175.md`
