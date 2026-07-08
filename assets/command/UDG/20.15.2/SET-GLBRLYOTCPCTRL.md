---
id: UDG@20.15.2@MMLCommand@SET GLBRLYOTCPCTRL
type: MMLCommand
name: SET GLBRLYOTCPCTRL（设置媒体中继全局回源TCP控制）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBRLYOTCPCTRL
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继全局回源TCP控制
status: active
---

# SET GLBRLYOTCPCTRL（设置媒体中继全局回源TCP控制）

## 功能

**适用NF：UPF、PGW-U**

该命令用于设置媒体中继全局回源TCP控制。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IPV4MSS | SENDBUFSIZE | REVBUFSIZE |
| --- | --- | --- | --- |
| 初始值 | 1460 | 20 | 80 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPV4MSS | IPv4最大报文段长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4最大报文段长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是为536～1460。<br>默认值：无<br>配置原则：无 |
| SENDBUFSIZE | 发送缓冲区大小（千字节） | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送缓冲区大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是为10～100，单位是千字节。<br>默认值：无<br>配置原则：无 |
| REVBUFSIZE | 接收缓冲区大小（千字节） | 可选必选说明：可选参数<br>参数含义：该参数用于指定接收缓冲区大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是为10～100，单位是千字节。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBRLYOTCPCTRL]] · 媒体中继全局回源TCP控制（GLBRLYOTCPCTRL）

## 使用实例

设置媒体中继全局回源TCP控制：

```
SET GLBRLYOTCPCTRL: IPV4MSS=1460;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-GLBRLYOTCPCTRL.md`
