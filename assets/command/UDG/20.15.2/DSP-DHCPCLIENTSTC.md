---
id: UDG@20.15.2@MMLCommand@DSP DHCPCLIENTSTC
type: MMLCommand
name: DSP DHCPCLIENTSTC（查询DHCPv4客户端报文统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DHCPCLIENTSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- DHCP管理
- DHCP客户端报文统计
status: active
---

# DSP DHCPCLIENTSTC（查询DHCPv4客户端报文统计）

## 功能

该命令用于显示DHCPv4客户端报文统计信息。

## 注意事项

该命令在Ethernet接口上配置执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于显示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DHCPCLIENTSTC]] · DHCPv4客户端报文统计（DHCPCLIENTSTC）

## 使用实例

显示DHCPv4客户端报文统计信息：

```
DSP DHCPCLIENTSTC: IFNAME="Ethernet64/0/4";
```

```

RETCODE = 0  操作成功

结果如下
--------
                      接口名称  =  Ethernet64/0/4
              发送发现报文个数  =  1
        接收服务器应答报文个数  =  1
              发送请求报文个数  =  1
    发送重启状态下请求报文个数  =  0
    发送选择状态下请求报文个数  =  1
    发送续租状态下请求报文个数  =  0
  发送重绑定状态下请求报文个数  =  0
          发送地址冲突报文个数  =  0
          发送地址释放报文个数  =  0
               接收ACK报文个数  =  1
               接收NAK报文个数  =  0
                  收到报文个数  =  2
                  发出报文个数  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DHCPv4客户端报文统计（DSP-DHCPCLIENTSTC）_00601349.md`
