---
id: UNC@20.15.2@MMLCommand@DSP NRFIMSIRTSTC
type: MMLCommand
name: DSP NRFIMSIRTSTC（显示IMSI路由统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFIMSIRTSTC
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- IMSI号段路由管理
status: active
---

# DSP NRFIMSIRTSTC（显示IMSI路由统计信息）

## 功能

**适用NF：NRF**

该命令用于显示IMSI路由统计信息。若查询某NF类型对应号段总数，请选择查询类型为“TOTALNUM”；若查询某NF类型按“NF组标识”细分的号段数统计，请选择查询类型为“NFGROUPNUM”。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询IMSI号段路由统计信息的查询条件类型。<br>数据来源：本端规划<br>取值范围：<br>- TOTALNUM（按NFType显示号段总数）<br>- NFGROUPNUM（按NF组标识显示号段数）<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFGROUPNUM"时为条件必选参数。该参数在"QUERYTYPE"配置为"TOTALNUM"时为条件可选参数。<br>参数含义：该参数用于表示待查询IMSI号段路由统计信息的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SMSF（SMSF）<br>默认值：无<br>配置原则：<br>不输入代表查询所有的NF类型对应的号段数，否则显示指定NFType对应的号段数。 |
| NEXTNRFGRPNAME | 归属NRF实例组名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFGROUPNUM"时为条件可选参数。<br>参数含义：该参数用于表示当前NRF基于IMSI号段寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFIMSIRTSTC]] · IMSI路由统计信息（NRFIMSIRTSTC）

## 使用实例

查询类型为TOTALNUM，查新IMSI号段路由的统计信息。

```
DSP NRFIMSIRTSTC: QUERYTYPE=TOTALNUM;
%%DSP NRFIMSIRTSTC: QUERYTYPE=TOTALNUM;%%
RETCODE = 0  执行成功

结果如下
------------------------
NF类型     号段数

UDM         2
UDR         0
AUSF        0
PCF         0
CHF         0
CUSTOM_OCS  0
SMSF        0
(结果个数 = 7)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NRFIMSIRTSTC.md`
