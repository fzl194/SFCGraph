---
id: UNC@20.15.2@MMLCommand@CLR ACTIVEALARM
type: MMLCommand
name: CLR ACTIVEALARM（清除活动告警）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: ACTIVEALARM
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 告警管理
status: active
---

# CLR ACTIVEALARM（清除活动告警）

## 功能

本命令用于清除活动告警。

## 注意事项

每次执行最多清除10万条活动告警。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| ME<br>ID | 网元<br>ID | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要清除指定网元的活动告警，网元ID可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询。<br>取值范围：整型，0~65535。<br>默认值：无。<br>配置原则：无。 |
| ALARMID | 告警<br>ID | 可选必选说明：<br>可选参数。<br>参数含义：<br>用于指示系统需要清除指定告警ID的活动告警，可通过<br>**[LST ACTALM](查询活动告警（LST ACTALM）_92570030.md)**<br>查询当前存在的活动告警ID<br>。<br>取值范围：整型，0~999999999。<br>默认值：无。<br>配置原则：<br>- 如果未指定该参数，但是配置了“流水号”，则会按流水号严格匹配清除告警。<br>- 如果未指定该参数，但是配置了“定位信息”，则会按定位信息严格匹配清除告警。<br>- 可选参数如果都为空，则清除网元全部告警。 |
| SNO | 流水号 | 可选必选说明：<br>可选参数。<br>参数含义：用于指示系统需要清除指定流水号的活动告警，流水号指在一个网元内产生的故障告警的序列编号，可通过<br>**[LST ACTALM](查询活动告警（LST ACTALM）_92570030.md)**<br>查询告警流水号。<br>取值范围：整型，1~2147483637。<br>默认值：无<br>。<br>配置原则：<br>- 如果未指定该参数，但是配置了“告警ID”，则会按告警ID严格匹配清除告警。<br>- 如果未指定该参数，但是配置了“定位信息”，则会按定位信息严格匹配清除告警。<br>- 可选参数如果都为空，则清除网元全部告警。 |
| PARAM | 定位信息 | 可选必选说明：<br>可选参数。<br>参数含义：用于指示系统需要清除指定定位信息的活动告警<br>，可通过<br>**[LST ACTALM](查询活动告警（LST ACTALM）_92570030.md)**<br>查询告警定位信息<br>。<br>取值范围：字符串，1~1700。<br>默认值：无。<br>配置原则：<br>- 须填写告警完整的定位信息。<br>- 如果未指定该参数，但是配置了“告警ID”，则会按告警ID严格匹配清除告警。<br>- 如果未指定该参数，但是配置了“流水号”，则会按流水号严格匹配清除告警。<br>- 可选参数如果都为空，则清除网元全部告警。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACTIVEALARM]] · 活动告警（ACTIVEALARM）

## 使用实例

清除 “网元ID” 为 “0” ， “流水号” 为 “663” 的活动告警：

```
%%CLR ACTIVEALARM: MEID=0, SNO=663;%%
```

```
+++    CSP/*MEID:0 MENAME:superom07-v4*/        2026-03-31 16:48:52
O&M    #3883
%%CLR ACTIVEALARM: MEID=0, SNO=663;%%
RETCODE = 0  操作成功

进度报告
--------
已完成 = 0%
(结果个数 = 1)

---    END

+++    CSP/*MEID:0 MENAME:superom07-v4*/        2026-03-31 16:48:52
O&M    #3883
%%CLR ACTIVEALARM: MEID=0, SNO=663;%%
RETCODE = 0  操作成功

进度报告
--------
已完成 = 99%
(结果个数 = 1)

---    END

+++    CSP/*MEID:0 MENAME:superom07-v4*/        2026-03-31 16:48:52
O&M    #3883
%%CLR ACTIVEALARM: MEID=0, SNO=663;%%
RETCODE = 0  操作成功

进度报告
--------
已完成 = 100%
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除活动告警（CLR-ACTIVEALARM）_37102208.md`
