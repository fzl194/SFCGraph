---
id: UNC@20.15.2@MMLCommand@DSP SMSFKEYDATA
type: MMLCommand
name: DSP SMSFKEYDATA（显示SMSF用户关键信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMSFKEYDATA
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 热备容灾
status: active
---

# DSP SMSFKEYDATA（显示SMSF用户关键信息）

## 功能

**适用NF：SMSF**

该命令用于查询5G SMSF注册用户的关键信息，包括用户信息、用户短消息签约信息等。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示SMSF用户查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “SUPI（SUPI）”：填写用户的IMSI<br>- “GPSI（GPSI）”：填写用户的MSISDN<br>默认值：无<br>配置原则：无 |
| SUPI | SUPI | 可选必选说明：该参数在"QUERYOPT"配置为"SUPI"时为条件必选参数。<br>参数含义：该参数用于表示SMSF用户SUPI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| GPSI | GPSI | 可选必选说明：该参数在"QUERYOPT"配置为"GPSI"时为条件必选参数。<br>参数含义：该参数用于表示SMSF用户GPSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFKEYDATA]] · 用户的SMSF关键信息（SMSFKEYDATA）

## 使用实例

当运营商希望查询SUPI为"123033500100001"的SMSF用户的关键信息时，执行如下命令：

```
DSP SMSFKEYDATA: QUERYOPT=SUPI, SUPI="123033500100001";
%%DSP SMSFKEYDATA: QUERYOPT=SUPI, SUPI="123033500100001";%%
RETCODE = 0  操作成功

结果如下：
------------------------
        SUPI  =  123033500100001
		GPSI  =  8613535000001
        AMF ID  =  AMF_Instance_0
      备份AMF信息 = {amf2.cluster1.net2.amf.5gc.mnc003.mcc460.3gppnetwork.org,46001822700}
        是否签约MT服务  =  TRUE
		是否禁止MT服务  =  FALSE
        是否禁止MT漫游服务  =  FALSE
		是否签约MO服务  =  TRUE
		是否禁止MO服务  =  FALSE
        是否禁止MO漫游服务  =  FALSE
		SMSF号 = 8613902111010
        跟踪区标识 =  12303350101
        NR小区全球标识 =  12303350110201
       GUAMIS = 12303822700
        AMF binding头域 =  NULL
是否由容灾恢复流程创建关键信息 = FALSE
          do索引 = 3
        用户关键信息更新时间  =  2023-07-22 11:30:44.288+00:00

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SMSFKEYDATA.md`
