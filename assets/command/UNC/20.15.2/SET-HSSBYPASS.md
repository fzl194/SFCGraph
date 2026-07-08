---
id: UNC@20.15.2@MMLCommand@SET HSSBYPASS
type: MMLCommand
name: SET HSSBYPASS（设置HSS故障Bypass功能控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: HSSBYPASS
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HSS故障BYPASS功能
status: active
---

# SET HSSBYPASS（设置HSS故障Bypass功能控制参数）

## 功能

**适用网元：MME**

该命令用于设置HSS故障Bypass功能控制参数。开启HSS全故障智能业务逃生功能开关后，在HSS全故障状态下业务可以惯性运行。

## 注意事项

- 该命令执行后立即生效。

- 此命令的最大记录数为1。
- 相关license授权并开启后，此命令配置才生效（License部件编码：LKV2HSSBP01）。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BPSW | HSS Bypass功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启和关闭HSS Bypass功能。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>系统初始设置值：OFF（关闭）<br>配置原则：无 |
| MSISDNCHK | MSISDN检查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否检查已进入HSS Bypass状态的用户的MSISDN，如果检查并且用户不存在MSISDN，不允许用户附着或者创建会话。<br>数据来源：全网规划<br>取值范围：<br>- NO（否）<br>- YES（是）<br>系统初始设置值：YES（是）<br>配置原则：无<br>说明：相关license授权并开启后，此参数配置不生效（License部件编码：LKV2NOISDN02）。 |
| RECOVERYACT | 退出Bypass状态恢复动作 | 可选必选说明：可选参数<br>参数含义：该参数用于设置退出HSS Bypass状态恢复动作。<br>数据来源：全网规划<br>取值范围：<br>- GRACEFUL_DEREG（优雅分离）：MME向HSS发送Update Location Request探测消息，当HSS响应消息状态码符合退出Bypass条件时，MME根据用户当前状态退出HSS Bypass，具体恢复动作为：若用户处于连接态，MME待用户进入空闲态后发起显式分离流程，并标记用户退出HSS Bypass状态；若用户处于空闲态，MME寻呼用户成功后发起显式分离流程，并标记用户退出HSS Bypass状态；若用户处于分离态，MME标记用户退出HSS Bypass状态。<br>- SUPPLEMENT_INTERACT（补充缺失流程）：MME补齐和HSS交互的位置更新和Notify流程，若成功则标记用户退出HSS Bypass状态，否则继续标记用户处于HSS Bypass状态。<br>系统初始设置值：SUPPLEMENT_INTERACT（补充缺失流程）<br>配置原则：无<br>说明：当用户没有MSISDN时，按照GRACEFUL_DEREG（优雅分离）退出Bypass状态，该参数不生效。 |
| SCANRATE | 整系统扫描速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定HSS Bypass状态的用户扫描速率。该参数为0时，按照10min扫描一轮。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~10000，单位是个/秒。<br>系统初始设置值：0（个/秒）。<br>配置原则：该参数应能被SPP进程个数的十倍整除，否则该参数将向上取整。例如，SPP进程数为4，当该参数设为41~80(个/秒)时，实际扫描速率按80(个/秒)处理。<br>说明：该参数修改后，待下一轮扫描该参数生效。若想要快速生效，可通过<br>**[STR HSSBPEXIT](启动用户退出HSS BYPASS状态(STR HSSBPEXIT)_20995641.md)**<br>重新触发用户扫描。 |
| SCANINTERVAL | 扫描时间间隔(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于表示开启HSS Bypass功能后，允许用户连续两次向HSS发探测消息的最小时间间隔。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~600，单位是秒。<br>系统初始设置值：600（秒）。<br>配置原则：<br>- 如果达到扫描时间间隔后，当前任务未扫描完成，则下一个扫描时间间隔后再尝试启动。<br>- 如果达到扫描时间间隔后，当前任务已扫描完成，则立即启动重新扫描。<br>- 当系统正在扫描时，该参数修改不生效。<br>- 当扫描到无用户在HSS Bypass状态时，停止扫描。 |
| RPTFAILCHR | 上报异常CHR开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当用户进入和退出HSS Bypass的状态时，是否上报异常CHR单据。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>系统初始设置值：ON（开启）<br>配置原则：无 |
| AUTOEXITSW | HSS Bypass自动退出开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否开启用户自动退出HSS Bypass状态开关。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>系统初始设置值：ON（开启）<br>配置原则：若本参数设置为“OFF”，在HSS恢复后，用户无法及时退出HSS Bypass状态，可能导致用户业务持续受到影响。建议本参数设置“ON”。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HSSBYPASS]] · HSS故障Bypass功能控制参数（HSSBYPASS）

## 使用实例

设置HSS故障Bypass功能控制参数，指定整系统扫描速率(个/秒)为100、扫描时间间隔(秒)为200：

```
SET HSSBYPASS: SCANRATE=100, SCANINTERVAL=200;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-HSSBYPASS.md`
