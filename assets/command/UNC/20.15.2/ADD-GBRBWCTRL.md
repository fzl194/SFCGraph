---
id: UNC@20.15.2@MMLCommand@ADD GBRBWCTRL
type: MMLCommand
name: ADD GBRBWCTRL（增加GBR承载带宽速率控制配置）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD GBRBWCTRL（增加GBR承载带宽速率控制配置）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用来增加GBR承载带宽速率控制配置，适用于WSFD-105007 5G QoS到4G QoS灵活映射特性。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS控制的类型。<br>数据来源：全网规划<br>取值范围：<br>- APN_LEVEL（APN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：该参数在"CTRLTYPE"配置为"APN_LEVEL"时为条件必选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| MBRUL | 上行最大速率(千比特/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的上行最大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |
| MBRDL | 下行最大速率(千比特/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的下行最大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |
| GBRUL | 上行保证速率(千比特/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的上行保证大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |
| GBRDL | 下行保证速率(千比特/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成GBR承载带宽控制的下行保证大速率(千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20000000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBRBWCTRL]] · GBR承载带宽速率控制配置（GBRBWCTRL）

## 使用实例

如果想添加一条GBRBWCTRL配置，执行如下命令：

```
ADD GBRBWCTRL:CTRLTYPE=APN_LEVEL,APN="huawei.com",MBRUL=1000,MBRDL=1000,GBRUL=1000,GBRDL=1000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GBRBWCTRL.md`
