---
id: UNC@20.15.2@MMLCommand@RMV PERFPEERNF
type: MMLCommand
name: RMV PERFPEERNF（删除NF局向性能统计对象）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV PERFPEERNF（删除NF局向性能统计对象）

## 功能

**适用NF：AMF、SMF、SMSF、NCG**

该命令用于删除NF局向性能统计对象。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例号 | 可选必选说明：必选参数<br>参数含义：该参数表示对端局向NF实例号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFPEERNF]] · NF局向性能统计对象（PERFPEERNF）

## 使用实例

删除“NF实例号”为“AMF_INSTANCE_001”的NF局向性能统计对象：

```
RMV PERFPEERNF: NFINSTANCEID="AMF_INSTANCE_001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFPEERNF.md`
