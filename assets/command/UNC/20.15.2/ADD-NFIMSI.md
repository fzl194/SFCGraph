---
id: UNC@20.15.2@MMLCommand@ADD NFIMSI
type: MMLCommand
name: ADD NFIMSI（增加IMSI号段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NFIMSI
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
- IMSI号段管理
status: active
---

# ADD NFIMSI（增加IMSI号段）

## 功能

**适用NF：NRF**

如果运营商希望在NRF上新增NF的IMSI的号段信息，配置此命令。

## 注意事项

- 立即生效

- 每个NF类型最多可输入600000条记录。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。
- NF的号段信息可以通过注册携带，也可以通过MML命令在NRF上配置，建议采用其中一种方式进行控制。如果NF注册已携带，且NRF上也进行了配置，NRF都会判断NF号段生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持IMSI号段的NF组标识，可以通过LST NFGROUP进行查询，支持IMSI号段配置的NF类型仅包含AUSF、PCF、UDM、 UDR、CHF、CUSTOM_OCS。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |
| SEGSTART | 号段起始字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IMSI号段配置的号段起始字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IMSI号段配置的号段结束字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能为以0开始。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFIMSI]] · IMSI号段（NFIMSI）

## 使用实例

运营商已经规划NF组标识为nfgroup01的号段类NF组，对此NF组配置支持的IMSI号段区间为12345678904到12345678905，12345678914到12345678916。

```
ADD NFIMSI: NFGROUPID="nfgroup01", SEGSTART="12345678904", SEGEND="12345678905";
ADD NFIMSI: NFGROUPID="nfgroup01", SEGSTART="12345678914", SEGEND="12345678916";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IMSI号段（ADD-NFIMSI）_09653306.md`
