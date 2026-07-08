---
id: UNC@20.15.2@MMLCommand@DSP VLRKEYDATA
type: MMLCommand
name: DSP VLRKEYDATA（显示VLR用户关键信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VLRKEYDATA
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 热备容灾
status: active
---

# DSP VLRKEYDATA（显示VLR用户关键信息）

## 功能

**适用NF：SMSF**

该命令用于显示VLR注册用户的关键信息，包含用户信息、用户短消息签约信息等。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VLR用户查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（国际移动用户识别码）”：国际移动用户识别码<br>- “MSISDN（移动台国际ISDN号码）”：移动台国际ISDN号码<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"QUERYOPT"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于表示VLR用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"QUERYOPT"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于表示VLR用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLRKEYDATA]] · 用户的VLR关键信息（VLRKEYDATA）

## 使用实例

当运营商希望查询IMSI为"460023500100001"的VLR用户的关键信息时，执行如下命令：

```
DSP VLRKEYDATA: QUERYOPT=IMSI, IMSI="123033500100001";
%%DSP VLRKEYDATA: QUERYOPT=IMSI, IMSI="123033500100001";%%
RETCODE = 0  操作成功

结果如下：
------------------------
                IMSI  =  123033500100001
		MSISDM  =  8613535000001
                是否签约MT服务  =  TRUE
		是否签约MO服务  =  TRUE
		VLR号 = 0
		VLRNAME = VLR01.MNC01.MCC220.3GPPNETWORK.ORG
		MMEN = 1
		位置区标识 = 123036115
		踪区标识 = NULL
              是否由容灾恢复流程创建关键信息表  =  FALSE
              do索引  =  2
               用户关键信息更新时间  =  2023-07-19 19:12:00.405+00:00

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-VLRKEYDATA.md`
