---
id: UNC@20.15.2@MMLCommand@RMV DIAMLOCINFO
type: MMLCommand
name: RMV DIAMLOCINFO（删除Diameter本端信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DIAMLOCINFO
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diameter本端信息
status: active
---

# RMV DIAMLOCINFO（删除Diameter本端信息）

## 功能

**适用NF：PGW-C、SMF**

![](删除Diameter本端信息（RMV DIAMLOCINFO）_09897273.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除Diameter本端信息可能导致Diameter链路中断，进而影响用户使用业务，比如用户被去活等。

此命令用来删除Diameter本端信息。支持批量删除，不给HOSTNAME字段赋值，删除所有记录。

## 注意事项

- 该命令执行后立即生效。
- 当未指定本端主机名时，禁止执行该命令。若需要执行，需将软参BYTE976的值设置为169。
- 该命令用于删除Gx或IP-CAN Session接口相关的标识信息。当被删除的标识信息已经在用时，对已建立的IP-CAN Session影响较大。
- 删除后，将导致所有Group下使用该LocalInfo的链路断开，已经建立的IP-CAN Session会话状态不受影响，但该会话的后续授权操作将失败。
- 删除正在使用的Diameter本端信息，会影响当前在线用户信令处理，可能导致用户去活等异常，具体异常看各diameter应用异常处理配置。如需删除，建议先去活用户。
- 如果该LocalInfo被DCC模板、PCC模板或全局PCC绑定，则绑定关系同时删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 本端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMLOCINFO]] · Diameter本端信息（DIAMLOCINFO）

## 使用实例

删除HOSTNAME为“test”的Diameter本端信息：

```
RMV DIAMLOCINFO:HOSTNAME="test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Diameter本端信息（RMV-DIAMLOCINFO）_09897273.md`
