---
id: UNC@20.15.2@MMLCommand@RMV APNUPRECOVER
type: MMLCommand
name: RMV APNUPRECOVER（删除指定UPF的APN级别链路故障恢复处理）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNUPRECOVER
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP故障管理
- N4接口故障恢复处理
status: active
---

# RMV APNUPRECOVER（删除指定UPF的APN级别链路故障恢复处理）

## 功能

**适用NF：SMF**

该命令用于在UPF主备容灾场景下，删除指定UPF的APN级别链路故障恢复处理。

## 注意事项

- 该命令执行后立即生效。

- 若删除前“UP链路故障恢复处理模式”配置为“无处理”，删除后功能无影响；
- 若删除前“UP链路故障恢复处理模式”配置为“检测到故障恢复后回迁”，删除后不检测主UPF链路故障后恢复状态。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置APN名称。该参数已经通过ADD APN命令中的APN参数配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需在ADD APN中进行配置。 |
| MASTERUPFID | 主UPF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置主UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。不支持配置单空格。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNUPRECOVER]] · 指定UPF的APN级别链路故障恢复处理（APNUPRECOVER）

## 使用实例

删除主UPF为“upf1”，APN为“apn1”的链路故障恢复处理：

```
RMV APNUPRECOVER: APN="apn1", MASTERUPFID="upf1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除指定UPF的APN级别链路故障恢复处理（RMV-APNUPRECOVER）_75982864.md`
