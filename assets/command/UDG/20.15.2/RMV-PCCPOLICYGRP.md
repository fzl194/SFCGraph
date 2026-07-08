---
id: UDG@20.15.2@MMLCommand@RMV PCCPOLICYGRP
type: MMLCommand
name: RMV PCCPOLICYGRP（删除PCC策略组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PCCPOLICYGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- PCC控制策略
- PCC策略组
status: active
---

# RMV PCCPOLICYGRP（删除PCC策略组）

## 功能

**适用NF：PGW-U、UPF**

![](删除PCC策略组（RMV PCCPOLICYGRP）_82837608.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会删除PCC策略组下所有的业务属性绑定关系

此命令用于删除PCC策略组。

支持批量删除：不输入条件，表示删除所有未被引用的PCC策略组。当配置量较大时单次执行可能无法删除全部记录，需要多次执行。

## 注意事项

- 该命令执行后立即生效。
- 输入的PccPolicyGrpNm通过LST RULE查询Rule记录，如果引用了该PccPolicyGrp的Rule的记录存在，则不允许删除PccPolicyGrp记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：可选参数<br>参数含义：设置PCC策略组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PCCPOLICYGRP]] · PCC策略组（PCCPOLICYGRP）

## 使用实例

删除名称为TestPccPolicyGrpName的PCC策略组：

```
RMV PCCPOLICYGRP:PCCPOLICYGRPNM ="TestPccPolicyGrpName";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PCCPOLICYGRP.md`
