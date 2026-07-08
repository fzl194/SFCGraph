---
id: UDG@20.15.2@MMLCommand@DSP MGMDGROUP
type: MMLCommand
name: DSP MGMDGROUP（查询IGMP加入组信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MGMDGROUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- IGMP组播组信息
status: active
---

# DSP MGMDGROUP（查询IGMP加入组信息）

## 功能

该命令用于显示IGMP加入组信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [IGMP加入组信息（MGMDGROUP）](configobject/UDG/20.15.2/MGMDGROUP.md)

## 使用实例

显示IGMP加入组信息：

```
DSP MGMDGROUP:ADDRESSFAMILY=ipv4unicast,VRFNAME="_public_";
```

```
RETCODE = 0  操作成功。

结果如下
--------
                     VPN实例名称  =  _public_
                        接口名称  =  Ethernet64/0/5
                          组地址  =  239.0.0.1
上一次发送report报文的主机IP地址  =  192.168.61.2
                    表项建立时间  =  00:00:50
                    表项超时时间  =  00:02:00
            最后一个成员查询次数  =  0
          最后一个成员查询定时器  =  off
                      源过滤模式  =  Exclude
                V1主机存在定时器  =  off
                V2主机存在定时器  =  off
                          组标记  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IGMP加入组信息（DSP-MGMDGROUP）_49802502.md`
