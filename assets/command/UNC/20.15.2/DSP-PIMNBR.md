---
id: UNC@20.15.2@MMLCommand@DSP PIMNBR
type: MMLCommand
name: DSP PIMNBR（查询PIM邻居信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PIMNBR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM邻居信息
status: active
---

# DSP PIMNBR（查询PIM邻居信息）

## 功能

该命令用于显示PIM邻居信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| NBRADDR | PIM邻居地址 | 可选必选说明：可选参数<br>参数含义：该参数用来表示PIM邻居地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PIMNBR]] · PIM邻居信息（PIMNBR）

## 使用实例

显示PIM邻居信息：

```
DSP PIMNBR:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
                      VPN实例名称 = _public_
                         接口名称 = Ethernet64/0/6
                      PIM邻居地址 = 192.168.15.1
            PIM邻居已经存在的时间 = 00:00:51
          PIM邻居还有多少时间超时 = 00:00:00
                   是否存在优先级 = TRUE
                         DR优先级 = 1
                    是否存在GenID = TRUE
                PIM邻居状态随机数 = 0x338e3931
             PIM邻居生存时间（s） = 105
                是否存在Lan-delay = TRUE
传递Prune剪枝消息的延迟时间（ms） = 500
    否决Prune剪枝的时间间隔（ms） = 2500
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PIMNBR.md`
