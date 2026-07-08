---
id: UNC@20.15.2@MMLCommand@DSP NRFLINKINFO
type: MMLCommand
name: DSP NRFLINKINFO（显示NRF管理的链路信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFLINKINFO
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- 链路管理
status: active
---

# DSP NRFLINKINFO（显示NRF管理的链路信息）

## 功能

**适用NF：NRF**

该命令可以查询NRF管理的链路信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERID | 对端标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF链路管理表中维护的当前链路数据的对端标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| PEERIDTYPE | 对端标识类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF链路管理表中维护的当前链路数据的对端标识类型。<br>数据来源：本端规划<br>取值范围：<br>- NRFLAYER（NRF分层链路）<br>- CALLBACKURL（状态通知回调链路）<br>- ASFWD（主备转发链路）<br>- NRFREG（NRF向北向NRF注册的链路）<br>- NFDETECT（NRF向NF的主动探测链路）<br>- OTHER（其他动态链路）<br>默认值：无<br>配置原则：无 |
| LINKSTATUS | 链路状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF链路管理表中维护的当前链路数据的链路状态。<br>数据来源：本端规划<br>取值范围：<br>- INVALID（未知状态 ）<br>- FAULT（故障状态 ）<br>- NORMAL（正常状态）<br>- OVERLOAD（过载状态）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFLINKINFO]] · NRF管理的链路信息（NRFLINKINFO）

## 使用实例

查询NRF管理的链路信息：

```
%%DSP NRFLINKINFO: PEERIDTYPE=CALLBACKURL;%%
RETCODE = 0  操作成功

结果如下
------------------------
Link information  =  {
	"PeerId": "10.70.200.1:5164",
	"PeerIdType": "CALLBACKURL",
	"LinkStatus": "NORMAL",
	"RetryAfterSeconds": 0,
	"AddrMsgStatus": "NotRecv",
	"LinkUpdateTime": "2020-03-16T21:17:06+08:00",
	"RecordCreateTime": "2020-03-16T21:17:06+08:00",
	"OverLoadBeginTime": "1970-01-01T08:00:00+08:00",
	"LogicLink": "AAEBRhNGyAEsFADFnRyBAAA=",
	"SbiInfo": {
		"NotifyType": "Add",
		"InfoType": "Callback",
		"PeerId": "10.70.200.1:5164",
		"NFType": "AMF",
		"Scheme": "http",
		"Fqdn": "tac-123.epc.mnc003.mcc123.3gppnetwork.org",
		"Ipv4Addresses": [
			"10.70.200.1:5164"
		],
		"Ipv6Addresses": null
	}
}
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NRF管理的链路信息（DSP-NRFLINKINFO）_31773562.md`
