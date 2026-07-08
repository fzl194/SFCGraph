---
id: UDG@20.15.2@MMLCommand@DSP MGMDSOURCE
type: MMLCommand
name: DSP MGMDSOURCE（查询IGMP加入源信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MGMDSOURCE
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

# DSP MGMDSOURCE（查询IGMP加入源信息）

## 功能

该命令用于显示IGMP加入源信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |
| GRPADDR | 组地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于指定组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MGMDSOURCE]] · IGMP加入源信息（MGMDSOURCE）

## 使用实例

显示IGMP加入源信息：

```
DSP MGMDSOURCE:VRFNAME="_public_",IFNAME="Ethernet64/0/5",GRPADDR="239.0.0.1",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
--------
           VPN实例名称  =  _public_
              接口名称  =  Ethernet64/0/5
                组地址  =  239.0.0.1
                源地址  =  192.168.0.1
          表项建立时间  =  00:00:38
          表项超时时间  =  00:02:01
  最后一个成员查询次数  =  0
最后一个成员查询定时器  =  off
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MGMDSOURCE.md`
