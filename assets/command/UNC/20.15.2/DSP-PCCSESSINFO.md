---
id: UNC@20.15.2@MMLCommand@DSP PCCSESSINFO
type: MMLCommand
name: DSP PCCSESSINFO（显示PCC会话信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PCCSESSINFO
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCC维护
- PCC会话查询
status: active
---

# DSP PCCSESSINFO（显示PCC会话信息）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询指定IMSI、MSISDN或IMEI的会话中所有的承载、PCC规则的安装情况，以及规则的生效失效时间、流量监控、profile-space、PRA等相关信息，适用于PCC用户。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERIDTYPE | 用户标识类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要查询的用户类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：按IMSI查询用户信息。<br>- MSISDN：按MSISDN查询用户信息。<br>- IMEI：按IMEI查询用户信息。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERIDTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：该参数用于指定被查询用户的MSISDN号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERIDTYPE”配置为“IMSI”时为必选参数。<br>参数含义：该参数用于指定被查询用户的IMSI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERIDTYPE”配置为“IMEI”时为必选参数。<br>参数含义：该参数用于指定被查询用户的IMEI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| DISPLAYMODE | 显示方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定显示用户会话信息的模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SIMPLE：显示用户的会话信息。<br>- VERBOSE：显示用户的会话详细信息。<br>- USG_MONITORING：显示用户的Usage Monitoring信息。<br>默认值：SIMPLE<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCSESSINFO]] · PCC会话信息（PCCSESSINFO）

## 使用实例

- Gx接口：查询IMSI为123011223344551的在线用户的会话信息：
  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551";
  ```
  ```

  RETCODE = 0  操作成功。

  PCC Session 信息
  -----------------------
  结果  =  
  Pcc Session 信息 IMSI 123031500010001 on Pod uncpod-0
  (No:1)
  -----------------------------------------------------------

  承载的QoS信息:
  ---------------------------
  QFI   QCI   Arp.PriorityLevel   Arp.preemptCap      Arp.preemptVuln     
  1     7     2                   May Preempt         Not Preemptable     

  承载的动态规则信息  [QFI:1]
  -----------------------------------------------------
  No    规则名称            规则来源            优先级
  1     rule2               PCRF Created        1000
  (结果个数 = 1)

  ---    END
  ```
- Gx接口：查询IMSI为123011223344551的在线用户的会话详细信息：
  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551", DISPLAYMODE=VERBOSE;
  ```
  ```

  RETCODE = 0  操作成功。

  PCC Session 信息
  -----------------------
  结果  =
  Pcc Session 信息 IMSI 123031500010001 on Pod uncpod-0
  (No:1)
  -----------------------------------------------------------

  Qosflow information :
  ---------------------------
  No   QFI   FiveQI   PriorityLevel   Arp.PriorityLevel   Arp.preemptCap   Arp.preemptVuln   MaxDataBurstVol   AverWindow    Qnc
  1    1     7        0               2                   May Preempt      Preemptable       0                 0             false

  Predefined Rule Information
  ---------------------------
  No   RuleName         Type             PolicyType
  1    any_uptolocalpcc UserProfile Rule PCC
  (结果个数 = 1)

  ---    END
  ```
- Gx接口：查询IMSI为123011223344551的在线用户的Usage Monitoring信息：
  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551", DISPLAYMODE=USG_MONITORING;
  ```
  ```

  RETCODE = 0  操作成功。

  PCC Session 信息
  -----------------------
  结果  =
  Pcc Session 信息 IMSI 123031500010001 on Pod uncpod-0
  (No:1)
  -----------------------------------------------------------

  Qosflow information :
  ---------------------------
  No   QFI   FiveQI   PriorityLevel   Arp.PriorityLevel   Arp.preemptCap   Arp.preemptVuln   MaxDataBurstVol   AverWindow    Qnc
  1    1     7        0               2                   May Preempt      Preemptable       0                 0             false

  Predefined Rule Information
  ---------------------------
  No   RuleName         Type             PolicyType
  1    any_uptolocalpcc UserProfile Rule PCC
  (结果个数 = 1)

  ---    END
  ```
- N7接口：查询IMSI为123011223344551的在线用户的会话信息：
  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551";
  ```
  ```

  RETCODE = 0  操作成功

  PCC会话信息
  -----------
  查询结果  =  
  PCC session information for IMSI 123011223344551 on Pod uncpod-0
  (session id: 5)
  -----------------------------------------

  Qosflow information :
  ---------------------
  No   QFI   FiveQI   PriorityLevel   Arp.PriorityLevel   Arp.preemptCap   Arp.preemptVuln   MaxDataBurstVol   AverWindow    Qnc
  1    1     5        0               3                   Not Preempt      Preemptable       0                 0             false

  Dynamic Rule Information of QosFlow/Bearer [QFI:1] 
  ---------------------------------------------------
  No   RuleName  RuleSource      Priority
  1    PccRule1  PCF created     1

  IPE Session Information
  --------------------
  IPE-Session-Associated-Indicator = false
  (结果个数 = 1)

  ---    END
  ```
- N7接口：查询IMSI为123011223344551的在线用户的会话详细信息：
  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551", DISPLAYMODE=VERBOSE;
  ```
  ```

  RETCODE = 0  操作成功。

  PCC Session 信息
  -----------------------
  结果  =
  Pcc Session 信息 IMSI 123031500010001 on Pod uncpod-0
  (No:1)
  -----------------------------------------------------------

  Qosflow information :
  ---------------------------
  No   QFI   FiveQI   PriorityLevel   Arp.PriorityLevel   Arp.preemptCap   Arp.preemptVuln   MaxDataBurstVol   AverWindow    Qnc
  1    1     5        0               1                   May Preempt      Preemptable       0                 0             false

  Predefined Rule Information
  ---------------------------
  No   RuleName         Type             PolicyType
  1    any_uptolocalpcc UserProfile Rule PCC

  IPE Session Information
  --------------------
  IPE-Session-Associated-Indicator = false
  (结果个数 = 1)

  ---    END
  ```
- N7接口：查询IMSI为123011223344551的在线用户的Usage Monitoring信息：
  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551", DISPLAYMODE=USG_MONITORING;
  ```
  ```

  RETCODE = 0  操作成功。

  PCC Session 信息
  -----------------------
  结果  =
  Pcc Session 信息 IMSI 123031500010001 on Pod uncpod-0
  (No:1)
  -----------------------------------------------------------

  Qosflow information :
  ---------------------------
  No   QFI   FiveQI   PriorityLevel   Arp.PriorityLevel   Arp.preemptCap   Arp.preemptVuln   MaxDataBurstVol   AverWindow    Qnc
  1    1     5        0               1                   May Preempt      Preemptable       0                 0             false

  Predefined Rule Information
  ---------------------------
  No   RuleName         Type             PolicyType
  1    any_uptolocalpcc UserProfile Rule PCC

  IPE Session Information
  --------------------
  IPE-Session-Associated-Indicator = false
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PCCSESSINFO.md`
