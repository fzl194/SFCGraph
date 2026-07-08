# 设置Credit Pooling功能（SET CREDITPOOLFUNC）

- [命令功能](#ZH-CN_MMLREF_0000002210761361__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002210761361__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002210761361__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002210761361__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000002210761361)

**适用NF：PGW-C、GGSN**

该命令用于设置Credit Pooling功能参数。

## [注意事项](#ZH-CN_MMLREF_0000002210761361)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CREDITPOOLSW |
| --- |
| DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0000002210761361)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002210761361)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CREDITPOOLSW | Credit Pooling功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置Credit Pooling功能开关。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：不开启Credit Pooling功能。<br>- “ENABLE（使能）”：开启Credit Pooling功能。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CREDITPOOLFUNC查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000002210761361)

需要支持Credit Pooling功能时，可以执行如下命令：

```
SET CREDITPOOLFUNC:CREDITPOOLSW=ENABLE;
```
