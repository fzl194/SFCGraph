---
id: UDG@20.15.2@MMLCommand@DSP APNSESSIONSTATS
type: MMLCommand
name: DSP APNSESSIONSTATS（按照IP地址分配方式查看当前在线会话数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: APNSESSIONSTATS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 查看APN当前在线会话数
status: active
---

# DSP APNSESSIONSTATS（按照IP地址分配方式查看当前在线会话数）

## 功能

**适用NF：PGW-U、UPF**

该命令用来按照IP地址分配方式查询当前在线会话数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CATEGORYTYPE | 种类 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IP_ALLOCATION：按照IP地址分配方式查看当前在线会话数。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNSESSIONSTATS]] · 按照IP地址分配方式查看当前在线会话数（APNSESSIONSTATS）

## 使用实例

按照IP地址分配方式查询当前在线会话数：

```
DSP APNSESSIONSTATS: CATEGORYTYPE=IP_ALLOCATION;
```

```

RETCODE = 0  Operation Success.

Ip Address Allocation Method
-------------------------
                                 Name of a Configured APN  =  a
     APN-specific Sessions Using Local Alloc IP Addresses  =  0
   APN-specific Sessions Using External Alloc IP Addresses =  0
    APN-specific Contexts Using LNS-assigned IP Addresses  =  0
(Number of results = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-APNSESSIONSTATS.md`
