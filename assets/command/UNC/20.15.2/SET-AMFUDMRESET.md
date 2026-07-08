---
id: UNC@20.15.2@MMLCommand@SET AMFUDMRESET
type: MMLCommand
name: SET AMFUDMRESET（设置AMF的UDM故障处理策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFUDMRESET
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF的UDM故障处理策略
status: active
---

# SET AMFUDMRESET（设置AMF的UDM故障处理策略）

## 功能

**适用NF：AMF**

该命令用于设置AMF的UDM故障处理策略。

## 注意事项

- 该命令执行后在下次UDM故障时生效。

- 扫描速率设置过大可能会对周边UDM产生冲击。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RECOVCHANGE | LINKDOWNORDEREG | BYPRORATE | IMMEDIATESW | IMMEDIATERATE |
| --- | --- | --- | --- | --- |
| ON | OFF | 5 | OFF | 1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RECOVCHANGE | recoveryTime变化时重选UDM开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UDM的recoveryTime变化时AMF是否重选UDM。UDM的recoveryTime改变时，会发NFUpdate消息给NRF，携带改变后的recoveryTime信元，然后NRF发NFStatusNotify消息给AMF。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFUDMRESET查询当前参数配置值。<br>配置原则：无 |
| LINKDOWNORDEREG | 链路故障或者去注册时重选UDM开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定AMF和UDM的链路持续故障、或者UDM的状态更新为去注册时AMF是否重选UDM。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFUDMRESET查询当前参数配置值。<br>配置原则：无 |
| BYPRORATE | 通过流程触发的扫描速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要重选UDM时，每个DS每秒扫描多少个用户，扫描到后对符合重选UDM条件的用户清除相关标记，以便用户在下次注册流程（包括所有注册类型）中重选UDM。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~50，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFUDMRESET查询当前参数配置值。<br>配置原则：<br>DS个数 × 扫描速率 = 整系统扫描速率。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="UeamCtrlSvc coordinator all";<br>如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |
| IMMEDIATESW | 立即触发开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要重选UDM时，是否启动扫描任务，扫描到后对符合重选UDM条件的用户立即重选UDM。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFUDMRESET查询当前参数配置值。<br>配置原则：无 |
| IMMEDIATERATE | 立即触发的扫描速率 | 可选必选说明：该参数在"IMMEDIATESW"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于指定需要重选UDM且“立即触发开关”开启时，每个DS每秒扫描多少个用户，扫描到后对符合重选UDM条件的用户立即重选UDM。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFUDMRESET查询当前参数配置值。<br>配置原则：<br>DS个数 × 扫描速率 = 整系统扫描速率。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="UeamCtrlSvc coordinator all";<br>如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFUDMRESET]] · AMF的UDM故障处理策略（AMFUDMRESET）

## 使用实例

设置UDM的recoveryTime变化时重选UDM，UDM的链路故障或者去注册时不重选UDM，通过流程触发重选UDM的扫描速率为5，关闭立即触发重选UDM开关。

```
SET AMFUDMRESET:RECOVCHANGE=ON,LINKDOWNORDEREG=OFF,BYPRORATE=5,IMMEDIATESW=OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-AMFUDMRESET.md`
