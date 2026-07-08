# 设置FPI差异化控制功能（SET FPIFUNC）

- [命令功能](#ZH-CN_CONCEPT_0000206725006876__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206725006876__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206725006876__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206725006876__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206725006876__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206725006876)

**适用NF：UPF、PGW-U**

该命令用于设置FPI差异化控制功能。

#### [注意事项](#ZH-CN_CONCEPT_0000206725006876)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | FPISWITCH | FPITRANSMETHOD | FPIPOLICYORIGIN |
| --- | --- | --- | --- |
| 初始值 | ENABLE | DSCP | NULL |

#### [操作用户权限](#ZH-CN_CONCEPT_0000206725006876)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206725006876)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FPISWITCH | FPI使能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置FPI差异化控制功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| FPITRANSMETHOD | FPI传递类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FPISWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于设置FPI传递类型。<br>数据来源：本端规划<br>取值范围：<br>- GTPU：配置FPI信息以GTP-U方式向RAN侧传递。<br>- DSCP：配置FPI信息以DSCP方式向RAN侧传递。<br>默认值：无<br>配置原则：无 |
| FPIPOLICYORIGIN | 策略来源 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FPITRANSMETHOD”配置为“GTPU”时为必选参数。<br>参数含义：该参数用于设置FPI策略来源。<br>数据来源：本端规划<br>取值范围：<br>- INTERNAL：表示FPI值来源于网关内部策略。<br>- EXTERNAL：表示FPI值来源于下行用户报文的IP DSCP值，是由外部策略网元设置。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206725006876)

设置FPI差异化控制功能为使能，FPI传递方式为DSCP方式：

```
SET FPIFUNC: FPISWITCH=ENABLE, FPITRANSMETHOD=DSCP;
```
