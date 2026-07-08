---
id: UNC@20.15.2@MMLCommand@LST AMFCONFLICTRULE
type: MMLCommand
name: LST AMFCONFLICTRULE（查询AMF冲突规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFCONFLICTRULE
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF冲突配置管理
status: active
---

# LST AMFCONFLICTRULE（查询AMF冲突规则）

## 功能

**适用NF：AMF**

该命令用于AMF查询冲突规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | CS类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CS的类型。<br>数据来源：本端规划<br>取值范围：<br>- UEAM（UEAM模块）<br>- LOCM（LOCM模块）<br>- UEM（UEM模块）<br>- AMPOLICY（AMPOLICY模块）<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程内部标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流程内部标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。不能为非法字符，只允许输入字母，数字，区分大小写。例如：ProcTypeIntraAmfInitialReg。<br>默认值：无<br>配置原则：无 |
| INITEVENTID | 初始事件类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定触发新流程的初始事件类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。不能为非法字符，只允许输入字母，数字，区分大小写。例如：InitIntraRegistration。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFCONFLICTRULE]] · AMF冲突规则（AMFCONFLICTRULE）

## 使用实例

- 查询所有的冲突规则，执行如下命令。
  ```
  %%LST AMFCONFLICTRULE:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  CS类型        流程内部标识                             初始事件类型         冲突流程规则

  UEAM模块      IntraAmfHandover                        InitN2NotifyEvent   {"Name":"When","Children":[{"Name":"ResultPreempt"}]}
  UEAM模块      IntraAmfHandoverCancel                  PathSwitch          {"Name":"When","Children":[{"Name":"ResultPreempt"}]}
  (结果个数 = 2)

  ---    END
  ```
- 查询特定场景下的部分冲突规则，执行如下命令。
  ```
  %%LST AMFCONFLICTRULE: CSTYPE=UEAM, PROCTYPE="IntraAmfHandover", INITEVENTID="InitN2NotifyEvent";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
       CS类型   =  UEAM模块
  流程内部标识   =  IntraAmfHandover
  初始事件类型   =  InitN2NotifyEvent
  冲突流程规则   =  {"Name":"When","Children":[{"Name":"ResultPreempt"}]}
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFCONFLICTRULE.md`
