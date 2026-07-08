---
id: UNC@20.15.2@MMLCommand@ADD NFGROUP
type: MMLCommand
name: ADD NFGROUP（增加NF组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NFGROUP
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF实例组信息管理
status: active
---

# ADD NFGROUP（增加NF组）

## 功能

**适用NF：NRF**

该命令用于在NRF上新增NF实例组信息。

NF组是由一个或者多个NF实例组成的容灾/负荷分担的集群，组内NF实例对外提供相同的业务功能。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF实例组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示在NRF上配置的NF实例组的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9），中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示在NRF上配置的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| GROUPDESC | NF实例组描述 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在NRF上配置的NF实例组的概要描述。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFGROUP]] · NF组（NFGROUP）

## 使用实例

在NRF上新增NF标识为nfgroup001，NF类型为CHF，组描述为nfdescription001的实例组：

```
ADD NFGROUP: NFGROUPID="nfgroup001", NFTYPE=CHF, GROUPDESC="nfdescription001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NFGROUP.md`
