# 设置IMS DDN流量控制上报CHR配置开关（SET IMSDDNFLOWCTRLCHR）

- [命令功能](#ZH-CN_MMLREF_0000001149776577__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001149776577__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001149776577__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001149776577__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001149776577)

**适用NF：SGW-C**

该命令用来设置语音IMS的DDN消息流控时是否上报CHR单据功能的开关。

## [注意事项](#ZH-CN_MMLREF_0000001149776577)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| IMSDDNFLOWCTRLCHR |
| --- |
| DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0000001149776577)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001149776577)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSDDNFLOWCTRLCHR | IMS DDN流量控制上报CHR配置开关 | 可选必选说明：可选参数<br>参数含义：该参数用来设置IMS DDN流量控制上报CHR配置开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSDDNFLOWCTRLCHR查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001149776577)

设置语音IMS的DDN消息流控时上报CHR单据开关使能，IMSDDNFLOWCTRLCHR为ENABLE：

```
SET IMSDDNFLOWCTRLCHR: IMSDDNFLOWCTRLCHR=ENABLE;
```
