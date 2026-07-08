---
id: UNC@20.15.2@MMLCommand@SET CHGIOPARA
type: MMLCommand
name: SET CHGIOPARA（设置融合计费惯性运行参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CHGIOPARA
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
- 惯性运行参数
status: active
---

# SET CHGIOPARA（设置融合计费惯性运行参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于控制融合计费惯性运行参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| N40USAGERPTSW | FINALRPTSW | VTRPTSW | CHFREAUTHRPTSW |
| --- | --- | --- | --- |
| ENABLE | ENABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| N40USAGERPTSW | N40用量上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SMF惯性运行期间是否计费。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：SMF惯性运行期间计费，计费使用量在惯性运行恢复后上报CHF。<br>- “DISABLE（不使能）”：SMF惯性运行期间不计费，计费使用量丢弃，不上报CHF。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGIOPARA查询当前参数配置值。<br>配置原则：无 |
| FINALRPTSW | 惯性运行FINAL上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SMF进入惯性运行时是否向CHF上报所有RG和QF的FINAL用量容器。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：事件发生，不生成流量容器，不上报CHF。<br>- “ENABLE（使能）”：事件发生，不下查用量，SMF构造零用量容器，并上报CHF。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGIOPARA查询当前参数配置值。<br>配置原则：无 |
| VTRPTSW | 惯性运行期间VT触发上报开关 | 可选必选说明：该参数在"FINALRPTSW"配置为"DISABLE"时为条件可选参数。<br>参数含义：该参数用于控制SMF惯性运行期间VT定时器超时是否上报CHF。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：事件发生，不生成流量容器，不上报CHF。<br>- “ENABLE（使能）”：事件发生，不下查用量，SMF构造零用量容器，并上报CHF。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGIOPARA查询当前参数配置值。<br>配置原则：<br>当参数FINALRPTSW配置为ENABLE时，该参数不生效。 |
| CHFREAUTHRPTSW | 惯性运行期间CHF REAUTH触发上报开关 | 可选必选说明：该参数在"FINALRPTSW"配置为"DISABLE"时为条件可选参数。<br>参数含义：该参数用于控制SMF惯性运行期间收到CHF REAUTH请求时是否上报CHF。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：事件发生，不生成流量容器，不上报CHF。<br>- “ENABLE（使能）”：事件发生，不下查用量，SMF构造零用量容器，并上报CHF。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHGIOPARA查询当前参数配置值。<br>配置原则：<br>当参数FINALRPTSW配置为ENABLE时，该参数不生效。 |

## 操作的配置对象

- [融合计费惯性运行参数（CHGIOPARA）](configobject/UNC/20.15.2/CHGIOPARA.md)

## 使用实例

设置SMF惯性运行期间计费，不上报FINAL，使能VT到上报和CHF REAUTH上报：

```
SET CHGIOPARA: N40USAGERPTSW=ENABLE, FINALRPTSW=DISABLE, VTRPTSW=ENABLE, CHFREAUTHRPTSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置融合计费惯性运行参数（SET-CHGIOPARA）_24796838.md`
