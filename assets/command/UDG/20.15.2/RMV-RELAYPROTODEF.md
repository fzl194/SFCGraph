---
id: UDG@20.15.2@MMLCommand@RMV RELAYPROTODEF
type: MMLCommand
name: RMV RELAYPROTODEF（删除媒体中继协议定义）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RELAYPROTODEF
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继协议定义
status: active
---

# RMV RELAYPROTODEF（删除媒体中继协议定义）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除媒体中继协议定义。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYPROTODEFNM | 媒体中继协议定义规则组名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定媒体中继协议定义规则组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| RELAYPROTORULE | 媒体中继协议定义规则 | 可选必选说明：可选参数<br>参数含义：该参数用来指定媒体中继协议定义规则。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYPROTODEF]] · 媒体中继协议定义（RELAYPROTODEF）

## 使用实例

假如需要删除一组媒体中继协议定义，则命令如下：

```
RMV RELAYPROTODEF: RELAYPROTODEFNM="def001";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除媒体中继协议定义（RMV-RELAYPROTODEF）_44232372.md`
