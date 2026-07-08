# 设置MEP_SMF联动功能开关（SET MEPINTERACT）

- [命令功能](#ZH-CN_MMLREF_0209652370__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652370__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652370__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652370__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652370)

**适用NF：SMF**

该命令用来控制MEP_SMF联动处理，使能开关时，SMF向MEP订阅并接受MEP推送的分流规则和DNS重定向规则，去使能开关时，SMF向MEP去订阅。

## [注意事项](#ZH-CN_MMLREF_0209652370)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH |
| --- |
| DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0209652370)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652370)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SMF是否与MEP联动。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：MEP_SMF联动开关不使能<br>- “ENABLE（使能）”：MEP_SMF联动开关使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MEPINTERACT查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652370)

设置MEP_SMF联动功能开关，SWITCH为ENABLE：

```
SET MEPINTERACT: SWITCH=ENABLE;
```
