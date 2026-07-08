---
id: UDG@20.15.2@MMLCommand@SET GLBRLYSTCPCTRL
type: MMLCommand
name: SET GLBRLYSTCPCTRL（设置媒体中继全局业务TCP控制）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBRLYSTCPCTRL
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
- 媒体中继
- 媒体中继全局业务TCP控制
status: active
---

# SET GLBRLYSTCPCTRL（设置媒体中继全局业务TCP控制）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置媒体中继全局业务TCP控制。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IPV4MSS | RESENDTOTALTIME | SENDBUFSIZE | REVBUFSIZE |
| --- | --- | --- | --- | --- |
| 初始值 | 1380 | 5 | 80 | 20 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPV4MSS | IPv4最大报文段长度 | 可选必选说明：可选参数<br>参数含义：该参数用来指定IPv4最大报文段长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为536~1460。<br>默认值：无<br>配置原则：无 |
| RESENDTOTALTIME | TCP数据超时重传总时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用来指定TCP数据超时重传总时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~30，单位为秒。<br>默认值：无<br>配置原则：无 |
| SENDBUFSIZE | 发送缓冲区大小（千字节） | 可选必选说明：可选参数<br>参数含义：该参数用来指定发送缓冲区大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10~100，单位为千字节。<br>默认值：无<br>配置原则：无 |
| REVBUFSIZE | 接收缓冲区大小（千字节） | 可选必选说明：可选参数<br>参数含义：该参数用来指定接收缓冲区大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10~100，单位为千字节。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [媒体中继全局业务TCP控制（GLBRLYSTCPCTRL）](configobject/UDG/20.15.2/GLBRLYSTCPCTRL.md)

## 使用实例

假如需要配置媒体中继全局业务TCP控制，则命令如下：

```
SET GLBRLYSTCPCTRL: IPV4MSS=1380, RESENDTOTALTIME=5, SENDBUFSIZE=80, REVBUFSIZE=20;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置媒体中继全局业务TCP控制（SET-GLBRLYSTCPCTRL）_94871981.md`
