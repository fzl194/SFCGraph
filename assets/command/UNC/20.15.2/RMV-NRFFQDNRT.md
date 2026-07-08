---
id: UNC@20.15.2@MMLCommand@RMV NRFFQDNRT
type: MMLCommand
name: RMV NRFFQDNRT（删除FQDN路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFFQDNRT
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- FQDN路由管理
status: active
---

# RMV NRFFQDNRT（删除FQDN路由）

## 功能

**适用NF：NRF**

该命令用于删除FQDN路由信息。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持FQDN路由寻址的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| FQDNSUFFIX | 域名后缀 | 可选必选说明：必选参数<br>参数含义：该参数用于表示域名的最长匹配后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，FQDN后缀不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于域名的最长后缀匹配寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFFQDNRT]] · FQDN路由（NRFFQDNRT）

## 使用实例

运营商网络为三层网络，最高层PLMN-NRF，中间层H-NRF，最底层L-NRF。L-NRF1归属于H-NRF1，H-NRF1归属于PLMN-NRF。在H-NRF1和PLMN-NRF上分别执行如下命令，删除NF类型为PCF，域名后缀为"huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org"的路由信息。

```
RMV NRFFQDNRT: NFTYPE=SMF, FQDNSUFFIX="huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org", NEXTNRFGRPNAME="L-NRF1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFFQDNRT.md`
