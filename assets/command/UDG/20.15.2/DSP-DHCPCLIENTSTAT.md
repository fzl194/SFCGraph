---
id: UDG@20.15.2@MMLCommand@DSP DHCPCLIENTSTAT
type: MMLCommand
name: DSP DHCPCLIENTSTAT（查询DHCPv4客户端状态信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DHCPCLIENTSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- DHCP管理
- DHCP客户端状态
status: active
---

# DSP DHCPCLIENTSTAT（查询DHCPv4客户端状态信息）

## 功能

该命令用于显示DHCPv4客户端状态信息。

## 注意事项

该命令在Ethernet接口上配置执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于显示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DHCPCLIENTSTAT]] · DHCPv4客户端状态信息（DHCPCLIENTSTAT）

## 使用实例

显示DHCPv4客户端状态信息：

```
DSP DHCPCLIENTSTAT: IFNAME="Ethernet64/0/4";
```

```

RETCODE = 0  操作成功

结果如下
--------
      接口名称  =  Ethernet64/0/4
       MAC地址  =  00e0-fcb7-4869
      IPv4地址  =  192.168.1.23
  IPv4地址掩码  =  255.255.255.0
服务器IPv4地址  =  192.168.1.2
          状态  =  绑定状态
      获取时间  =  2017-04-06T15:27:34
      租期时间  =  2017-04-06T16:27:34
      续租时间  =  2017-04-06T15:57:34
    重绑定时间  =  2017-04-06T16:20:04
      中止原因  =  NA
      租期时长  =  NA
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DHCPCLIENTSTAT.md`
