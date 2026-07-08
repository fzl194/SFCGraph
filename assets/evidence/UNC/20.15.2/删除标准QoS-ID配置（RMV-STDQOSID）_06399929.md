# 删除标准QoS ID配置（RMV STDQOSID）

- [命令功能](#ZH-CN_MMLREF_0306399929__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0306399929__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0306399929__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0306399929__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0306399929)

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于删除标准QoS ID配置。

## [注意事项](#ZH-CN_MMLREF_0306399929)

- 该命令执行后只对新激活用户生效。

- 配置中的标准QoS ID被EXTENQCIATTR中的EXTQCIMAPDEFQCI或EXTENDQCIMAP中的STANDARDQCI使用时，该配置无法删除。

#### [操作用户权限](#ZH-CN_MMLREF_0306399929)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0306399929)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSIDTYPE | QoS ID类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS ID类型。<br>数据来源：本端规划<br>取值范围：<br>- “QCI（QCI）”：QCI<br>- “FIVEQI（5QI）”：5QI<br>默认值：无<br>配置原则：无 |
| QOSIDSV | QoS ID起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS ID起始值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~255。<br>默认值：无<br>配置原则：<br>该参数的值必须小于等于QoS ID的结束值。 |

## [使用实例](#ZH-CN_MMLREF_0306399929)

删除“QCI=90”的“标准QoS ID”配置：

```
RMV STDQOSID:QOSIDTYPE=QCI,QOSIDSV=90;
```
