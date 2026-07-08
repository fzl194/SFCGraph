---
id: UNC@20.15.2@MMLCommand@MOD GBRBWCTRL
type: MMLCommand
name: MOD GBRBWCTRL（修改GBR承载带宽速率控制配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GBRBWCTRL
command_category: 配置类
applicable_nf:
- GGSN
- PGW-C
- SMF
effect_mode: 对新用户生效
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

# MOD GBRBWCTRL（修改GBR承载带宽速率控制配置）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用来修改GBR承载带宽速率控制配置。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS控制的类型。<br>数据来源：全网规划<br>取值范围：<br>- APN_LEVEL（APN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：该参数在"CTRLTYPE"配置为"APN_LEVEL"时为条件必选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| MBRUL | 上行最大速率(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的上行最大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |
| MBRDL | 下行最大速率(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的下行最大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |
| GBRUL | 上行保证速率(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的上行保证大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |
| GBRDL | 下行保证速率(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的下行保证大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [GBR承载带宽速率控制配置（GBRBWCTRL）](configobject/UNC/20.15.2/GBRBWCTRL.md)

## 使用实例

如果想修改一条GBRBWCTRL，执行如下命令：

```
MOD GBRBWCTRL:CTRLTYPE=APN_LEVEL,APN="huawei.com",MBRUL=2000,MBRDL=2000,GBRUL=2000,GBRDL=2000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GBR承载带宽速率控制配置（MOD-GBRBWCTRL）_40119813.md`
