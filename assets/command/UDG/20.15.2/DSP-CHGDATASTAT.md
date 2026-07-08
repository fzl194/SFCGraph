---
id: UDG@20.15.2@MMLCommand@DSP CHGDATASTAT
type: MMLCommand
name: DSP CHGDATASTAT（显示计费数据统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CHGDATASTAT
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务监控
- 业务统计管理
- 计费数据统计信息
status: active
---

# DSP CHGDATASTAT（显示计费数据统计信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

用来查询计费数据统计信息，比如预定义URR流量上报信息、UserProfile安装次数、整体转发和计费流量差异比例信息、缺省费率流量增量信息、子协议Top30的流量增量信息、预定义规则Top20的匹配次数增量信息、URR Top20的流量增量信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATTYPE | 统计类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要显示计费数据的统计类型。<br>数据来源：本端规划<br>取值范围：ENUM。<br>- UPINSTALL：查询UserProfile安装次数。<br>- URRVOLUME：查询URR流量统计信息。<br>- WHOLE_VOLUME_CONDITION：整体转发和计费流量差异比例信息。<br>- TOPN_URR_VOLUME：URR流量增量Top20信息。<br>- RULE_MATCH_NUM：预定义PCC规则Top20的匹配次数增量信息。<br>- PROTOCOL_VOLUME：协议Top30的流量增量信息。<br>- DEFAULT_URR_VOLUME：缺省费率流量增量信息。<br>默认值：无<br>配置原则：无 |
| URRID | URRID(Predef) | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATTYPE”配置为“URRVOLUME”时为可选参数。<br>参数含义：用于指示URR标识（预定义）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2147483646。<br>默认值：无<br>配置原则：无 |
| USERPROFILENAME | UserProfileName | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATTYPE”配置为“UPINSTALL”时为可选参数。<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DATETYPE | 周期类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATTYPE”配置为“DEFAULT_URR_VOLUME”、“PROTOCOL_VOLUME”、“RULE_MATCH_NUM”、“TOPN_URR_VOLUME” 或 “WHOLE_VOLUME_CONDITION”时为可选参数。<br>参数含义：该参数用于指定要显示计费数据的查询周期，支持按天查近七天数据或按月查近期6个月数据。<br>数据来源：本端规划<br>取值范围：ENUM。<br>- DAY：天。<br>- MONTH：月。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CHGDATASTAT]] · 计费数据统计信息（CHGDATASTAT）

## 使用实例

- 查询URR流量统计数据：
  ```
  %%DSP CHGDATASTAT: STATTYPE=URRVOLUME;
  ```
  ```
  %%
  RETCODE = 0  Operation succeeded

  Charging Data Statistics
  ------------------------
  Result                                                                                                                

  URRID      ReportVolume(Total)  ReportVolume(Today)  ReportVolume(YesterDay)  ReportVolume(The Day Before Yesterday)  
  1          3000                   2970               2940                     2910                                    
  2          4000                   3980               3960                     3940                                                                        
  (Number of results = 3)

  ---    END
  ```
- 查询UserProfile安装次数信息：
  ```
  %%DSP CHGDATASTAT: STATTYPE=UPINSTALL;
  ```
  ```
  %%
  RETCODE = 0  Operation succeeded

  UserProfile Installation Count
  ------------------------------
                              UserProfileName  =  up
                            InstallCnt(Total)  =  1
                            InstallCnt(Today)  =  1
                        InstallCnt(Yesterday)  =  0
         InstallCnt(The Day Before Yesterday)  =  0
  (Number of results = 1)

  ---    END
  ```
- 查询协议Top30的流量增量信息：
  ```
  %%DSP CHGDATASTAT: STATTYPE=PROTOCOL_VOLUME, DATETYPE=DAY;
  ```
  ```
  %%
  RETCODE = 0  Operation succeeded

  Protocol Volume Statistics
  --------------------------
  Result  =  

  ssgpod-0 Top30 Protocol Volume Information:
  Last 1Day:
  No.  ProtocolName                    Volume
  1    http                            360

  (Number of results = 1)
  ```
- 查询整体转发和计费流量差异比例信息：
  ```
  %%DSP CHGDATASTAT: STATTYPE=WHOLE_VOLUME_CONDITION, DATETYPE=DAY;
  ```
  ```
  %%
  RETCODE = 0  Operation succeeded

  whole volume condition
  ----------------------
  Result  =  

  ssgpod-0:
  Lost ratio type     Last 1Day           
  uplinkvolume        0.000%(100/100)              
  dnlinkvolume        0.000%(100/100)              
  uplinkpktnum        0.000%(1/1)              
  dnlinkpktnum        0.000%(1/1)              

  (Number of results = 1)

  ---    END
  ```
- 查询预定义规则Top20的匹配次数增量信息：
  ```
  %%DSP CHGDATASTAT: STATTYPE=RULE_MATCH_NUM, DATETYPE=DAY;
  ```
  ```
  %%
  RETCODE = 0  Operation succeeded

  Rule Match Num Statistics
  --------------------------
  Result  =  

  ssgpod-0 Top20 Rule Match Num Information:
  Last 1Day:
  No.  RuleName                                                          RuleMatchNum
  1    rule1                                                             360

  (Number of results = 1)
  ```
- 查询URR Top20的流量增量信息：
  ```
  %%DSP CHGDATASTAT: STATTYPE=TOPN_URR_VOLUME, DATETYPE=DAY;
  ```
  ```
  %%
  RETCODE = 0  Operation succeeded

  Top20 URR Volume Statistics
  --------------------------
  Result  =  

  ssgpod-0 Top20 URR Volume Information:
  Last 1Day:
  No.  URRID       Volume
  1    1           1360

  (Number of results = 1)
  ```
- 查询缺省费率流量增量信息：
  ```
  %%DSP CHGDATASTAT: STATTYPE=DEFAULT_URR_VOLUME, DATETYPE=DAY;
  ```
  ```
  %%
  RETCODE = 0  Operation succeeded

  Default URR Volume Statistics
  --------------------------
  Result  =  
  ssgpod-0:
  Volume Type     Last 1Day
  uplink          482
  dnlink          1440

  (Number of results = 1)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-CHGDATASTAT.md`
