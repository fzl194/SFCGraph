---
id: UNC@20.15.2@MMLCommand@STR ENBTASYN
type: MMLCommand
name: STR ENBTASYN（启动eNodeB跟踪区信息同步任务）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: ENBTASYN
command_category: 动作类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- eNodeB管理
- eNodeB跟踪区同步
status: active
---

# STR ENBTASYN（启动eNodeB跟踪区信息同步任务）

## 功能

**适用NF：MME**

该命令用于启动eNodeB跟踪区信息同步任务，可以根据输入参数选择所有eNodeB、以进程为单位或者以eNodeB为单位的同步任务。

## 注意事项

- 在Tm接口链路正常的情况下使用。

- 正常情况下不要执行，只有在TSN侧需要MME重新上报时才需要执行。
- 此命令执行后立即生效。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBTASYNTYPE | TA同步类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定同步任务的类型。<br>取值范围：<br>- “ALL（全部eNodeB）”：表示将让所有eNodeB重新上报跟踪区信息。<br>- “SPEACIAL_PROCESS（指定SGP进程）”：表示让指定SGP进程上关联的eNodeB重新上报跟踪区信息。<br>- “ENODEBID（指定eNodeB ID）”：表示让指定eNodeB重新上报跟踪区信息。<br>默认值：ALL |
| RUNAME | RU名称 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要同步eNodeB跟踪区信息的资源单元名称。该参数可以通过<br>**[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)**<br>命令查询。<br>前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“SPEACIAL_PROCESS（指定SGP进程）”值后生效。<br>取值范围：1~63位字符串<br>默认值：无 |
| PROCID | 进程号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要同步eNodeB跟踪区信息的SGP进程的进程号。该参数可以通过<br>**[DSP PROCESSLINK](../../../../../../平台服务管理/操作维护/VNFC公共功能管理/操作维护/系统调测/进程管理/查询LINK进程信息(DSP PROCESSLINK)_11295772.md)**<br>命令查询，选取结果中的“相同进程类型的索引”列。<br>前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“SPEACIAL_PROCESS（指定SGP进程）”值后生效。<br>取值范围：0~20<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待同步的eNodeB对应的移动国家代码。<br>前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“ENODEB_ID（指定eNodeB ID）”值后生效。<br>数据来源：整网规划<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待同步的eNodeB对应的移动网号。<br>前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“ENODEB_ID（指定eNodeB ID）”值后生效。<br>数据来源：整网规划<br>取值范围：2位或者3位十进制数字<br>默认值：无 |
| ENBTYPE | eNodeB类型 | 可选必选说明：条件必选参数<br>参数含义：待同步的eNodeB的类型。<br>前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“ENODEB_ID（指定eNodeB ID）”值后生效。<br>取值范围：<br>- “HOME_ENB(HOME_ENB)”：28位长的eNodeB。<br>- “MACRO_ENB(MACRO_ENB)”：20位长的eNodeB。<br>默认值：无 |
| ENBID | eNodeB标识 | 可选必选说明：条件必选参数<br>参数含义：待同步的eNodeB ID。该参数可以通过<br>**[DSP S1APLNK](../../../S1接口管理/S1AP链路/显示S1AP连接状态(DSP S1APLNK)_26146252.md)**<br>命令查询。<br>前提条件：该参数在“ENBTASYNTYPE（TA同步类型）”参数配置为“ENODEB_ID（指定eNodeB ID）”值后生效。<br>取值范围：0~268435455<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ENBTASYN]] · eNodeB跟踪区信息同步任务（ENBTASYN）

## 使用实例

1. 启动所有eNodeB重新上报跟踪区信息：
  STR ENBTASYN: ENBTASYNTYPE=ALL;
2. 启动进程号为0的SGP进程关联的eNodeB重新上报跟踪区信息：
  STR ENBTASYN: ENBTASYNTYPE=SPEACIAL_PROCESS, RUNAME="USN_SP_RU_0064", PROCID=0;
3. 启动移动国家代码为460，移动网号为00，标识为1104的eNodeB重新上报跟踪区信息：
  STR ENBTASYN: ENBTASYNTYPE=ENODEB_ID, MCC="460", MNC="00", ENBTYPE=MACRO_ENB, ENBID=1104;

## 证据

- 原始手册：`evidence/UNC/20.15.2/STR-ENBTASYN.md`
