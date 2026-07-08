---
id: UNC@20.15.2@MMLCommand@LST IPBINDVPN
type: MMLCommand
name: LST IPBINDVPN（查询接口绑定VPN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPBINDVPN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IP绑定VPN
status: active
---

# LST IPBINDVPN（查询接口绑定VPN）

## 功能

该命令用于查询接口绑定VPN。

若不指定IFNAME参数时，则查询所有接口绑定的VPN；若指定IFNAME参数时，则查询指定接口绑定的VPN。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于表示绑定VPN的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPBINDVPN]] · 接口绑定VPN（IPBINDVPN）

## 使用实例

查询接口绑定VPN：

```
LST IPBINDVPN:IFNAME="Ethernet64/0/1";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
      接口名  =  Ethernet64/0/1
    IPv4地址  =  192.168.1.1
IPv4地址掩码  =  255.255.0.0
 VPN实例名称  =  __mpp_vpn_inner__
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPBINDVPN.md`
