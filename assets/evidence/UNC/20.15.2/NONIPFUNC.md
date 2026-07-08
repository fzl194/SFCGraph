# 设置Non-IP功能配置（SET NONIPFUNC）

- [命令功能](#ZH-CN_MMLREF_0228567659__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0228567659__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0228567659__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0228567659__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0228567659)

**适用NF：SGW-C、PGW-C**

该命令用于配置整机Non-IP功能相关的信息。

## [注意事项](#ZH-CN_MMLREF_0228567659)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NONIPSWITCH |
| --- |
| DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0228567659)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0228567659)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NONIPSWITCH | Non-IP功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启和关闭Non-IP功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NONIPFUNC查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0228567659)

使能Non-IP功能，则可以进行如下设置：

```
SET NONIPFUNC: NONIPSWITCH=ENABLE;
```
