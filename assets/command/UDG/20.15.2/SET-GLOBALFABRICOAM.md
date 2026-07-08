---
id: UDG@20.15.2@MMLCommand@SET GLOBALFABRICOAM
type: MMLCommand
name: SET GLOBALFABRICOAM（设置OAM全局配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLOBALFABRICOAM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# SET GLOBALFABRICOAM（设置OAM全局配置）

## 功能

![](设置OAM全局配置（SET GLOBALFABRICOAM）_92520017.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置全局OAM（Operation Administration and Maintenance）相关配置：包括OAM使能，OAM报文检测周期，OAM报文超时检测倍数。

报文转发时，需要根据链路状态进行快速选路、负载分担等，因此需要OAM功能检测Fabric口间的链路通断状态并提供依据。

设置全局OAM配置可以使能去使能Fabric OAM功能。OAM功能用来检测链路状态，建议开启，默认情况下也是开启的。

## 注意事项

- 该命令执行后立即生效。
- 如果修改Fabric-OAM开关，影响系统可靠性，如果修改检测间隔，间隔过小或者过大，会导致丢包率上升或者检测能力降低。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| OAMSWITCH | OAMINTERVAL | OAMMULTIPLIER |
| --- | --- | --- |
| enable | 200 | 15 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OAMSWITCH | OAM使能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定OAM功能是否开启。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- disable：去使能。<br>- enable：使能。<br>默认值：无 |
| OAMINTERVAL | OAM报文发送周期（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定OAM报文发送周期，单位为毫秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为100～60000。且有效取值为100毫秒的倍数。<br>默认值：无<br>配置原则：由于OAM探测使用数据面的CPU资源，默认间隔200ms，multiplier是15精度，如果配置成100ms精度对性能有较大影响，且丢包率会上升，随着资源数目增加影响增大，从而影响业务正常使用，建议配置为200ms。 |
| OAMMULTIPLIER | OAM报文超时检测倍数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定OAM报文超时检测倍数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～50。<br>默认值：无<br>配置原则：建议使用默认值15。 |

## 操作的配置对象

- [OAM全局配置（GLOBALFABRICOAM）](configobject/UDG/20.15.2/GLOBALFABRICOAM.md)

## 使用实例

如果用户希望开启OAM功能，周期为200ms，连续15次报文超时，认为OAM链路断，可以使用如下命令设置全局OAM参数：

```
SET GLOBALFABRICOAM:OAMSWITCH=enable,OAMINTERVAL=200,OAMMULTIPLIER=15;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置OAM全局配置（SET-GLOBALFABRICOAM）_92520017.md`
