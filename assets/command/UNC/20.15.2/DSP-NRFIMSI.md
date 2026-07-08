---
id: UNC@20.15.2@MMLCommand@DSP NRFIMSI
type: MMLCommand
name: DSP NRFIMSI（显示IMSI号段匹配信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFIMSI
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
- IMSI号段管理
status: active
---

# DSP NRFIMSI（显示IMSI号段匹配信息）

## 功能

**适用NF：NRF**

该命令用于查询与输入IMSI号段存在交集的配置号段及所属NF组标识。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示待查询的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>默认值：无<br>配置原则：无 |
| SEGQUERYSTART | 号段查询条件起始字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询NRF上IMSI号段配置的起始字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGQUERYEND | 号段查询条件结束字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询NRF上IMSI号段配置的结束字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能为以0开始。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFIMSI]] · IMSI号段匹配信息（NRFIMSI）

## 使用实例

查询起始字符串为"11111"，结束字符串为"44444"的IMSI号段匹配信息。

```
DSP NRFIMSI: NFTYPE=CHF, SEGQUERYSTART="11111", SEGQUERYEND="44444";
%%DSP NRFIMSI: NFTYPE=CHF, SEGQUERYSTART="11111", SEGQUERYEND="44444";%%
RETCODE = 0  执行成功

结果如下
------------------------
NF组标识             号段查询结果起始字符串  号段查询结果结束字符串   NF类型

chfpool-guangf-001  000000000000000     111111111111111      CHF
chfpool-guangf-001  111111111111111     222222222222222      CHF
(结果个数 = 2)
        
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NRFIMSI.md`
