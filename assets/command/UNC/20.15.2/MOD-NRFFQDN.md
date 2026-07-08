---
id: UNC@20.15.2@MMLCommand@MOD NRFFQDN
type: MMLCommand
name: MOD NRFFQDN（修改NRF的FQDN）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NRFFQDN
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NRF FQDN配置管理
status: active
---

# MOD NRFFQDN（修改NRF的FQDN）

## 功能

**适用NF：NSSF**

该命令用于修改NRF的FQDN。

## 注意事项

- 该命令执行后立即生效。

- 该命令会修改NRF的FQDN。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于描述命令的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于描述移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于描述移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| SST | 切片服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于描述切片服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示切片细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：可选参数<br>参数含义：该参数用于描述NRF的FQDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFFQDN]] · NRF的FQDN（NRFFQDN）

## 使用实例

假如运营商希望修改一条INDEX为1、MCC为"460"、MNC为"03"、SST为1、FQDN为"TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG"的记录，执行下列命令。

```
MOD NRFFQDN: INDEX=1, MCC="460", MNC="03", SST=1, FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NRF的FQDN（MOD-NRFFQDN）_09652626.md`
