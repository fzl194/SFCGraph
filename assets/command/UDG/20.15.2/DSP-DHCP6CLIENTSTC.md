---
id: UDG@20.15.2@MMLCommand@DSP DHCP6CLIENTSTC
type: MMLCommand
name: DSP DHCP6CLIENTSTC（查询DHCPv6客户端报文统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DHCP6CLIENTSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- DHCP管理
- DHCPv6客户端报文统计
status: active
---

# DSP DHCP6CLIENTSTC（查询DHCPv6客户端报文统计）

## 功能

该命令用于显示DHCPv6客户端报文统计信息。

## 注意事项

该命令在Ethernet接口上配置执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于显示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DHCP6CLIENTSTC]] · DHCPv6客户端报文统计（DHCP6CLIENTSTC）

## 使用实例

显示DHCPv6客户端报文统计信息：

```
DSP DHCP6CLIENTSTC:;
```

```

RETCODE = 0  操作成功

结果如下
--------
                       接口名称  =  Ethernet64/0/4
          接收Advertise报文个数  =  1
              接收Reply报文个数  =  1
        接收Reconfigure报文个数  =  0
            接收Invalid报文个数  =  0
            发送Solicit报文个数  =  14
            发送Request报文个数  =  1
            发送Confirm报文个数  =  0
              发送Renew报文个数  =  0
             发送Rebind报文个数  =  0
            发送Release报文个数  =  0
            发送Decline报文个数  =  0
发送Information Request报文个数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DHCPv6客户端报文统计（DSP-DHCP6CLIENTSTC）_00440793.md`
