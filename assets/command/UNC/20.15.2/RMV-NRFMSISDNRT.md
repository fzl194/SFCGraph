---
id: UNC@20.15.2@MMLCommand@RMV NRFMSISDNRT
type: MMLCommand
name: RMV NRFMSISDNRT（删除MSISDN号段路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFMSISDNRT
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
- MSISDN号段路由管理
status: active
---

# RMV NRFMSISDNRT（删除MSISDN号段路由）

## 功能

**适用NF：NRF**

该命令用于删除指定NF类型的MSISDN号段的路由。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持MSISDN号段路由寻址的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SMSF（SMSF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为PCF、UDM、CHF、CUSTOM_OCS、SMSF的路由转发功能，其他NF类型为预留功能。 |
| SEGSTART | 号段起始字符 | 可选必选说明：必选参数<br>参数含义：该参数用于表示MSISDN号段的起始号码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。十进制数字，号段的起始号码必须与结束号码长度保持一致，数值必须小于或等于结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符 | 可选必选说明：必选参数<br>参数含义：该参数用于表示MSISDN号段的结束号码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。十进制数字，号段的结束号码必须与起始号码长度保持一致，数值大于或等于起始号码的数值，且号段的结束号码不能以0开始。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFMSISDNRT]] · MSISDN号段路由（NRFMSISDNRT）

## 使用实例

运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最低层L-NRF。L-NRF归属于H-NRF，H-HRF归属于PLMN-NRF。 在H-NRF和PLMN-NRF上分别执行如下命令，删除NF类型为“PCF”，MSISDN号段为“125126~225226”的路由信息。

```
RMV NRFMSISDNRT: NFTYPE=PCF, SEGSTART="125126", SEGEND="225226";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFMSISDNRT.md`
