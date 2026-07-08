# 删除冲突规则（RMV AMFCONFLICTRULE）

- [命令功能](#ZH-CN_MMLREF_0000001460982529__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001460982529__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001460982529__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001460982529__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001460982529)

![](删除冲突规则（RMV AMFCONFLICTRULE）_60982529.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除冲突规则可能影响现有业务对冲突场景的判断和解决策略，如果需要使用该命令，请联系华为技术支持。

**适用NF：AMF**

该命令用于删除AMF特定的冲突场景下的冲突处理规则。

## [注意事项](#ZH-CN_MMLREF_0000001460982529)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001460982529)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001460982529)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | CS类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CS的类型。<br>数据来源：本端规划<br>取值范围：<br>- UEAM（UEAM模块）<br>- LOCM（LOCM模块）<br>- UEM（UEM模块）<br>- AMPOLICY（AMPOLICY模块）<br>默认值：无<br>配置原则：无 |
| PROCTYPE | 流程内部标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程内部标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。不能为非法字符，只允许输入字母，数字，区分大小写。例如：ProcTypeIntraAmfInitialReg。<br>默认值：无<br>配置原则：无 |
| INITEVENTID | 初始事件类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定触发新流程的初始事件类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。不能为非法字符，只允许输入字母，数字，区分大小写。例如：InitIntraRegistration。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001460982529)

在IntraAmfHandover流程中，收到了NG-RAN的“RRC Inactive Transition Report”消息，如果希望删除该冲突场景下的冲突规则，则执行如下命令。

```
RMV AMFCONFLICTRULE: CSTYPE=UEAM, PROCTYPE="IntraAmfHandover", INITEVENTID="InitN2NotifyEvent";
```
