---
id: UNC@20.15.2@MMLCommand@RMV NCGCHLMAP
type: MMLCommand
name: RMV NCGCHLMAP（删除话单通道一级目录类型映射表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NCGCHLMAP
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 话单通道一级目录类型映射表
status: active
---

# RMV NCGCHLMAP（删除话单通道一级目录类型映射表）

## 功能

**适用NF：NCG**

该命令用于删除特定字段前缀与话单通道一级目录类型的映射关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FIELDTYPE | 决定话单通道一级目录类型的字段 | 可选必选说明：必选参数<br>参数含义：该参数用于指定决定话单通道类型的字段。<br>数据来源：本端规划<br>取值范围：<br>- GPSI（GPSI）<br>默认值：无<br>配置原则：无 |
| PREFIX | 决定话单通道一级目录类型的字段前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定决定话单通道类型的字段前缀。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入由0~9的数字组成的字符串，字符串长度最大为15。<br>默认值：无<br>配置原则：无 |
| FIRSTDIRTYPE | 话单通道一级目录类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定话单一级目录类型。<br>数据来源：本端规划<br>取值范围：<br>- CBN2B（广电物联网场景下的分拣目录）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [话单通道一级目录类型映射表（NCGCHLMAP）](configobject/UNC/20.15.2/NCGCHLMAP.md)

## 使用实例

删除话单分拣字段为GPSI，字段前缀为"8610086"，话单通道一级目录类型为CBN2B的映射关系：

```
RMV NCGCHLMAP: FIELDTYPE=GPSI, PREFIX="8610640", FIRSTDIRTYPE=CBN2B;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除话单通道一级目录类型映射表（RMV-NCGCHLMAP）_25111036.md`
