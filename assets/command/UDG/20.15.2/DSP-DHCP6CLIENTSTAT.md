---
id: UDG@20.15.2@MMLCommand@DSP DHCP6CLIENTSTAT
type: MMLCommand
name: DSP DHCP6CLIENTSTAT（查询DHCPv6客户端状态信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DHCP6CLIENTSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- DHCP管理
- DHCPv6客户端状态
status: active
---

# DSP DHCP6CLIENTSTAT（查询DHCPv6客户端状态信息）

## 功能

该命令用于显示DHCPv6客户端状态信息。

## 注意事项

该命令在Ethernet接口上配置执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DHCP6CLIENTSTAT]] · DHCPv6客户端状态信息（DHCP6CLIENTSTAT）

## 使用实例

显示DHCPv6客户端状态信息：

```
DSP DHCP6CLIENTSTAT: IFNAME="Ethernet64/0/4";
```

```

RETCODE = 0  操作成功

结果如下
--------
            接口名称  =  Ethernet64/0/4
        地址申请模式  =  有状态模式
        地址申请状态  =  绑定状态
        服务器的DUID  =  0001000658e6cb436c0001a33659
        客户端的DUID  =  0000000000000000005056230005
    服务器的全局地址  =  FE80::6E00:1FF:FEA3:3659
          源IPv6地址  =  FE80::250:56FF:FEB7:4869
          地址联盟ID  =  0x6
      续租时长（秒）  =  133
    重绑定时长（秒）  =  212
            获取时间  =  2017-04-06T15:35:18
            更新时间  =  2017-04-06T15:37:31
        绑定更新时间  =  2017-04-06T15:38:50
            IPv6地址  =  2001:db8::6
  有效生命周期（秒）  =  400
  首选生命周期（秒）  =  266
            超时时间  =  2017-04-06T15:41:58
      剩余时间（秒）  =  282
        租期时长      =  NA
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DHCP6CLIENTSTAT.md`
