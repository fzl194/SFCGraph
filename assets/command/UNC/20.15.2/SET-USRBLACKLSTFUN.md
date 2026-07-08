---
id: UNC@20.15.2@MMLCommand@SET USRBLACKLSTFUN
type: MMLCommand
name: SET USRBLACKLSTFUN（设置用户黑名单接入控制功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: USRBLACKLSTFUN
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 接入限制
- 黑名单接入限制
status: active
---

# SET USRBLACKLSTFUN（设置用户黑名单接入控制功能）

## 功能

![](设置用户黑名单接入控制功能（SET USRBLACKLSTFUN）_65393486.assets/notice_3.0-zh-cn_2.png)

执行此命令，如果参数“RESTRICTSW”误配为“YES”，可能导致用户无法接入。

**适用NF：SGSN、MME、AMF**

该命令用于设置用户黑名单接入限制功能开关以及拒绝原因值。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RESTRICTSW | N2REJCAUSE | S1REJCAUSE | IUREJCAUSE | GBREJCAUSE |
| --- | --- | --- | --- | --- |
| NO | 0 | 0 | 0 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESTRICTSW | 接入限制开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制系统是否支持用户黑名单接入限制功能。<br>黑名单接入限制的用户列表通过ADD USRBLACKLST命令配置。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：否<br>- “YES（是）”：是<br>默认值：无。<br>配置原则：无 |
| N2REJCAUSE | N2模式拒绝原因值 | 可选必选说明：该参数在"RESTRICTSW"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于设置用户由于黑名单接入限制导致流程失败时，下发给UE的原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~111。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST USRBLACKLSTFUN查询当前参数配置值。<br>配置原则：<br>参数取值为0，表示不使用特殊指定原因值，发生该异常时系统将下发#15（No suitable cells in tracking area）原因值。<br>原因值为1表示非协议定义原因值，不建议配置。<br>参数修改为非0值，可能会改变此参数所控制的异常场景中下发给终端的拒绝原因值，从而导致相应拒绝类话统指标的变化。 |
| S1REJCAUSE | S1模式拒绝原因值 | 可选必选说明：该参数在"RESTRICTSW"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于设置用户由于黑名单接入限制导致流程失败时，下发给UE的原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~111。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST USRBLACKLSTFUN查询当前参数配置值。<br>配置原则：<br>参数取值为0，表示不使用特殊指定原因值，发生该异常时系统将下发#15（No suitable cells in tracking area）原因值。<br>原因值为1表示非协议定义原因值，不建议配置。<br>参数修改为非0值，可能会改变此参数所控制的异常场景中下发给终端的拒绝原因值，从而导致相应拒绝类话统指标的变化。 |
| IUREJCAUSE | IU模式拒绝原因值 | 可选必选说明：该参数在"RESTRICTSW"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于设置用户由于黑名单接入限制导致流程失败时，下发给UE的原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~111。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST USRBLACKLSTFUN查询当前参数配置值。<br>配置原则：<br>参数设置为0，表示不使用特殊指定原因值，发生该异常时系统将下发#7(GPRS services not allowed)。<br>原因值为1表示非协议定义原因值，不建议配置。<br>参数修改为非0值，可能会改变此参数所控制的异常场景中下发给终端的拒绝原因值，从而导致相应拒绝类话统指标的变化。 |
| GBREJCAUSE | GB模式拒绝原因值 | 可选必选说明：该参数在"RESTRICTSW"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于设置用户由于黑名单接入限制导致流程失败时，下发给UE的原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~111。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST USRBLACKLSTFUN查询当前参数配置值。<br>配置原则：<br>参数设置为0，表示不使用特殊指定原因值，发生该异常时系统将下发#14(GPRS services not allowed in this PLMN)原因值。<br>原因值为1表示非协议定义原因值，不建议配置。<br>参数修改为非0值，可能会改变此参数所控制的异常场景中下发给终端的拒绝原因值，从而导致相应拒绝类话统指标的变化。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRBLACKLSTFUN]] · 用户黑名单接入控制功能（USRBLACKLSTFUN）

## 使用实例

设置开启用户黑名单接入限制功能，并且N2模式拒绝原因值为#15（No suitable cells in tracking area）原因值，执行如下命令：

```
SET USRBLACKLSTFUN: RESTRICTSW=YES, N2REJCAUSE=15;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-USRBLACKLSTFUN.md`
