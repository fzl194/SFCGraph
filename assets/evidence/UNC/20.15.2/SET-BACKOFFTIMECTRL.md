# 设置异常场景的Back-off Time开关（SET BACKOFFTIMECTRL）

- [命令功能](#ZH-CN_MMLREF_0296243091__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296243091__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296243091__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296243091__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0296243091)

**适用NF：GGSN、PGW-C、SGW-C**

该命令用来指定异常场景下激活响应中是否携带Back-off Time字段。

## [注意事项](#ZH-CN_MMLREF_0296243091)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| APNLOCKBOTSW | GGSNBOTSW | BRLIMITBOTSW |
| --- | --- | --- |
| DISABLE | DISABLE | DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0296243091)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0296243091)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNLOCKBOTSW | 控制APN锁定导致激活失败应答消息中携带Back-off Time字段的开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制APN锁定导致激活失败应答消息中是否携带Back-off Time。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIMECTRL查询当前参数配置值。<br>配置原则：<br>取值为ENBALE时表示携带Back-off Time；否则不携带。 |
| GGSNBOTSW | 控制激活应答消息中携带GGSN Back-off Time字段的开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制激活应答消息中是否携带GGSN Back-off Time。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIMECTRL查询当前参数配置值。<br>配置原则：<br>取值为ENBALE时表示携带GGSN Back-off Time；否则不携带。 |
| BRLIMITBOTSW | 控制承载受限导致激活失败应答消息中携带Back-off Time字段的开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制因为承载受限导致激活失败应答消息中是否携带Back-off Time字段。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST BACKOFFTIMECTRL查询当前参数配置值。<br>配置原则：<br>取值为ENBALE时表示携带Back-off Time字段；否则不携带。 |

## [使用实例](#ZH-CN_MMLREF_0296243091)

当运营商需要设置因APN锁定而激活失败的响应中携带Back-off time参数时，配置如下：

```
SET BACKOFFTIMECTRL: APNLOCKBOTSW = ENABLE;
```
