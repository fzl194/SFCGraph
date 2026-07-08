---
id: UNC@20.15.2@MMLCommand@RMV APNCHGMODE
type: MMLCommand
name: RMV APNCHGMODE（删除基于APN的计费接口选择方式）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNCHGMODE
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- APN计费模式
status: active
---

# RMV APNCHGMODE（删除基于APN的计费接口选择方式）

## 功能

![](删除基于APN的计费接口选择方式（RMV APNCHGMODE）_96242742.assets/notice_3.0-zh-cn_2.png)

删除基于APN的计费接口选择方式不当可能选错计费策略接口，相应计费策略接口未配置时会导致计费相关流程失败，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除基于APN的计费接口选择功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |
| TMACCTYPE | 指定终端和接入类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定终端和接入类型。<br>数据来源：本端规划<br>取值范围：<br>- “UE5G_RAT4G（5G终端4G接入）”：5G终端4G接入是指在4G接入的PDN激活流程中，激活消息的PCO中携带5G PDU session ID信息。<br>- “UE5G_RAT5G（5G终端5G接入）”：5G终端5G接入是指在5G接入的PDU激活流程。<br>- “UENON5G_RAT4G（非5G终端4G接入）”：非5G终端4G接入是指在4G接入的PDN激活流程。<br>- “RAT2G（2G接入）”：2G接入是指在2G接入的一次PDP激活流程。<br>- “RATNBIOT（NB-IoT接入）”：NB-IoT接入是指NB-IoT用户接入。<br>- “NON_3GPP（非3GPP接入）”：非3GPP接入是指用户从非3GPP网络接入。<br>- “RATLTEM（LTE-M接入）”：LTE-M接入是指LTE-M用户接入。<br>- “RAT3G（3G接入）”：3G接入是指在3G接入的PDP一次激活流程。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNCHGMODE]] · 基于APN的计费接口选择方式（APNCHGMODE）

## 使用实例

删除基于APN的计费接口选择方式，“APN名称”为“huawei.com”，指定终端和接入类型为5G终端4G接入。

```
RMV APNCHGMODE: APN="huawei.com", TMACCTYPE=UE5G_RAT4G;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNCHGMODE.md`
