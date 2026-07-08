---
id: UDG@20.15.2@MMLCommand@RMV PCCACTIONPROP
type: MMLCommand
name: RMV PCCACTIONPROP（删除PCC动作属性）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PCCACTIONPROP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- PCC控制策略
- PCC动作属性
status: active
---

# RMV PCCACTIONPROP（删除PCC动作属性）

## 功能

**适用NF：PGW-U、UPF**

此命令用于删除PCC动作属性。支持批量删除，不输入条件，表示删除所有未被引用的PCC动作属性。

## 注意事项

- 该命令执行后立即生效。
- 输入的PccActPropName通过LST PCCPOLICYGRP和LST SRVPBINDPCCPG查询PccPolicyGrp记录，如果引用了该PccActionProp的PccPolicyGrp的记录存在，则不允许删除PccActionProp记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCACTPROPNAME | PCC动作属性名称 | 可选必选说明：可选参数<br>参数含义：设置PCC动作属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PCCACTIONPROP]] · PCC动作属性（PCCACTIONPROP）

## 使用实例

删除名称为TestPccActPropName的PCC动作属性：

```
RMV PCCACTIONPROP:PCCACTPROPNAME="TestPccActPropName";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PCCACTIONPROP.md`
