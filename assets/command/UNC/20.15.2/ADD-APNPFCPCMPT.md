---
id: UNC@20.15.2@MMLCommand@ADD APNPFCPCMPT
type: MMLCommand
name: ADD APNPFCPCMPT（增加指定APN的PFCP私有信元携带配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNPFCPCMPT
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
- 接口管理
- PFCP接口管理
- 基于APN的PFCP私有信元管理
status: active
---

# ADD APNPFCPCMPT（增加指定APN的PFCP私有信元携带配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于增加指定APN的PFCP私有信元携带配置，控制UNC发送的PFCP消息中，是否允许携带指定特性相关的私有信元。

## 注意事项

- 该命令执行后立即生效。

- 如果需要给SGW-U创建承载级别的CreateQer，需要同时开启CREATEQERSW和PFCPQCISW开关。
- 当PFCPQCISW被置为ENABLE时，需确认DWORD1067 BIT23已开启。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”；该参数取值应与ADD APN命令中参数“APN”保持一致，使用该前需通过ADD APN添加一组记录。 |
| CREATEQERSW | SMF给SGW-U携带承载级CreateQer信元控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF是否给SGW-U的消息中携带承载级CreateQer。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |
| PFCPQCISW | SMF给UPF携带Qci信元控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF是否给UPF的消息携带Qci信元。<br>数据来源：全网规划<br>取值范围：<br>- INHERIT（继承全局）<br>- ENABLE（使能）<br>- DISABLE（不使能）<br>默认值：INHERIT<br>配置原则：<br>业务处理过程中优先应用APN下的设置，只有当PFCPQCISW下配置为INHERIT时才应用SET PFCPPVTEXT配置中FEATURE=QCI，SWITCH控制。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNPFCPCMPT]] · 指定APN的PFCP私有信元携带配置（APNPFCPCMPT）

## 使用实例

增加指定APN的PFCP私有信元携带配置。APN名称为huawei.com，SMF给SGW-U携带承载级CreateQer信元控制开关为使能，SMF给UPF携带Qci信元控制开关为继承：

```
ADD APNPFCPCMPT:APN="huawei.com", CREATEQERSW=ENABLE,PFCPQCISW=INHERIT; 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNPFCPCMPT.md`
