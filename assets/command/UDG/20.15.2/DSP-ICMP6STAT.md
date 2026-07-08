---
id: UDG@20.15.2@MMLCommand@DSP ICMP6STAT
type: MMLCommand
name: DSP ICMP6STAT（查询ICMP6统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ICMP6STAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- ICMP6统计
status: active
---

# DSP ICMP6STAT（查询ICMP6统计）

## 功能

该命令用于显示ICMPv6报文统计计数。

若不指定IFNAME参数时，则显示所有接口的ICMPv6报文统计计数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ICMP6STAT]] · ICMP6统计（ICMP6STAT）

## 使用实例

显示ICMPv6报文统计计数：

```
DSP ICMP6STAT:IFNAME="Ethernet65/0/8";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
        收到NA  =  0
        发送NA  =  0
        收到RA  =  0
        发送RA  =  0
        收到NS  =  0
        发送NS  =  0
        收到RS  =  0
        发送RS  =  0
发送ICMPv6请求  =  0
发送ICMPv6响应  =  0
收到ICMPv6请求  =  0
收到ICMPv6响应  =  0
(返回结果 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ICMP6统计（DSP-ICMP6STAT）_49961378.md`
