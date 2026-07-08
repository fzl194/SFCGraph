---
id: UNC@20.15.2@MMLCommand@ADD CANDIDATEAMF
type: MMLCommand
name: ADD CANDIDATEAMF（增加候选AMF）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CANDIDATEAMF
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- 候选AMF配置管理
status: active
---

# ADD CANDIDATEAMF（增加候选AMF）

## 功能

**适用NF：NSSF**

本命令用于配置候选AMF，建立AMF与AMFSET的关联关系。通过SET NSSFFUNCPARA命令将切片选择流程中给NF返回的信元配置为CandidateAmfList时，需要配置此命令。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NSSF上均需执行此命令，且配置参数一致。

- 最多可输入10000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于描述命令的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| AMFINSTANCEID | AMF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于描述全局唯一的AMF标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于描述移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：<br>该参数需要与ADD AMFSETID命令中MCC参数配置保持一致。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于描述移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：<br>该参数需要与ADD AMFSETID命令中MNC参数配置保持一致。 |
| REGIONID | 区域ID | 可选必选说明：必选参数<br>参数含义：该参数用于描述AMF区域ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。按照十六进制输入，输入时不带0x，不足两位时需手动从左边补0，取值范围00~ff。<br>默认值：无<br>配置原则：无 |
| AMFSETID | AMF集合标识 | 可选必选说明：必选参数<br>参数含义：该参数用于描述AMF集合的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。按照十六进制输入，输入时不带0x，不足三位时需手动从左边补0，取值范围000~3ff。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CANDIDATEAMF]] · 候选AMF（CANDIDATEAMF）

## 使用实例

假如运营商将切片选择流程中给NF返回的信元配置为CandidateAmfList，并希望增加一条INDEX为1、AMFINSTANCEID为"AMF01"、MCC为"460"、MNC为"03"、REGIONID为"01"、AMFSETID为"001"的记录， 建立AMF与AMFSET的关联关系，执行下列命令。

```
ADD CANDIDATEAMF: INDEX=1, AMFINSTANCEID="AMF01", MCC="460", MNC="03", REGIONID="01", AMFSETID="001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加候选AMF（ADD-CANDIDATEAMF）_18715631.md`
