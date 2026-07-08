---
id: UNC@20.15.2@MMLCommand@SET AMFAUSFRESET
type: MMLCommand
name: SET AMFAUSFRESET（设置AMF的AUSF故障处理策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFAUSFRESET
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF的AUSF故障处理策略
status: active
---

# SET AMFAUSFRESET（设置AMF的AUSF故障处理策略）

## 功能

**适用NF：AMF**

该命令用于设置AMF的AUSF故障处理策略。

## 注意事项

- 该命令执行后在下次AUSF故障时生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RECOVCHANGE | SCANMODE | RATE | INTERVAL | SCANNUM |
| --- | --- | --- | --- | --- |
| OFF | DEFAULT | 1 | 1 | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RECOVCHANGE | recoveryTime变化时重选AUSF开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定AUSF的recoveryTime变化时是否重选AUSF。AUSF的recoveryTime改变时，会发NFUpdate消息给NRF，携带改变后的recoveryTime信元，然后NRF发NFStatusNotify消息给AMF。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFAUSFRESET查询当前参数配置值。<br>配置原则：无 |
| SCANMODE | 扫描模式 | 可选必选说明：可选参数<br>参数含义：该参数表示扫描模式。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（默认扫描模式）”：使用RATE设置的扫描速率。<br>- “CUSTOM（自定义扫描模式）”：使用通过SCANNUM除以INTERVAL得到的自定义扫描速率。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFAUSFRESET查询当前参数配置值。<br>配置原则：无 |
| RATE | 扫描速率(个/秒) | 可选必选说明：该参数在"SCANMODE"配置为"DEFAULT"时为条件可选参数。<br>参数含义：该参数用于指定每个DS每秒扫描多少个用户，对符合重选条件用户在后续需要鉴权的流程中重选AUSF并进行鉴权。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~20，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFAUSFRESET查询当前参数配置值。<br>配置原则：<br>DS个数 × 扫描速率 = 整系统扫描速率。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="UeamCtrlSvc coordinator all";<br>如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |
| INTERVAL | 单位扫描时间(秒) | 可选必选说明：该参数在"SCANMODE"配置为"CUSTOM"时为条件可选参数。<br>参数含义：该参数用于表示AUSF故障后AMF对用户扫描的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~600，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFAUSFRESET查询当前参数配置值。<br>配置原则：无 |
| SCANNUM | 单位扫描个数 | 可选必选说明：该参数在"SCANMODE"配置为"CUSTOM"时为条件可选参数。<br>参数含义：该参数用于表示每个DS每隔INTERVAL设置的时间扫描多少个用户，对符合重选条件用户在后续需要鉴权的流程中重选AUSF并进行鉴权。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~20，单位是个。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFAUSFRESET查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFAUSFRESET]] · AMF的AUSF故障处理策略（AMFAUSFRESET）

## 使用实例

设置AUSF的recoveryTime变化时重选AUSF，使用默认扫描模式，扫描速率为2，执行如下命令：

```
SET AMFAUSFRESET:RECOVCHANGE=ON,SCANMODE=DEFAULT,RATE=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-AMFAUSFRESET.md`
