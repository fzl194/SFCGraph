---
id: UNC@20.15.2@MMLCommand@SET CHFINIT
type: MMLCommand
name: SET CHFINIT（设置融合计费模板中用户激活相关参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CHFINIT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 融合计费模板
status: active
---

# SET CHFINIT（设置融合计费模板中用户激活相关参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置融合计费模板（Converged Charging Template）中用户激活相关参数。

## 注意事项

- 该命令执行后立即生效。

- 该命令的CCTMPLTNAME参数使用ADD CCT命令配置生成。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CCTMPLTNAME | CHFINIT | CCRINITRGNUM | WAITCHFRESP | RGSOURCE |
| --- | --- | --- | --- | --- |
| global | SENDREQ | 5 | ENABLE | DEFAULT |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置融合计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无。<br>配置原则：无 |
| CHFINIT | CHF交互使能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置融合计费模板中用户激活时是否需要到CHF交互。<br>数据来源：本端规划<br>取值范围：<br>- SENDREQ（激活发送）<br>- NOTSENDREQ（激活不发送）<br>- INITRGTRIGR（有预申请RG触发发送）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查询当前参数配置值。<br>配置原则：无 |
| CCRINITRGNUM | 初始RG个数 | 可选必选说明：可选参数<br>参数含义：该参数用于配置融合计费模板中用户激活时发送的初始请求消息中允许携带RG的最大个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~10。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查询当前参数配置值。<br>配置原则：无 |
| WAITCHFRESP | CHF交互等待CHF响应开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置融合计费模板中用户激活需要到CHF交互的情况下是否需要等待CHF响应。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查询当前参数配置值。<br>配置原则：<br>暂不支持配置此参数，默认等待CHF响应。 |
| RGSOURCE | RG来源 | 可选必选说明：可选参数<br>参数含义：该参数用于配置融合计费模板中用户激活需要到CHF交互的情况下所携带的RG来源。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（缺省配置）”：该参数仅对PCC用户生效，使用PCF下发的规则向CHF预申请配额。各种规则优先级为：动态规则>预定义规则>预定义规则组(UserProfile)。对于预定义规则组(UserProfile)使用其CtxStartRating配置<br>- “CTXSTARTRATING（CTX命令设置RG）”：该参数表示使用配置的预定义规则组(UserProfile)的CtxStartRating配置去CHF申请配额<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CCT查询当前参数配置值。<br>配置原则：<br>当该参数设置为DEFAULT时，在新增UPF与在线恢复场景下，仅使用PCF下发的动态规则向CHF预申请配额。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHFINIT]] · 融合计费模板中用户激活相关参数（CHFINIT）

## 使用实例

设置名为“test”的CCT融合计费模板的中用户激活时是需要到CHF交互：

```
SET CHFINIT: CCTMPLTNAME="test", CHFINIT=SENDREQ;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CHFINIT.md`
