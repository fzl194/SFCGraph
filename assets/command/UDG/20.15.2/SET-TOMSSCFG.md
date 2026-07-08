---
id: UDG@20.15.2@MMLCommand@SET TOMSSCFG
type: MMLCommand
name: SET TOMSSCFG（设置Tcp Mss配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOMSSCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- TCP MSS配置
status: active
---

# SET TOMSSCFG（设置Tcp Mss配置）

## 功能

**适用NF：UPF**

该命令用于设置TCP报文长度。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | V4TCPMSSVALUE | V6TCPMSSVALUE |
| --- | --- | --- |
| 初始值 | 1460 | 1440 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| V4TCPMSSVALUE | IPv4 TCP报文长度（字节） | 可选必选说明：可选参数<br>参数含义：设置TPV4 TCP报文长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为496～1500。<br>默认值：无<br>配置原则：无 |
| V6TCPMSSVALUE | IPv6 TCP报文长度（字节） | 可选必选说明：可选参数<br>参数含义：设置IPV6 TCP报文长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为496～1500。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOMSSCFG]] · Tcp Mss配置（TOMSSCFG）

## 使用实例

设置IPv4 TCP报文长度为496字节，IPv6 TCP报文长度为1500字节：

```
SET TOMSSCFG: V4TCPMSSVALUE=496, V6TCPMSSVALUE=1500;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-TOMSSCFG.md`
