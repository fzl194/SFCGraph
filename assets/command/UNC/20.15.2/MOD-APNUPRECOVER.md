---
id: UNC@20.15.2@MMLCommand@MOD APNUPRECOVER
type: MMLCommand
name: MOD APNUPRECOVER（修改指定UPF的APN级别链路故障恢复处理）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD APNUPRECOVER（修改指定UPF的APN级别链路故障恢复处理）

## 功能

**适用NF：SMF**

该命令用于在UPF主备容灾场景下，修改指定UPF的APN级别链路故障恢复处理。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置APN名称。该参数已经通过ADD APN命令中的APN参数配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需在ADD APN中进行配置。 |
| MASTERUPFID | 主UPF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置主UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。不支持配置单空格。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| HANDLINGMODE | UP链路故障恢复处理模式 | 可选必选说明：必选参数<br>参数含义：该参数用于设置UP链路故障恢复处理模式。<br>数据来源：本端规划<br>取值范围：<br>- “NOHANDLING（无处理）”：选择“无处理”时，不检测主UPF链路故障后的恢复情况。<br>- “BACKMIGRATION（检测到故障恢复后回迁）”：选择“检测到故障恢复后回迁”时，若主UPF故障后恢复，将备UPF上的会话去活后重新在主UPF上激活。<br>默认值：无<br>配置原则：<br>1.当该参数配置为“检测到故障恢复后回迁”时，必须通过SET UPCSCANRATE命令设置“故障恢复回迁任务”扫描任务对应的扫描速率和扫描间隔。建议保持默认取值。 |
| BACKUPFID | 备UPF实例名称 | 可选必选说明：该参数在"HANDLINGMODE"配置为"BACKMIGRATION"时为条件必选参数。<br>参数含义：该参数用于设置备UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。不支持配置单空格。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNUPRECOVER]] · 指定UPF的APN级别链路故障恢复处理（APNUPRECOVER）

## 使用实例

修改主UPF为“upf1”，APN为“apn1”的链路故障恢复处理，将UP链路故障恢复处理模式设置为“无处理”：

```
MOD APNUPRECOVER: APN="apn1", MASTERUPFID="upf1", HANDLINGMODE=NOHANDLING;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改指定UPF的APN级别链路故障恢复处理（MOD-APNUPRECOVER）_75822984.md`
