---
id: UDG@20.15.2@MMLCommand@SET PKTFRAMEIDENT
type: MMLCommand
name: SET PKTFRAMEIDENT（设置帧包识别功能相关参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PKTFRAMEIDENT
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 帧包识别
- 帧包识别参数
status: active
---

# SET PKTFRAMEIDENT（设置帧包识别功能相关参数）

## 功能

**适用NF：UPF、PGW-U**

该命令用于设置帧包关系识别功能开关及相关参数。针对游戏、XR等通过帧传输且对时延敏感的业务，帧包识别功能可以识别报文的帧信息，并通过GTPU的标签将帧信息传递到无线侧，无线侧对同一帧数据的报文进行统一调度，避免部分报文调度不及时而产生的帧时延。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 使能帧包识别功能开关，并通过ADD RULE命令配置帧包识别类型的业务规则，帧包识别功能才能生效。
- 帧包识别功能开关和关键帧识别功能开关不能同时开启。
- 该命令设置的帧包识别功能仅在UPF与某些华为设备对接时支持，如要开启该功能需要联系华为技术支持评估。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | PKTFRMIDENTSW | LEARNINGTIME | KEYFRAMESW |
| --- | --- | --- | --- |
| 初始值 | DISABLE | 1 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PKTFRMIDENTSW | 帧包识别功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置帧包关系识别功能开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| LEARNINGTIME | 帧包关系学习时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置帧包识别功能对每条媒体流的初始学习时间。此段时间内仅做帧包关系学习，不进行帧包识别。初始学习时间结束后，开始进行帧包关系识别，将识别结果通过GTPU扩展头携带给无线侧。在识别帧包关系的同时，UDG会持续学习帧包关系并更新学习结果。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是秒。<br>默认值：无<br>配置原则：此值配置越小，学习时间越短，获取到学习结果越快。但学习时间太短可能导致学习结果不够准确。需要基于实际测试情况酌情调整此配置。 |
| KEYFRAMESW | 关键帧识别功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置关键帧识别功能开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PKTFRAMEIDENT]] · 帧包识别功能相关参数（PKTFRAMEIDENT）

## 使用实例

假设运营商需要开启帧包识别功能，帧包学习时间为3秒：

```
SET PKTFRAMEIDENT:  PKTFRMIDENTSW=ENABLE,  LEARNINGTIME=3;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置帧包识别功能相关参数（SET-PKTFRAMEIDENT）_29529276.md`
