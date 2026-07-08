---
id: UDG@20.15.2@MMLCommand@SET UPINFO
type: MMLCommand
name: SET UPINFO（设置UP信息）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPINFO
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- UP信息管理
- UP信息
status: active
---

# SET UPINFO（设置UP信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

设置UPF基本信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- UPF上有用户在线时，该命令不可用。
- 该命令用来配置偶联消息中的Node ID，如果不配置会导致偶联建立失败。
- 信令消息抄送场景，UPF主机名的长度最大支持253。
- 当IPv4NodeID被设置为0.0.0.0时，该参数值被视为无效值，如果需要设置IPv4的UP Node ID时，需要选择有效的IPv4值重新设置。
- 当IPv6NodeID被设置为0000:0000:0000:0000:0000:0000:0000:0000时，该参数值被视为无效值，如果需要设置IPv6的UP Node ID时，需要选择有效的IPv6值重新设置。
- 三个参数都是可选参数，但三个参数中必须输入一项有效值，且只允许输入一项有效值。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IPV6NODEID | IPV4NODEID |
| --- | --- | --- |
| 初始值 | 0:0:0:0:0:0:0:0 | 0.0.0.0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | HostName | 可选必选说明：可选参数<br>参数含义：该参数用来指定UPF的主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。支持的字符类型包括：大小写字母、数字、“ -”、“ .”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPV6NODEID | IPv6地址类型的Node Id | 可选必选说明：可选参数<br>参数含义：IPv6类型的UPF Node Id。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4NODEID | IPv4地址类型的Node Id | 可选必选说明：可选参数<br>参数含义：IPv4类型的UPF Node Id。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPINFO]] ·  UP 参数信息（UPINFO）

## 使用实例

设置UPF的主机名为UPF27：

```
SET UPINFO: HOSTNAME="UPF27";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-UPINFO.md`
