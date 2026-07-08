---
id: UNC@20.15.2@MMLCommand@LST LOCALGGSN
type: MMLCommand
name: LST LOCALGGSN（查询本地GGSN列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCALGGSN
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- 本地GGSN功能
status: active
---

# LST LOCALGGSN（查询本地GGSN列表）

## 功能

**适用网元：SGSN**

本命令用于查询本地GGSN地址。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的记录的IP地址类型。<br>数据来源：整网规划<br>取值范围：枚举类型<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| IP | IPv4地址 | 可选必选说明：条件可选参数<br>参数定义：该参数用于指定待查询的记录内的任一IPv4地址。<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 有效的IPv4地址不能为 0.0.0.0,255.255.255.255，或0.x.y.z。<br>- 有效的IPv4地址不能为环回地址(127.x.y.z)，或组播地址(224.x.y.z)。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| IPV6 | IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定待查询的记录内的任一IPv6地址。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALGGSN]] · 本地GGSN列表（LOCALGGSN）

## 使用实例

查询表项记录：

LST LOCALGGSN:;

```
%%LST LOCALGGSN:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
配置类型         IP地址类型    起始IPv4地址    终止IPv4地址    掩码               描述

IP+掩码          IPv4          192.168.0.0     192.168.0.0     255.255.255.255    NULL
起始IP+终止IP    IPv4          10.10.0.0       10.10.10.255    0.0.0.0            NULL
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LOCALGGSN.md`
