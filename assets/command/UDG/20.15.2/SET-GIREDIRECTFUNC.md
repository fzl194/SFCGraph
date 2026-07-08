---
id: UDG@20.15.2@MMLCommand@SET GIREDIRECTFUNC
type: MMLCommand
name: SET GIREDIRECTFUNC（设置全局Gi重定向信息）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GIREDIRECTFUNC
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
- 业务安全防护
- 用户攻击防护
- Gi重定向
- Gi重定向功能
status: active
---

# SET GIREDIRECTFUNC（设置全局Gi重定向信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置Gi重定向全局开关，当需要控制UE之间互访的恶意攻击报文和需要通过网关将报文重定向来保证网络的安全的场景下使用此命令设置Gi重定向全局开关。当全局开关使能后，基于VPN的重定向配置才会生效，允许将用户报文重定向到指定地址或者丢弃。当全局开关不使能时，允许UE互访。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | V4GIREDIRSWITCH | V6GIREDIRSWITCH |
| --- | --- | --- |
| 初始值 | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| V4GIREDIRSWITCH | IPV4全局Gi重定向开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示全局IPv4类型的Gi重定向功能的使能开关。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：去使能全局IPv4 Gi重定向功能。<br>- ENABLE：使能全局IPv4 Gi重定向功能。<br>默认值：无<br>配置原则：无 |
| V6GIREDIRSWITCH | IPV6全局Gi重定向开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示全局IPv6类型的Gi重定向功能的使能开关。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：去使能全局IPv6 Gi重定向功能。<br>- ENABLE：使能全局IPv6 Gi重定向功能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [全局Gi重定向信息（GIREDIRECTFUNC）](configobject/UDG/20.15.2/GIREDIRECTFUNC.md)

## 使用实例

使能IPv4以及IPv6全局Gi重定向功能：

```
SET GIREDIRECTFUNC:V4GIREDIRSWITCH=ENABLE,V6GIREDIRSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置全局Gi重定向信息（SET-GIREDIRECTFUNC）_82837764.md`
