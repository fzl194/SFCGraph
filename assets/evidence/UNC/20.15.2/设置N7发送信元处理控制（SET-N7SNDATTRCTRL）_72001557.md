# 设置N7发送信元处理控制（SET N7SNDATTRCTRL）

- [命令功能](#ZH-CN_MMLREF_0272001557__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0272001557__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0272001557__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0272001557__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0272001557)

**适用NF：GGSN**

该命令用于设置N7接口发送的消息中部分信元的处理方式。

## [注意事项](#ZH-CN_MMLREF_0272001557)

- 该命令执行后立即生效。

- 修改GERAN和UTRAN为TRUE时，需要提前和对端PCF确认是否支持23G接入。
- GERAN和UTRAN为FALSE时，RatType和位置相关的Trigger不生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| GERAN | UTRAN |
| --- | --- |
| FALSE | FALSE |

#### [操作用户权限](#ZH-CN_MMLREF_0272001557)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0272001557)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GERAN | 携带GERAN类信元 | 可选必选说明：可选参数<br>参数含义：该参数用于指定2G接入时N7接口是否携带GERAN类信元。设置为使能时，2G接入时N7接口支持携带sgsnAddr、geraLocation、rattype信元。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7SNDATTRCTRL查询当前参数配置值。<br>配置原则：无 |
| UTRAN | 携带UTRAN类信元 | 可选必选说明：可选参数<br>参数含义：该参数用于指定3G接入时N7接口是否携带UTRAN类信元。设置为使能时，3G接入时N7接口支持携带sgsnAddr、utraLocation、rattype信元。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7SNDATTRCTRL查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0272001557)

使能N7接口消息中支持携带2G、3G相关的信元。

```
SET N7SNDATTRCTRL: GERAN=TRUE, UTRAN=TRUE;
```
