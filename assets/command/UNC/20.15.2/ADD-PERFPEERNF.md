---
id: UNC@20.15.2@MMLCommand@ADD PERFPEERNF
type: MMLCommand
name: ADD PERFPEERNF（增加NF局向性能统计对象）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PERFPEERNF
command_category: 配置类
applicable_nf:
- AMF
- SMF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# ADD PERFPEERNF（增加NF局向性能统计对象）

## 功能

**适用NF：AMF、SMF、SMSF、NCG**

该命令用于增加NF局向性能统计对象。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACETYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数表示对端局向服务化接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “N7（N7）”：N7<br>- “N8（N8）”：N8<br>- “N10（N10）”：N10<br>- “N11（N11）”：N11<br>- “N12（N12）”：N12<br>- “N15（N15）”：N15<br>- “N17（N17）”：N17<br>- “N20（N20）”：N20<br>- “N21（N21）”：N21<br>- “N40（N40）”：N40<br>- “Nocs（Nocs）”：Nocs<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例号 | 可选必选说明：必选参数<br>参数含义：该参数表示对端局向NF实例号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述对端局向信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFPEERNF]] · NF局向性能统计对象（PERFPEERNF）

## 使用实例

增加“接口类型”为“N8”，“NF实例号”为“AMF_INSTANCE_001”的NF局向性能统计对象：

```
ADD PERFPEERNF: INTERFACETYPE=N8, NFINSTANCEID="AMF_INSTANCE_001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加NF局向性能统计对象（ADD-PERFPEERNF）_09654373.md`
