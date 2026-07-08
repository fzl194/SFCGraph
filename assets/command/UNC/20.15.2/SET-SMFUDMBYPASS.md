---
id: UNC@20.15.2@MMLCommand@SET SMFUDMBYPASS
type: MMLCommand
name: SET SMFUDMBYPASS（设置SMF的UDM全故障Bypass相关功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMFUDMBYPASS
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- UDM Bypass管理
- UDM Bypass策略管理
status: active
---

# SET SMFUDMBYPASS（设置SMF的UDM全故障Bypass相关功能）

## 功能

**适用NF：SMF**

该命令用于设置SMF的UDM全故障Bypass功能。当用户要求UDM全故障时业务能惯性运行，需要设置该功能。

## 注意事项

- 该命令执行后立即生效。

- 当"UDM全故障Bypass开关(UDMBYPASS)"由“ON”修改成“OFF”时，SMF上会话会根据已配置的自动退出"Bypass功能开关(AUTOEXITSW)"决定是否自动退出Bypass。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| UDMBYPASS | FAULTDETECTRATE | SCANINTERVAL | RPTFAILCHR | AUTOEXITSW |
| --- | --- | --- | --- | --- |
| OFF | 1 | 600 | ON | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UDMBYPASS | UDM全故障Bypass开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF是否支持基于用户的UDM全故障Bypass功能。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFUDMBYPASS查询当前参数配置值。<br>配置原则：无 |
| FAULTDETECTRATE | 故障探测速率(个/秒) | 可选必选说明：该参数在"UDMBYPASS"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于指定故障探测速率，即每个DS每秒扫描多少个用户，扫描到后对符合重选UDM条件的用户立即重选。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~20，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFUDMBYPASS查询当前参数配置值。<br>配置原则：<br>DS个数 * 扫描速率 = 整系统扫描速率。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="SmcCtrlSvc coordinator all";<br>如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |
| SCANINTERVAL | 扫描时间间隔(秒) | 可选必选说明：该参数在"UDMBYPASS"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于表示UDM Bypass后SMF对用户扫描的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~600，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFUDMBYPASS查询当前参数配置值。<br>配置原则：无 |
| RPTFAILCHR | 上报异常CHR开关 | 可选必选说明：该参数在"UDMBYPASS"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于设置当由于UDM Bypass会话接入成功时，是否上报异常CHR单据。<br>参数意义如下：<br>当设置为ON时，将接入5G成功且进入UDM Bypass的流程（涉及首次PDU会话激活、4到5切换）上报到异常CHR单据。<br>当设置为OFF时，将接入5G成功且进入UDM Bypass的流程（涉及首次PDU会话激活、4到5切换）上报到正常CHR单据。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFUDMBYPASS查询当前参数配置值。<br>配置原则：无 |
| AUTOEXITSW | 自动退出Bypass功能开关 | 可选必选说明：该参数在"UDMBYPASS"配置为"ON"时为条件可选参数。<br>参数含义：该参数是用于控制是否开启用户会话自动退出UDM Bypass状态的开关。<br>值为“ON”时，会话会在UDM恢复后自动退出Bypass。<br>值为“OFF”时，会话会在UDM恢复后，不自动退出。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFUDMBYPASS查询当前参数配置值。<br>配置原则：<br>设置为“OFF”后，在UDM恢复后，用户无法及时退出UDM Bypass状态，用户业务可能会持续受到影响。建议开关保持“ON”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFUDMBYPASS]] · SMF的UDM全故障Bypass相关功能（SMFUDMBYPASS）

## 使用实例

设置UDM全故障进入Bypass的功能为ON，会话的扫描速率为5，单用户扫描间隔时间为600秒，上报异常CHR开关为ON，自动退出Bypass功能为ON。

```
SET SMFUDMBYPASS:UDMBYPASS=ON,FAULTDETECTRATE=5,SCANINTERVAL=600,RPTFAILCHR=ON,AUTOEXITSW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMF的UDM全故障Bypass相关功能（SET-SMFUDMBYPASS）_77037100.md`
