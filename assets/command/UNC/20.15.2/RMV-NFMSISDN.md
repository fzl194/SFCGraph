---
id: UNC@20.15.2@MMLCommand@RMV NFMSISDN
type: MMLCommand
name: RMV NFMSISDN（删除MSISDN号段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NFMSISDN
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- MSISDN号段管理
status: active
---

# RMV NFMSISDN（删除MSISDN号段）

## 功能

**适用NF：NRF**

如果运营商希望在NRF上删除NF的MSISDN的号段信息，配置此命令。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示MSISDN号段配置的NF组标识，可以通过LST NFGROUP进行查询，支持MSISDN号段配置的NF类型仅包含UDM、UDR、CHF、PCF、CUSTOM_OCS。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示MSISDN号段的起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。十进制数字，号段的起始号码必须与结束号码长度保持一致，数值必须小于或等于结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示MSISDN号段的结束号码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。十进制数字，号段的结束号码必须与起始号码长度保持一致，数值大于或等于起始号码的数值，且号段的结束号码不能以0开始。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFMSISDN]] · MSISDN号段（NFMSISDN）

## 使用实例

删除NF标识为nfgroupid-city1的MSISDN号段信息，号段范围为11111到99999。

```
RMV NFMSISDN: NFGROUPID="nfgroupid-city1", SEGSTART="11111", SEGEND="99999";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NFMSISDN.md`
