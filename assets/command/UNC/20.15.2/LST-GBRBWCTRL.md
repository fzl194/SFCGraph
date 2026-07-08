---
id: UNC@20.15.2@MMLCommand@LST GBRBWCTRL
type: MMLCommand
name: LST GBRBWCTRL（查询GBR承载带宽速率控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBRBWCTRL
command_category: 查询类
applicable_nf:
- GGSN
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- QoS映射
- GBR带宽控制
status: active
---

# LST GBRBWCTRL（查询GBR承载带宽速率控制配置）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用来查询GBR承载带宽速率控制配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLTYPE | 控制类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS控制的类型。<br>数据来源：全网规划<br>取值范围：<br>- APN_LEVEL（APN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：该参数在"CTRLTYPE"配置为"APN_LEVEL"时为条件可选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| MBRUL | 上行最大速率(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的上行最大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |
| MBRDL | 下行最大速率(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的下行最大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |
| GBRUL | 上行保证速率(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的上行保证大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |
| GBRDL | 下行保证速率(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的下行保证大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GBRBWCTRL]] · GBR承载带宽速率控制配置（GBRBWCTRL）

## 使用实例

查询所有GBRBWCTRL配置：

```
LST GBRBWCTRL:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GBRBWCTRL.md`
