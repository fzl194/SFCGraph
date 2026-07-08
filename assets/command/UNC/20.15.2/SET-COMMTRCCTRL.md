---
id: UNC@20.15.2@MMLCommand@SET COMMTRCCTRL
type: MMLCommand
name: SET COMMTRCCTRL（设置通用模块跟踪控制功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: COMMTRCCTRL
command_category: 配置类
applicable_nf:
- AMF
- SMF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# SET COMMTRCCTRL（设置通用模块跟踪控制功能）

## 功能

![](设置通用模块跟踪控制功能（SET COMMTRCCTRL）_00083280.assets/notice_3.0-zh-cn_2.png)

修改该命令可能导致跟踪功能不可用，请谨慎使用并联系华为技术支持协助操作。

**适用NF：AMF、SMF、SMSF、NCG**

该命令用于设置通用模块跟踪功能控制参数，以控制特定的模块是否上报跟踪。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RPTFLOWCTRLMSG |
| --- |
| OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| E2ENOTREPORT | E2E跟踪不上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否不上报E2E跟踪消息。<br>数据来源：本端规划<br>取值范围：<br>- TOPO（TOPO）<br>- GTPSIG（GTPSIG）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMMTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| ITFNOTREPORT | 接口跟踪不上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否不上报接口跟踪消息。<br>数据来源：本端规划<br>取值范围：<br>- GTPC（GTPC）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMMTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| USERNOTREPORT | 用户跟踪不上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否不上报用户跟踪消息。<br>数据来源：本端规划<br>取值范围：<br>- TOPO（TOPO）<br>- GTPSIG（GTPSIG）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMMTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| RANDOMNOTREPORT | 随机跟踪不上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否不上报随机跟踪消息。<br>数据来源：本端规划<br>取值范围：<br>- TOPO（TOPO）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMMTRCCTRL查询当前参数配置值。<br>配置原则：无 |
| RPTFLOWCTRLMSG | 上报跟踪流控的消息开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TOPO、GTPC、LOCM所在进程是否上报跟踪流控消息。当开关为OFF时，不上报跟踪流控消息。<br>数据来源：本端规划<br>取值范围：<br>- OFF（OFF）<br>- ON（ON）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMMTRCCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/COMMTRCCTRL]] · 通用模块跟踪控制功能（COMMTRCCTRL）

## 使用实例

假设需要关闭TOPO模块的用户跟踪功能时，可以执行如下命令：

```
SET COMMTRCCTRL: USERNOTREPORT=TOPO-1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置通用模块跟踪控制功能（SET-COMMTRCCTRL）_00083280.md`
