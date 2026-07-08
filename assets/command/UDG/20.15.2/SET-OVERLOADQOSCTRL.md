---
id: UDG@20.15.2@MMLCommand@SET OVERLOADQOSCTRL
type: MMLCommand
name: SET OVERLOADQOSCTRL（设置过载限速参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: OVERLOADQOSCTRL
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- 过载限速
- 过载限速参数
status: active
---

# SET OVERLOADQOSCTRL（设置过载限速参数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](设置过载限速参数（SET OVERLOADQOSCTRL）_00602758.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，参数设置不合理可能触发非预期的过载限速，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置过载限速参数。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH | CPUTHRESH | CPURECVTHRESH | MBRUL | MBRDL | USERSAMPMODE | OVERLOADPERIOD | RECVPERIOD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | 80 | 75 | 1000 | 1000 | SAMPLING_AUTO | 12 | 36 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 过载限速开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定过载限速功能的开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| CPUTHRESH | CPU过载阈值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定CELL_SSG进程CPU过载阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为50～90。<br>默认值：80<br>配置原则：无 |
| CPURECVTHRESH | CPU恢复阈值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定CELL_SSG进程CPU过载恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为50～90。<br>默认值：75<br>配置原则：该配置参数CPURECVTHRESH的取值不能大于配置参数CPUTHRESH的取值。 |
| MBRUL | 上行最大带宽(千比特/秒) | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定会话过载限速的上行最大带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为100～150000，单位是千比特每秒。<br>默认值：1000<br>配置原则：无 |
| MBRDL | 下行最大带宽(千比特/秒) | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定会话过载限速的下行最大带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为100～150000，单位是千比特每秒。<br>默认值：1000<br>配置原则：无 |
| USERSAMPMODE | 用户抽样方式 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定用户抽样方式。<br>数据来源：本端规划<br>取值范围：<br>- SAMPLING_AUTO：系统根据过载时平均CPU自动计算需要过载限速的在线会话比例。<br>- SAMPLING_MANUAL_10：系统过载时抽取10%在线会话进行过载限速控制。<br>- SAMPLING_MANUAL_20：系统过载时抽取20%在线会话进行过载限速控制。<br>- SAMPLING_MANUAL_30：系统过载时抽取30%在线会话进行过载限速控制。<br>- SAMPLING_MANUAL_40：系统过载时抽取40%在线会话进行过载限速控制。<br>- SAMPLING_MANUAL_50：系统过载时抽取50%在线会话进行过载限速控制。<br>- SAMPLING_MANUAL_60：系统过载时抽取60%在线会话进行过载限速控制。<br>- SAMPLING_MANUAL_70：系统过载时抽取70%在线会话进行过载限速控制。<br>- SAMPLING_MANUAL_80：系统过载时抽取80%在线会话进行过载限速控制。<br>- SAMPLING_MANUAL_90：系统过载时抽取90%在线会话进行过载限速控制。<br>- SAMPLING_MANUAL_100：系统过载时抽取100%在线会话进行过载限速控制。<br>默认值：SAMPLING_AUTO<br>配置原则：<br>- 该参数配置为SAMPLING_AUTO时，业务节点进入过载限速状态时，会根据平均CPU计算抽样比例，选择对应比例的在线会话进行过载限速控制。<br>- 该参数设置为SAMPLING_MANUAL_10~SAMPLING_MANUAL_100时，业务节点进入过载限速状态时，会根据配置选择对应比例的在线会话进行过载限速控制。 |
| OVERLOADPERIOD | 过载限速判定周期数 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定过载限速判定周期数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～60，每周期时长5秒。<br>默认值：12<br>配置原则：<br>- 过载限速判定周期数时长内平均CPU、最后一个周期的CPU均大于等于CPU过载阈值，系统判定为业务节点过载，进行过载限速处理。<br>- 建议该参数保持默认值。 |
| RECVPERIOD | 过载限速恢复判定周期数 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定过载限速恢复判定周期数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～255，每周期时长5秒。<br>默认值：36<br>配置原则：<br>- 过载限速恢复判定周期数时长内平均CPU、最后一个周期的CPU均小于CPU过载恢复阈值，系统判定为业务节点过载恢复，解除过载限速处理。<br>- 建议该参数保持默认值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OVERLOADQOSCTRL]] · 过载限速参数（OVERLOADQOSCTRL）

## 使用实例

设置使能过载限速功能，执行如下命令：

```
SET OVERLOADQOSCTRL: SWITCH=ENABLE, CPUTHRESH=80, CPURECVTHRESH=75, MBRUL=1000, MBRDL=1000, USERSAMPMODE=SAMPLING_AUTO, OVERLOADPERIOD=12, RECVPERIOD=36;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-OVERLOADQOSCTRL.md`
