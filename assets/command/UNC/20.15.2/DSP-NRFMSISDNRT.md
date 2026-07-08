---
id: UNC@20.15.2@MMLCommand@DSP NRFMSISDNRT
type: MMLCommand
name: DSP NRFMSISDNRT（显示MSISDN路由匹配信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFMSISDNRT
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
- MSISDN号段路由管理
status: active
---

# DSP NRFMSISDNRT（显示MSISDN路由匹配信息）

## 功能

**适用NF：NRF**

该命令用于查询与输入MSISDN号段存在交集的配置号段及所属NRF实例组信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示待查询支持MSISDN号段路由的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SMSF（SMSF）<br>默认值：无<br>配置原则：无 |
| SEGQUERYSTART | 号段路由查询条件起始字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询NRF上MSISDN号段路由配置的起始字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段的起始号码必须与结束号码长度保持一致，数值必须小于或等于结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGQUERYEND | 号段查询条件结束字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询NRF上MSISDN号段路由配置的结束字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段的结束号码必须与起始号码长度保持一致，数值大于或等于起始号码的数值，且号段的结束号码不能以0开始。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFMSISDNRT]] · MSISDN号段路由（NRFMSISDNRT）

## 使用实例

查询起始字符串为"00000"，结束字符串为"22222"的MSISDN号段路由匹配信息。

```
DSP NRFMSISDNRT: NFTYPE=UDM, SEGQUERYSTART="00000", SEGQUERYEND="22222";
%%DSP NRFMSISDNRT: NFTYPE=UDM, SEGQUERYSTART="00000", SEGQUERYEND="22222";%%
RETCODE = 0  执行成功

结果如下
------------------------
NF类型  归属NRF实例组名称    号段路由查询结果起始字符串    号段路由查询结果结束字符串    Pod名称

UDM     nrfpool-guangf-001   000000000000000               111111111111111               nrf-pod-98945dc9d-hsc9f
UDM     nrfpool-guangf-002   111111111111111               222222222222222               nrf-pod-98945dc9d-hsc9f
(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示MSISDN路由匹配信息（DSP-NRFMSISDNRT）_45444647.md`
