---
id: UNC@20.15.2@MMLCommand@ADD SEGBLACKLIST
type: MMLCommand
name: ADD SEGBLACKLIST（增加导入号段黑名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SEGBLACKLIST
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
- 号段导入管理
status: active
---

# ADD SEGBLACKLIST（增加导入号段黑名单）

## 功能

**适用NF：NRF**

该命令已废弃。

该命令用于新增导入号段黑名单，命令中配置的号段数据将在NRF导入号段数据中失效。例如，NRF通过导入号段方式定义UDM支持的IMSI号段的范围为123456~234567，345678~456789，通过此命令配置UDM的IMSI黑名单范围为123456~234567，则UDM通过导入号段方式实际支持的IMSI号段范围123456~234567失效，345678~456789仍然有效。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入10240条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGTYPE | 号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段黑名单作用的号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>- IMSIRT（IMSIRT）<br>- MSISDNRT（MSISDNRT）<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段黑名单作用的NF类型，即哪些NF类型支持号段文件中给出的号段信息。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>默认值：无<br>配置原则：<br>该参数在“SEGTYPE”配置为“IMSI、IMSIRT”时，取值范围为上述所有NF类型，该参数在“SEGTYPE”配置为“MSISDN、MSISDNRT”时，取值范围为PCF、UDM、UDR、CHF、CUSTOM_OCS。 |
| SEGSTART | 号段起始字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段黑名单起始字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。十进制数字，号段的起始号码必须与结束号码长度保持一致，数值必须小于或等于结束号码的数值。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段黑名单结束字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。十进制数字，号段的结束号码必须与起始号码长度保持一致，数值大于或等于起始号码的数值。<br>默认值：无<br>配置原则：无 |
| GROUPID | 组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示待配置IMSI/MSISDN号段黑名单的NF组标识或配置IMSIRT/MSISDNRT路由转发号段黑名单的下一跳NRF组标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9），中划线（-）组成。当配置IMSI/MSISDN号段黑名单的NF组标识时，不区分大小写；当配置IMSIRT/MSISDNRT路由转发号段黑名单的下一跳NRF组标识时，则区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SEGBLACKLIST]] · 导入号段黑名单（SEGBLACKLIST）

## 使用实例

NRF通过导入号段方式定义NF组标识为udm的UDM类型所支持的IMSI号段的范围为123456~234567，345678~456789，通过此命令配置UDM的IMSI黑名单范围为123456~234567：

```
ADD SEGBLACKLIST: SEGTYPE=IMSI, NFTYPE=UDM, SEGSTART="123456", SEGEND="234567", GROUPID="udm";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SEGBLACKLIST.md`
