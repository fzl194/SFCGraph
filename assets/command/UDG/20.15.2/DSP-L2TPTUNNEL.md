---
id: UDG@20.15.2@MMLCommand@DSP L2TPTUNNEL
type: MMLCommand
name: DSP L2TPTUNNEL（查询L2TP隧道的相关信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: L2TPTUNNEL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP隧道查询
status: active
---

# DSP L2TPTUNNEL（查询L2TP隧道的相关信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查看L2TP隧道相关的信息。运营商可以分别根据APN名字、接口名字等信息查询L2TP的隧道信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SHOWTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INTERFACE：表示根据Gi接口名字查询隧道信息。<br>- APN：表示根据APN名字查询隧道信息。<br>默认值：无<br>配置原则：无 |
| INTERFACENAME | 接口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SHOWTYPE”配置为“INTERFACE”时为必选参数。<br>参数含义：该参数用于指定查询的Gi接口名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| TUNNELID | L2TP隧道号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SHOWTYPE”配置为“INTERFACE”时为可选参数。<br>参数含义：该参数用于指定查询的L2TP隧道号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～64000。<br>默认值：无<br>配置原则：无 |
| APN | APN实例名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SHOWTYPE”配置为“APN”时为必选参数。<br>参数含义：该参数用于表示APN实例名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：_、#、$等。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [L2TP隧道的相关信息（L2TPTUNNEL）](configobject/UDG/20.15.2/L2TPTUNNEL.md)

## 使用实例

运营商如果需要查看giif1/0/0接口下，ID为1的隧道的信息：

```
DSP L2TPTUNNEL: SHOWTYPE=INTERFACE,INTERFACENAME="giif1/0/0",TUNNELID=1;
```

```

L2TP tunnel info
-------------------------
        Remote Name  =  NULL
       Group Number  =  869
    Local Tunnel ID  =  1
   Remote Tunnel ID  =  5
Remote IPv4 Address  =  NULL
        Remote Port  =  1701
           Sessions  =  1
          Giif Name  =  giif1/0/0
  Giif IPv4 Address  =  NULL
             Uptime  =  0 days, 0 hours, 0 minutes
   Send Window Size  =  64
            IP Type  =  IPV6
Remote IPv6 Address  =  2001:DB8:0:0:0:0:0:84
  Giif IPv6 Address  =  FE80:64:83:3:0:0:0:82
(Number of results = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询L2TP隧道的相关信息（DSP-L2TPTUNNEL）_35373529.md`
