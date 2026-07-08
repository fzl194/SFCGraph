---
id: UNC@20.15.2@MMLCommand@MOD IMSIAPNBINDUP
type: MMLCommand
name: MOD IMSIAPNBINDUP（修改APN下用户和UPF的绑定关系配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IMSIAPNBINDUP
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 用户APN绑定UPF
status: active
---

# MOD IMSIAPNBINDUP（修改APN下用户和UPF的绑定关系配置）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于修改APN下用户和UPF的绑定关系配置，支持修改APN下一个用户和UPF的绑定。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 使用该命令时，如果用户在SGW-C、PGW-C、I-SMF、N16aSMF、V-SMF、N16SMF形态下想要选中特定UPF，建议将参数PAUPNFINSTNAME和参数IMUPNFINSTNAME配置为同一个UPF。
- 2G/3G/4G场景不支持绑定辅锚点。
- 不支持智能分流专用会话。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 起始IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI号段的起始IMSI，当ENDIMSI没有值时，起始IMSI和终止IMSI相同。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。该参数每一位只能是数字0-9。<br>默认值：无<br>配置原则：无 |
| ACCESSTYPE | 接入类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的接入类型。<br>数据来源：本端规划<br>取值范围：<br>- GUL（2/3/4G接入）<br>- NG（5G接入）<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入APN需要在ADD APN命令中配置。<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。 |
| PAUPNFINSTNAME | 主锚点UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主锚点UPF实例名称。主锚点UPF为用户接入数据网络使用到的中心UPF锚点。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>主锚点UPF实例名称可通过LST PNFPROFILE查询。 |
| IMUPNFINSTNAME | N3/S1-U口UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N3/S1-U口UPF实例名称。N3/S1-U口UPF是用户与锚点UPF之间的I-UPF。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>若通过IMSIAPNBINDUP选择插入I-UPF，请针对该I-UPF增加服务区域信息（ADD PNFSMFSERAREA），服务区域需要绑定到TAI或LAI。 |
| AUXUPNFINSTNAME | 辅锚点UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定辅锚点UPF实例名称。辅锚点UPF为用户接入数据网络使用到的边缘UPF锚点。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>辅锚点UPF实例名称可通过LST PNFPROFILE查询。 |
| ULCLDEPLOYMODE | UL CL部署模式 | 可选必选说明：该参数在"ACCESSTYPE"配置为"NG"时为条件可选参数。<br>参数含义：该参数用于表示UL CL部署模式。<br>数据来源：本端规划<br>取值范围：<br>- “AUXSHUNTPREFER（优先使用辅锚点分流）”：优先辅锚点分流。如果没有与辅锚点合设的ULCL，则使用分离的ULCL。<br>- “PSASHUNTMUST（只使用主锚点分流）”：只使用主锚点分流。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIAPNBINDUP]] · APN下用户和UPF的绑定关系配置（IMSIAPNBINDUP）

## 使用实例

修改用户“11111111111111”，APN为“huawei.com”在5G的UP绑定关系：主锚点绑定UP1，辅锚点绑定UP2，N3锚点绑定UP3：

```
MOD IMSIAPNBINDUP: IMSI="11111111111111", ACCESSTYPE=NG, APN="huawei.com", PAUPNFINSTNAME="UP1", AUXUPNFINSTNAME="UP2", IMUPNFINSTNAME="UP3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IMSIAPNBINDUP.md`
