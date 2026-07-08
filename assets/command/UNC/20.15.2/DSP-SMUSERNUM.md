---
id: UNC@20.15.2@MMLCommand@DSP SMUSERNUM
type: MMLCommand
name: DSP SMUSERNUM（显示会话管理的用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMUSERNUM
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 查询用户数
status: active
---

# DSP SMUSERNUM（显示会话管理的用户数）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查看SMF/PGW-C/SGW-C/GGSN-C的用户数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRY_SCOPE | 查询范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指示查询用户数的范围。<br>数据来源：本端规划<br>取值范围：<br>- “SUMMARY（汇总信息）”：查询汇总信息。以汇总方式呈现。<br>- “ALL_POD_INFO（所有POD信息）”：查询所有POD信息。以POD粒度呈现。<br>- “SPECIFIED_POD_INFO（指定POD信息）”：查询指定POD信息。<br>默认值：SUMMARY<br>配置原则：无 |
| QRY_CLASS | 查询分类 | 可选必选说明：可选参数<br>参数含义：该参数用于指示查询用户数的分类条件。<br>数据来源：本端规划<br>取值范围：<br>- “APN（APN）”：查询使用该APN激活的当前在线用户数。<br>- “RAT（无线接入类型）”：查询不同无线接入类型的用户数。<br>- “SUMMARY（汇总信息）”：查询所有类型的汇总会话上下文数。<br>- “ALIASAPN（别名APN）”：查询使用该别名APN激活的当前在线用户数。<br>默认值：SUMMARY<br>配置原则：无 |
| APN | APN | 可选必选说明：该参数在"QRY_CLASS"配置为"APN"时为条件必选参数。<br>参数含义：该参数用于指示需要查询会话上下文的APN。使用用户请求的APN对应的上报属性中“上报给话统的APN名”参数的取值，即在SET APNREPORTATTR命令中设置的该APN的PERFORMANCE的取值，指定使用用户请求的APN还是真实的APN进行统计。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| RAT | 无线接入类型 | 可选必选说明：该参数在"QRY_CLASS"配置为"RAT"时为条件必选参数。<br>参数含义：该参数用于指示指定需要查询会话上下文的无线接入类型。<br>数据来源：全网规划<br>取值范围：<br>- “UTRAN（UTRAN）”：通用陆地无线接入网。<br>- “GERAN（GERAN）”：GSM/EDGE无线接入网。<br>- “EUTRAN（EUTRAN）”：演进型通用陆地无线接入网。<br>- “NGRAN（NGRAN）”：5G无线接入网。<br>- “EUTRAN_NB_IOT（EUTRAN-NB-IOT）”：演进型通用陆地无线接入网-窄带物联网。<br>- “WLAN（WLAN）”：无线局域网<br>- “REDCAP（REDCAP）”：轻量能力。<br>默认值：无<br>配置原则：无 |
| POD_ID | POD名称 | 可选必选说明：该参数在"QRY_SCOPE"配置为"SPECIFIED_POD_INFO"时为条件必选参数。<br>参数含义：该参数用于指示需要查询会话上下文的POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| ALIASAPN | 别名APN | 可选必选说明：该参数在"QRY_CLASS"配置为"ALIASAPN"时为条件必选参数。<br>参数含义：该参数用于指示需要查询会话上下文的别名APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMUSERNUM]] · 会话管理的用户数（SMUSERNUM）

## 使用实例

当需要查询系统的用户数时，使用如下命令：

```
%%DSP SMUSERNUM: QRY_SCOPE=SUMMARY, QRY_CLASS=SUMMARY;%%
RETCODE = 0  操作成功

结果如下
--------
                           查询分类  =  汇总信息
                        GTPv1用户数  =  0
  本网签约并在本网接入的GTPv1用户数  =  0
异网漫入并在拜访地接入的GTPv1用户数  =  0
  漫出并在回归属地激活的GTPv1用户数  =  0
                        GTPv2用户数  =  0
  本网签约并在本网接入的GTPv2用户数  =  0
异网漫入并在拜访地接入的GTPv2用户数  =  0
  漫出并在回归属地激活的GTPv2用户数  =  0
                           SA用户数  =  0
     本网签约并在本网接入的SA用户数  =  0
   异网漫入并在拜访地接入的SA用户数  =  0
     漫出并在回归属地激活的SA用户数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SMUSERNUM.md`
