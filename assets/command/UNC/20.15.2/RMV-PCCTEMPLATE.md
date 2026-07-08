---
id: UNC@20.15.2@MMLCommand@RMV PCCTEMPLATE
type: MMLCommand
name: RMV PCCTEMPLATE（删除PCC模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCCTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- PCC模板
status: active
---

# RMV PCCTEMPLATE（删除PCC模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除一个PCC模板配置。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCTEMPNAME | PCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCC模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写，不允许命名为“global”。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCTEMPLATE]] · PCC模板（PCCTEMPLATE）

## 使用实例

因业务变更，APN下不再需要PCC功能，则可以删除已经配置的PCC模板：

```
RMV PCCTEMPLATE: PCCTEMPNAME="new_pcc_template";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除PCC模板（RMV-PCCTEMPLATE）_09897066.md`
