---
id: UNC@20.15.2@MMLCommand@SET AMFFCPARA
type: MMLCommand
name: SET AMFFCPARA（设置AMF自保流控参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFFCPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 拥塞控制
- AMF流控参数
status: active
---

# SET AMFFCPARA（设置AMF自保流控参数）

## 功能

![](设置AMF自保流控参数（SET AMFFCPARA）_25121209.assets/notice_3.0-zh-cn_2.png)

执行该命令开启Backoff Timer功能可能导致流控触发后的系统性能下降。

**适用NF：AMF**

该命令用于设置AMF自保流控参数。

## 注意事项

- 该命令执行后立即生效。

- “CPU过载控制门限”参数在UNC 20.5.1版本及之后不再使用。阈值后续通过ADD FCPARAM或MOD FCPARAM命令配置。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CPUTHD | FCACT | BOTSW | MINBOT | MAXBOT |
| --- | --- | --- | --- | --- |
| 70 | DISCARD | OFF | 900 | 1800 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPUTHD | CPU过载控制门限(%) | 可选必选说明：可选参数<br>参数含义：该参数用于设置AMF自保流控功能过载CPU门限。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是50~80。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFFCPARA查询当前参数配置值。<br>配置原则：无 |
| FCACT | 流控措施 | 可选必选说明：可选参数<br>参数含义：该参数用于设置初始注册请求消息被流控时系统采取的措施。其他消息则直接丢弃。<br>数据来源：全网规划<br>取值范围：<br>- “DISCARD（丢弃）”：丢弃初始注册请求消息。<br>- “REJECT（拒绝）”：回复注册拒绝消息，携带原因值为#22 Congestion，如果携带Back off timer信元，用于指示请求消息重复尝试的延迟时长。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFFCPARA查询当前参数配置值。<br>配置原则：无 |
| BOTSW | Backoff Timer信元开关 | 可选必选说明：该参数在"FCACT"配置为"REJECT"时为条件可选参数。<br>参数含义：该参数用于自保流控情况下，注册拒绝消息中是否携带backoff timer信元。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFFCPARA查询当前参数配置值。<br>配置原则：无 |
| MINBOT | Backoff timer最小值(秒) | 可选必选说明：该参数在"BOTSW"配置为"ON"时为条件可选参数。<br>参数含义：本参数用于设置Backoff timer的最小值，用于计算发给终端的Backoff timer时长。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~11160，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFFCPARA查询当前参数配置值。<br>配置原则：无 |
| MAXBOT | Backoff timer最大值(秒) | 可选必选说明：该参数在"BOTSW"配置为"ON"时为条件可选参数。<br>参数含义：本参数用于设置Backoff timer的最大值，用于计算发给终端的Backoff timer时长。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~11160，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFFCPARA查询当前参数配置值。<br>配置原则：<br>该参数的取值必须大于等于“MINBOT（Backoff timer最小值(秒)）”的取值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFFCPARA]] · AMF自保流控参数（AMFFCPARA）

## 使用实例

设置CPU过载控制门限为70%，设置流控措施为丢弃：

```
SET AMFFCPARA:CPUTHD=70,FCACT=DISCARD;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-AMFFCPARA.md`
