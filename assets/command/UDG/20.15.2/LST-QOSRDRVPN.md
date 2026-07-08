---
id: UDG@20.15.2@MMLCommand@LST QOSRDRVPN
type: MMLCommand
name: LST QOSRDRVPN（查询QoS重定向VPN）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: QOSRDRVPN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 重定向VPN
status: active
---

# LST QOSRDRVPN（查询QoS重定向VPN）

## 功能

该命令用于查询非本地报文重定向到指定VPN的配置。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| VRFNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定重定向VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [QoS重定向VPN（QOSRDRVPN）](configobject/UDG/20.15.2/QOSRDRVPN.md)

## 使用实例

查询所有的重定向VPN配置：

```
LST QOSRDRVPN:;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
   接口名称  =  Ethernet66/0/3
    VPN名称  =  vpn1
   (结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询QoS重定向VPN（LST-QOSRDRVPN）_49961018.md`
