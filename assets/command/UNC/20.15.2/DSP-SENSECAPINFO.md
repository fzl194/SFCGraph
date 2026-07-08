---
id: UNC@20.15.2@MMLCommand@DSP SENSECAPINFO
type: MMLCommand
name: DSP SENSECAPINFO（显示感知基站感知能力信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SENSECAPINFO
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 感知业务管理
- 显示基站感知能力信息
status: active
---

# DSP SENSECAPINFO（显示感知基站感知能力信息）

## 功能

**适用NF：AMF**

在部署感知的场景下，通过本命令可以查询通感基站的感知能力信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SENSERANID | 感知基站ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定感知基站的ID标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>感知基站的标识ID可以通过查看SFG接口跟踪获取，或通过DSP ANINFO命令将"OUTPUTTYPE"参数设置为"Screen"、"NGAPLEIDX"参数设置为0，同时不输入"NGRANNODETYPE"参数，过滤查询所有结果中"NGRANNODETYPE"字段为SFgnb的记录，从记录的“SLAVELIST”参数中获取。 |
| PLMNID | PLMN ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定感知基站的PLMN标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>感知基站的PLMN ID可以通过查看SFG接口跟踪获取，或通过DSP ANINFO命令将"OUTPUTTYPE"参数设置为"Screen"、"NGAPLEIDX"参数设置为0，同时不输入"NGRANNODETYPE"参数，过滤查询所有结果中"NGRANNODETYPE"字段为SFgnb的记录，从记录的“SLAVELIST”参数中获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SENSECAPINFO]] · 感知基站感知能力信息（SENSECAPINFO）

## 使用实例

查询感知基站ID为12345，PLMN ID为12303的基站的感知能力信息时，执行如下命令：

```
%%DSP SENSECAPINFO: SENSERANID=12345, PLMNID=12303;%%
RETCODE = 0  操作成功

操作结果如下
------------
            感知基站ID  =  12345
               PLMN ID  =  12303
        感知主基站标识  =  1
     感知主基站PLMN ID  =  12303
          感知能力信息  =  [
	{
		"SenseCellId": 228,
		"SenseCapState": "Enable",
		"SenseCapDisableReason": "Unspec",
		"SenseCellTaskState": "Enable",
		"SenseWorkingMode": "Normal",
		"SenseScenarioList": [
			{
				"SenseScenarioType": "SeaArea",
				"RefreshingRate": 100
			}
		]
	}
]
感知能力最新刷新时间戳  =  2024-08-23T14:02:39+08:00
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SENSECAPINFO.md`
