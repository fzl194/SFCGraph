---
id: UNC@20.15.2@MMLCommand@DSP REGNFINFO
type: MMLCommand
name: DSP REGNFINFO（显示NF信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: REGNFINFO
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF实例管理
status: active
---

# DSP REGNFINFO（显示NF信息）

## 功能

**适用NF：NRF**

该命令用于查询NF实例的Profile信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示待查询的NF实例标识，可以通过DSP REGNFINSTANCE命令查询ID消息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF信息（REGNFINFO）](configobject/UNC/20.15.2/REGNFINFO.md)

## 使用实例

查询NF实例的Profile信息：

```
DSP REGNFINFO: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
%%DSP REGNFINFO: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";%%
RETCODE = 0  操作成功

结果如下
------------------------
NF Profile Information  =  {
	"allowedNfDomains": [
		"domains1",
		"domains2"
	],
	},
	"capacity": 0,
	"fqdn": "tac-123.epc.mnc003.mcc123.3gppnetwork.org",
	"heartBeatTimer": 60,
	"interPlmnFqdn": "tac-123.epc.mnc003.mcc123.3gppnetwork.org",
	"ipv4Addresses": [
		"10.0.0.0"
	],
	"ipv6Addresses": [
		"2001:db8:0:1:1:1:1:1"
	],
	"load": 0,
	"locality": "china",
	"nfInstanceId": "123e4567-e89b-12d3-a456-426655440000",
	"nfServicePersistence": false,
	"nfServices": [
		{
			"allowedNfDomains": [
				"domains1",
				"domains2"
			],
			"fqdn": "tac-123.epc.mnc003.mcc123.3gppnetwork.org",
			"interPlmnFqdn": "tac-123.epc.mnc003.mcc123.3gppnetwork.org",
			"ipEndPoints": [
				{
					"ipv4Address": "10.0.0.1",
					"transport": "TCP",
					"port": 5031
				}
			],
			"load": 0,
			"nfServiceStatus": "REGISTERED",
			"priority": 0,
			"recoveryTime": "2019-03-01T20:20:20Z",
			"scheme": "http",
			"serviceInstanceId": "service_instance_0",
			"serviceName": "namf-comm",
			"supportedFeatures": "e345",
			"versions": [
				{
					"apiVersionInUri": "v1",
					"apiFullVersion": "1.0.0.0"
				}
			]
		}
	],

}
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NF信息（DSP-REGNFINFO）_09652204.md`
