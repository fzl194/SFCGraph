---
id: UNC@20.15.2@MMLCommand@RMV DCCTEMPLATE
type: MMLCommand
name: RMV DCCTEMPLATE（删除DCC模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DCCTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- 信用控制模板
status: active
---

# RMV DCCTEMPLATE（删除DCC模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除DCC在线计费模板。

## 注意事项

- 该命令执行后立即生效。
- 当DCCTemplate配置在APNCharge、GlbDccTemplate、UsrProfCharge中时，不可以删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | DCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定操作的DCC在线计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DCCTEMPLATE]] · DCC模板（DCCTEMPLATE）

## 使用实例

删除名为“DccTemplate”的DCC在线计费模板：

```
RMV DCCTEMPLATE:DCCTMPLTNAME="DccTemplate";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DCC模板（RMV-DCCTEMPLATE）_09896925.md`
