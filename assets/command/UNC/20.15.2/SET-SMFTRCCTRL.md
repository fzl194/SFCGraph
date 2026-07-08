---
id: UNC@20.15.2@MMLCommand@SET SMFTRCCTRL
type: MMLCommand
name: SET SMFTRCCTRL（设置SMF跟踪控制功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMFTRCCTRL
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# SET SMFTRCCTRL（设置SMF跟踪控制功能）

## 功能

![](设置SMF跟踪控制功能（SET SMFTRCCTRL）_77579580.assets/notice_3.0-zh-cn_2.png)

修改该命令可能导致跟踪功能不可用，请谨慎使用并联系华为技术支持协助操作。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置SMF跟踪功能控制参数。

## 注意事项

- 该命令执行后立即生效。

- 该命令中的部分参数取值（TOPO、GTPSIG、GTPC）已废弃，由SET COMMTRCCTRL命令取代。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LAN5GNOTREPORT | BRC5GNOTREPORT | RPTFLOWCTRLMSG |
| --- | --- | --- |
| DISABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| E2EIEIGNORE | E2E信元忽略开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否忽略E2E跟踪信元。当忽略E2E跟踪信元时，系统不会上报E2E跟踪消息，也不会向下游网元传递跟踪信元。<br>数据来源：本端规划<br>取值范围：<br>- SMC（SMC）<br>- CM4G（CM4G）<br>- CM5G（CM5G）<br>- POLICY4G（POLICY4G）<br>- POLICY5G（POLICY5G）<br>- ACCT（ACCT）<br>- UESM（UESM）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| E2ENOTREPORT | E2E跟踪不上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否不上报E2E跟踪消息。<br>数据来源：本端规划<br>取值范围：<br>- SMC（SMC）<br>- CM4G（CM4G）<br>- CM5G（CM5G）<br>- POLICY4G（POLICY4G）<br>- POLICY5G（POLICY5G）<br>- ACCT（ACCT）<br>- UESM（UESM）<br>- UPC（UPC）<br>- “TOPO（TOPO）”：已废弃。<br>- “GTPSIG（GTPSIG）”：已废弃。<br>- VNGM（VNGM）<br>- DHCP（DHCP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| E2ENOTTRANSFER | E2E跟踪信元不传递开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否向下游网元传递跟踪信元。<br>数据来源：本端规划<br>取值范围：<br>- UPF（UPF）<br>- PGW（PGW）<br>- PCF（PCF）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| ITFNOTREPORT | 接口跟踪不上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否不上报接口跟踪消息。<br>数据来源：本端规划<br>取值范围：<br>- “GTPC（GTPC）”：已废弃。<br>- N4（N4）<br>- USMGa（USM Ga）<br>- Gy（Gy）<br>- Gx（Gx）<br>- USMGTPU（USM GTPU）<br>- S6b（S6b）<br>- Gi（Gi）<br>- DHCP（DHCP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| USERNOTREPORT | 用户跟踪不上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否不上报用户跟踪消息。<br>数据来源：本端规划<br>取值范围：<br>- SMC（SMC）<br>- CM4G（CM4G）<br>- CM5G（CM5G）<br>- POLICY4G（POLICY4G）<br>- POLICY5G（POLICY5G）<br>- ACCT（ACCT）<br>- UESM（UESM）<br>- UPC（UPC）<br>- “TOPO（TOPO）”：已废弃。<br>- “GTPSIG（GTPSIG）”：已废弃。<br>- VNGM（VNGM）<br>- DHCP（DHCP）<br>- SMSECM（SMSECM）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| RANDOMNOTREPORT | 随机用户跟踪不上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否不上报随机跟踪消息。<br>数据来源：本端规划<br>取值范围：<br>- SMC（SMC）<br>- CM4G（CM4G）<br>- CM5G（CM5G）<br>- POLICY4G（POLICY4G）<br>- POLICY5G（POLICY5G）<br>- ACCT（ACCT）<br>- UESM（UESM）<br>- UPC（UPC）<br>- “TOPO（TOPO）”：已废弃。<br>- VNGM（VNGM）<br>- SMSECM（SMSECM）<br>- DHCP（DHCP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| LAN5GNOTREPORT | 5G LAN组会话跟踪不上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否不上报5G LAN组会话跟踪消息。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| BRC5GNOTREPORT | 5G广播跟踪不上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否不上报5G广播跟踪消息。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| RPTFLOWCTRLMSG | 上报跟踪流控的消息开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否上报跟踪流控消息。当开关为DISABLE时，不上报跟踪流控消息。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFTRCCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [SMF跟踪控制功能（SMFTRCCTRL）](configobject/UNC/20.15.2/SMFTRCCTRL.md)

## 使用实例

假设需要关闭SMC模块的用户跟踪功能时，可以执行如下命令：

```
SET SMFTRCCTRL:USERNOTREPORT=SMC-1&CM4G-0&CM5G-0&POLICY4G-0&POLICY5G-0&ACCT-0&UESM-0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMF跟踪控制功能（SET-SMFTRCCTRL）_77579580.md`
