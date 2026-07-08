---
id: UNC@20.15.2@MMLCommand@DSP NRFMSISDNSTC
type: MMLCommand
name: DSP NRFMSISDNSTC（显示MSISDN号段统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFMSISDNSTC
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- MSISDN号段管理
status: active
---

# DSP NRFMSISDNSTC（显示MSISDN号段统计信息）

## 功能

**适用NF：NRF**

该命令用于显示MSISDN号段统计信息。若查询NF类型对应号段总数，请选择查询类型为“TOTALNUM”；若查询“NF组标识”细分的号段数统计，请选择查询类型为“NFGROUPNUM”。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询MSISDN号段统计信息的查询条件类型。<br>数据来源：本端规划<br>取值范围：<br>- TOTALNUM（按NFType显示号段总数）<br>- NFGROUPNUM（按NF组标识显示号段数）<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFGROUPNUM"时为条件必选参数。该参数在"QUERYTYPE"配置为"TOTALNUM"时为条件可选参数。<br>参数含义：该参数用于表示待查询MSISDN号段统计信息的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>默认值：无<br>配置原则：<br>不输入代表查询所有的NF类型对应的号段数，否则显示指定NFType对应的号段数。 |
| NFGROUPID | NF组标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFGROUPNUM"时为条件可选参数。<br>参数含义：该参数用于表示MSISDN号段配置的NF组标识，可以通过LST NFGROUP进行查询，支持MSISDN号段配置的NF类型仅包含PCF、UDM、UDR、CHF、CUSTOM_OCS。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：<br>不输入代表显示对应NF类型下所有NF组标识的号段数；否则显示指定NF组标识的号段数。 |

## 操作的配置对象

- [MSISDN号段统计信息（NRFMSISDNSTC）](configobject/UNC/20.15.2/NRFMSISDNSTC.md)

## 使用实例

查询类型为TOTALNUM，查新MSISDN号段的统计信息。

```
DSP NRFMSISDNSTC: QUERYTYPE=TOTALNUM;
%%DSP NRFMSISDNSTC: QUERYTYPE=TOTALNUM;%%
RETCODE = 0  执行成功

结果如下
------------------------
NF类型      号段数

UDM         2
UDR         1
PCF         1
CHF         2
CUSTOM_OCS  1
(结果个数 = 5)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示MSISDN号段统计信息（DSP-NRFMSISDNSTC）_98764636.md`
