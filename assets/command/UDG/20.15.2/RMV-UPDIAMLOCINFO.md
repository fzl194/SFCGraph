---
id: UDG@20.15.2@MMLCommand@RMV UPDIAMLOCINFO
type: MMLCommand
name: RMV UPDIAMLOCINFO（删除Diameter本端信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPDIAMLOCINFO
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- Diameter连接
- Diameter本端信息
status: active
---

# RMV UPDIAMLOCINFO（删除Diameter本端信息）

## 功能

**适用NF：UPF**

![](删除Diameter本端信息（RMV UPDIAMLOCINFO）_45195180.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除Diameter本端信息可能导致Diameter链路中断，进而影响用户使用业务，比如用户被去活等。

此命令用来删除Diameter本端信息。支持批量删除，不给HOSTNAME字段赋值，删除所有记录。

## 注意事项

- 该命令执行后立即生效。
- 该命令用于删除Swm接口相关的标识信息。
- 删除后，将导致所有Group下使用该LocalInfo的链路断开。
- 删除正在使用的Diameter本端信息，会影响当前在线用户信令处理，可能导致用户去活等异常，具体异常看各diameter应用异常处理配置。如需删除，建议先去活用户。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 本端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMLOCINFO]] · Diameter本端信息（UPDIAMLOCINFO）

## 使用实例

删除HOSTNAME为“test”的Diameter本端信息：

```
RMV UPDIAMLOCINFO:HOSTNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-UPDIAMLOCINFO.md`
