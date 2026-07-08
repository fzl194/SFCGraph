---
id: UNC@20.15.2@MMLCommand@DSP NDNEIGHBOR
type: MMLCommand
name: DSP NDNEIGHBOR（显示IPv6 ND邻居表项）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NDNEIGHBOR
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND表项
status: active
---

# DSP NDNEIGHBOR（显示IPv6 ND邻居表项）

## 功能

该命令用于显示ND表项。

不指定参数时，查询设备上所有ND表项信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYCOND | 查询条件 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ND邻居表项查询条件。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV6ADDRESS：IPv6地址。<br>- VRFNAME：VPN名称。<br>- IFNAME：接口名称。<br>默认值：无 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYCOND”配置为“IPV6ADDRESS”时为必选参数。<br>参数含义：该参数用于显示IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| VRFNAME | VPN名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYCOND”配置为“VRFNAME”时为必选参数。<br>参数含义：该参数用于显示VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYCOND”配置为“IFNAME”时为必选参数。<br>参数含义：该参数用于显示接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NDNEIGHBOR]] · 静态ND邻居表项（NDNEIGHBOR）

## 使用实例

显示ND表项：

```
DSP NDNEIGHBOR:QUERYCOND=IFNAME,IFNAME="Ethernet65/0/8";
```

```

RETCODE = 0  操作成功。

结果如下
--------
IPv6地址           VPN名称        接口名            MAC地址           表项状态    存活时间（min）    安全     VLAN索引    CE VLAN索引

2001:db8::11       _public_       Ethernet65/0/8    00e0-fc01-0001    可达        NULL               TRUE     NULL        NULL
2001:db8::12       _public_       Ethernet65/0/8    00e0-fc01-0002    不完整      0                  FALSE    NULL        NULL
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NDNEIGHBOR.md`
