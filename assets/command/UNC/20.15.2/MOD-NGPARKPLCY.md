---
id: UNC@20.15.2@MMLCommand@MOD NGPARKPLCY
type: MMLCommand
name: MOD NGPARKPLCY（修改园区策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGPARKPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 园区策略管理
status: active
---

# MOD NGPARKPLCY（修改园区策略）

## 功能

**适用NF：AMF**

该命令用于修改园区策略。

## 注意事项

- 该命令执行后立即生效。

- 不同园区策略中的区域编码不能重复，且不能包含重叠的跟踪区。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARKID | 园区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个园区。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| AREACODE | 区域编码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用园区策略的区域。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。该区域编码必须先通过ADD AREACODE进行添加，而区域内的跟踪区列表则通过ADD AREAMEM进行添加。<br>默认值：无<br>配置原则：无 |
| DNNGRPID | DNN群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用园区策略的DNN群组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~32。DNN群组标识通过ADD DNNGRP进行配置。<br>默认值：无<br>配置原则：无 |
| INERTIA | 惯性运行开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制指定园区是否支持惯性运行功能。默认值为关闭。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无<br>配置原则：<br>当运营商希望通AMF与NG-RAN之间的N2接口故障后，保持终端的连接状态，保证数据传输正常，需要将本参数设置为“ON”。 |

## 操作的配置对象

- [园区策略（NGPARKPLCY）](configobject/UNC/20.15.2/NGPARKPLCY.md)

## 使用实例

将园区标识为“park”，区域编码为“huawei”，且DNN群组标识为“BIG_GROUP”的惯性运行功能关闭，执行如下命令：

```
MOD NGPARKPLCY: PARKID="park", AREACODE="huawei", DNNGRPID="BIG_GROUP", INERTIA=OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改园区策略（MOD-NGPARKPLCY）_06399921.md`
