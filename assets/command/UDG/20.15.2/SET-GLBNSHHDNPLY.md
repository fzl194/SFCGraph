---
id: UDG@20.15.2@MMLCommand@SET GLBNSHHDNPLY
type: MMLCommand
name: SET GLBNSHHDNPLY（配置NSH头增强全局策略）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBNSHHDNPLY
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- NSH头增强
- NSH全局策略
status: active
---

# SET GLBNSHHDNPLY（配置NSH头增强全局策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置NSH头增强全局策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- NSH头增强名称需要在NSHHEADEN中存在配置。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | REDIRIPVER | REDIRIPV4 | REDIRIPV6 | DSTSERVERPORT |
| --- | --- | --- | --- | --- |
| 初始值 | IPV4 | 0.0.0.0 | 0000:0000:0000:0000:0000:0000:0000:0000 | 6633 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSHNAME | NSH头增强名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置NSH头增强名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| REDIRIPVER | 重定向IP协议版本 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：添加重定向IP的版本为IPv4。<br>- IPV6：添加重定向IP的版本为IPv6。<br>- IPVER_ALL：添加重定向IP的版本为IPv4和IPv6。<br>默认值：无<br>配置原则：无 |
| REDIRIPV4 | 重定向IPV4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“REDIRIPVER”配置为“IPV4” 或 “IPVER_ALL”时为必选参数。<br>参数含义：该参数用于设置重定向服务器的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：无 |
| REDIRIPV6 | 重定向IPV6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“REDIRIPVER”配置为“IPV6” 或 “IPVER_ALL”时为必选参数。<br>参数含义：该参数用于设置重定向服务器的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| DSTSERVERPORT | NSH对端设备端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于设置NSH对端设备端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBNSHHDNPLY]] · NSH头增强全局策略（GLBNSHHDNPLY）

## 使用实例

设置名称为“nsh” 的NSH头增强配置，IP协议版本为IPv4，IP地址为10.0.0.0，则按如下命令配置：

```
SET GLBNSHHDNPLY: NSHNAME="nsh", REDIRIPVER=IPV4, REDIRIPV4="10.0.0.0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-GLBNSHHDNPLY.md`
