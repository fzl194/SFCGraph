---
id: UNC@20.15.2@MMLCommand@RMV PCCUSRFLOWCTRL
type: MMLCommand
name: RMV PCCUSRFLOWCTRL（删除流控策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCCUSRFLOWCTRL
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 更新流控策略
status: active
---

# RMV PCCUSRFLOWCTRL（删除流控策略）

## 功能

**适用NF：SMF**

该命令用于删除流控策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRFLOWCTRLNAME | Update流控策略名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Update流控策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [流控策略（PCCUSRFLOWCTRL）](configobject/UNC/20.15.2/PCCUSRFLOWCTRL.md)

## 使用实例

删除流控策略flowctr1。

```
RMV PCCUSRFLOWCTRL: USRFLOWCTRLNAME="flowctr1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除流控策略（RMV-PCCUSRFLOWCTRL）_11712040.md`
