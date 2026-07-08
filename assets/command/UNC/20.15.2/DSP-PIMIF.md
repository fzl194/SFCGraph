---
id: UNC@20.15.2@MMLCommand@DSP PIMIF
type: MMLCommand
name: DSP PIMIF（显示PIM接口信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PIMIF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM接口配置
status: active
---

# DSP PIMIF（显示PIM接口信息）

## 功能

该命令用于显示PIM接口信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PIMIF]] · PIM接口配置（PIMIF）

## 使用实例

显示PIM接口信息：

```
DSP PIMIF:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,IFNAME="Ethernet64/0/3";
```

```
RETCODE = 0  操作成功。

结果如下
--------
                             VPN实例名称  =  _public_
                                  地址族  =  IPv4单播
                                接口名称  =  Ethernet64/0/3
             接口上启动的PIM协议的版本号  =  2
                                接口状态  =  Up
                   在接口上的PIM邻居个数  =  0
                                DR优先级  =  1
                        该接口上DR的地址  =  192.168.1.2
                  Hello报文发送间隔（s）  =  30
                    PIM邻居维持时间（s）  =  105
               Assert状态的保持时间（s）  =  180
                     JP报文发送间隔（s）  =  60
                 JP加入剪枝维持时间（s）  =  210
                   接口的Lan-delay（ms）  =  500
Hello消息中否决Prune剪枝的时间间隔（ms）  =  2500
                   接口上的Generation ID  =  0x6f94abf1
                           非DR的NBR个数  =  0
              没有使用Lan-delay的NBR个数  =  0
                        DF选举的健壮系数  =  0
                                 PIM模式  =  稀疏模式
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PIMIF.md`
