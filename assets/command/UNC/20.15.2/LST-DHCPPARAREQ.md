---
id: UNC@20.15.2@MMLCommand@LST DHCPPARAREQ
type: MMLCommand
name: LST DHCPPARAREQ（查询向外部DHCPv4或者DHCPv6服务器发送的消息中的请求信元中的参数信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DHCPPARAREQ
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- DHCP管理
- DHCP请求信元参数信息
status: active
---

# LST DHCPPARAREQ（查询向外部DHCPv4或者DHCPv6服务器发送的消息中的请求信元中的参数信息）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来查询向外部DHCPv4或者DHCPv6服务器发送的消息中的请求信元中的参数信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DHCPPARAREQ]] · 向外部DHCPv4或者DHCPv6服务器发送的消息中的请求信元中的参数信息（DHCPPARAREQ）

## 使用实例

查询向外部DHCPv4或者DHCPv6服务器发送的消息中的请求信元中的参数信息：

```
%%LST DHCPPARAREQ:;%%
RETCODE = 0  操作成功

结果如下
--------
   指定DHCPv4消息中是否请求DNS服务器地址  =  使能
指定DHCPv4消息中是否请求P-CSCF服务器地址  =  使能
   指定DHCPv6消息中是否请求DNS服务器地址  =  不使能
指定DHCPv6消息中是否请求P-CSCF服务器地址  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询向外部DHCPv4或者DHCPv6服务器发送的消息中的请求信元中的参数信息（LST-DHCPPARAREQ）_86824470.md`
