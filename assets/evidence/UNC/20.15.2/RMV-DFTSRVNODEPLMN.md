# 删除默认PLMN（RMV DFTSRVNODEPLMN）

- [命令功能](#ZH-CN_MMLREF_0209652341__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652341__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652341__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652341__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652341)

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于删除UNC设备默认的PLMN。

## [注意事项](#ZH-CN_MMLREF_0209652341)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652341)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652341)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 结点类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网元类型。<br>数据来源：本端规划<br>取值范围：<br>- SGSN（SGSN）<br>- SGW（SGW）<br>- PGW（PGW）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652341)

删除PGW默认所属的PLMN为46002（MCC=460, MNC=02）：

```
RMV DFTSRVNODEPLMN:NODETYPE=PGW;
```
