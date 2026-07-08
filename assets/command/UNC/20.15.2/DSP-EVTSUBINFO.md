---
id: UNC@20.15.2@MMLCommand@DSP EVTSUBINFO
type: MMLCommand
name: DSP EVTSUBINFO（显示网络开放事件的订阅信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: EVTSUBINFO
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 网络开放管理
- 查询网络开放事件订阅信息
status: active
---

# DSP EVTSUBINFO（显示网络开放事件的订阅信息）

## 功能

**适用NF：AMF**

该命令用于查询指定用户的网络开放事件的订阅信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于标识网络开放事件订阅信息的查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（IMSI）”：IMSI<br>- “MSISDN（MSISDN）”：MSISDN<br>- “IMEI（IMEI）”：IMEI<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"QUERYOPT"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定待查询订阅信息的用户的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"QUERYOPT"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定待查询订阅信息的用户的MSISDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：该参数在"QUERYOPT"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于指定待查询订阅信息的用户的IMEI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [网络开放事件的订阅信息（EVTSUBINFO）](configobject/UNC/20.15.2/EVTSUBINFO.md)

## 使用实例

查询IMSI为460121866587用户当前被订阅的网络开放事件信息，执行如下命令：

```
%%DSP EVTSUBINFO: QUERYOPT=IMSI, IMSI="460121866587";%%
RETCODE = 0  操作成功

结果如下
------------------------
事件订阅信息  =  [
	{
		"eventList": [
			{
				"type": "REACHABILITY_REPORT",
				"immediateFlag": true
			}
		],
		"eventNotifyUri": "http://10.10.10.10:53552/namf-evts/eventnotify/v1/subscriptions/08b1a0181209088810120400100021",
		"notifyCorrelationId": "1111111111",
		"subCorrelationId": "001637d81615e1383aab6df",
		"nfId": "bf33a517-7789-4637-b675-b3591b0d706b",
		"groupId": "groupid-11112222-460-01-01020304050607080900",
		"options": {
			"trigger": "CONTINUOUS",
			"maxReports": 1000,
			"expiry": "2020-06-11T19:24:12+08:00"
		}
	}
]
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示网络开放事件的订阅信息（DSP-EVTSUBINFO）_45495623.md`
