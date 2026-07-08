---
id: UNC@20.15.2@MMLCommand@SET N40QUOTACTRL
type: MMLCommand
name: SET N40QUOTACTRL（设置N40接口配额的控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: N40QUOTACTRL
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
- 全局配置
status: active
---

# SET N40QUOTACTRL（设置N40接口配额的控制参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用来控制N40接口配额的控制参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ZEROQUOTAACT | ZEROTIMEQTACT | BLKTIMER | ONLMETERINGTYPE | TCMODE |
| --- | --- | --- | --- | --- |
| NORMAL | TERMINATE | 0 | DEFAULT | DEFAULT |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ZEROQUOTAACT | CHF下发零配额的动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CHF下发零配额时的处理动作。<br>数据来源：本端规划<br>取值范围：<br>- “NORMAL（正常处理）”：按正常配额处理，下发零配额给UPF。<br>- “BLCK_TRG_RPT（BLCK_TRG_RPT）”：阻塞业务，后续有Trigger触发时，上报Charging Data Request Update消息。<br>- “BLCK_IMMED_RPT（BLCK_IMMED_RPT）”：阻塞业务，立即触发一条原因为Final的Charging Data Request Update消息。<br>- “BLCK_NO_RPT（阻塞业务）”：阻塞业务。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40QUOTACTRL查询当前参数配置值。<br>配置原则：无 |
| ZEROTIMEQTACT | CHF下发零时长配额的动作 | 可选必选说明：可选参数<br>参数含义：该参数用于控制CHF响应消息中GrantedUnit中携带零时长配额的动作。<br>数据来源：本端规划<br>取值范围：<br>- “TERMINATE（去活会话）”：去活PDU会话。<br>- “ACCEPT（接受）”：按正常时长配额处理。<br>- “NOTCTRL（忽略）”：忽略时长配额控制。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40QUOTACTRL查询当前参数配置值。<br>配置原则：<br>该配置与BYTE504 BIT1冲突时，按软参配置生效。<br>该参数仅在参数ZEROQUOTAACT配置为NORMAL时生效。 |
| BLKTIMER | RG级阻塞处理时间间隔(分钟) | 可选必选说明：该参数在"ZEROQUOTAACT"配置为"BLCK_IMMED_RPT"、"BLCK_NO_RPT"时为条件可选参数。<br>参数含义：该参数用于指定RG级阻塞动作的业务阻塞时间。从阻塞开始经过配置时长以后，业务再来时可以重新触发配额申请。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~1440。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40QUOTACTRL查询当前参数配置值。<br>配置原则：无 |
| ONLMETERINGTYPE | 在线计费上报统计类型 | 可选必选说明：可选参数<br>参数含义：该参数用于控制CHF仅下发在线计费RG时长或流量配额时，是否同时上报时长和流量的使用情况给CHF。<br>数据来源：全网规划<br>取值范围：<br>- “DEFAULT（缺省）”：按GrantedUnit下发的配额类型上报给CHF。<br>- “TIME_VOLUME（同时上报时长和流量）”：同时上报时长和流量使用情况给CHF。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40QUOTACTRL查询当前参数配置值。<br>配置原则：无 |
| TCMODE | 费率切换模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定零点时是否强制发生费率切换。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（缺省）”：费率切换发生的时间点按费率切换配置（ADD TARIFFGROUP）生效。<br>- “DAILY（每天零点强制费率切换）”：在费率切换配置基础上，每天00：00再强制进行费率切换，生效范围为所有用户。<br>- “MONTHLY（月初第一天零点强制费率切换）”：在费率切换配置基础上，月初第一天00：00再强制进行费率切换，生效范围为所有用户。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40QUOTACTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N40QUOTACTRL]] · N40接口配额的控制参数（N40QUOTACTRL）

## 使用实例

设置SMF收到零配额动作为阻塞不上报：

```
SET N40QUOTACTRL: ZEROQUOTAACT=BLCK_NO_RPT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-N40QUOTACTRL.md`
