---
id: UNC@20.15.2@MMLCommand@DSP MGMDIF
type: MMLCommand
name: DSP MGMDIF（显示IGMP接口信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MGMDIF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- IGMP接口配置
status: active
---

# DSP MGMDIF（显示IGMP接口信息）

## 功能

该命令用于显示IGMP接口信息。

## 注意事项

- 在监控IGMP接口的状态或检查IGMP接口的故障原因时，可执行命令DSP MGMDIF获取使能IGMP功能的接口上的IGMP配置和运行信息。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MGMDIF]] · IGMP接口配置（MGMDIF）

## 使用实例

显示IGMP接口信息：

```
DSP MGMDIF: VRFNAME="_public_", ADDRESSFAMILY=ipv4unicast, IFNAME="Ethernet64/0/3";
```

```
RETCODE = 0  操作成功。

结果如下
--------
                   VPN实例名称  =  _public_
                        地址族  =  IPv4单播
                      接口名称  =  Ethernet64/0/3
                    接口IP地址  =  10.0.0.1
                      IGMP状态  =  Up
 协商的周期性普遍查询时间（s）  =  1627389951
 配置的周期性普遍查询时间（s）  =  60
        其他查询器存在的定时器  =  0
   普遍查询的最大响应时间（s）  =  10
        最后一个成员查询定时器  =  2
启动时查询器发送查询报文的间隔  =  15
              启动时的查询次数  =  2
              普遍查询的定时器  =  00:00:50
                查询器的IP地址  =  10.0.0.1
查询器是否存在和是否本地查询器  =  本台路由器
          收到的Join报文的个数  =  0
         收到的Leave报文的个数  =  0
            协商的鲁棒稳定系数  =  1627389951
            配置的鲁棒稳定系数  =  2
            查询器启动时的状态  =  Off
              其他查询器的状态  =  Off
        总的收到的Report的个数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MGMDIF.md`
