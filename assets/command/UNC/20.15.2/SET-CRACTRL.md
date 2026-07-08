---
id: UNC@20.15.2@MMLCommand@SET CRACTRL
type: MMLCommand
name: SET CRACTRL（设置CRA控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CRACTRL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- CRA控制
status: active
---

# SET CRACTRL（设置CRA控制参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置实时位置上报的开关及本地实时位置上报的Trigger。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CRARULE | TAI | ECGI |
| --- | --- | --- | --- |
| 初始值 | PCRF | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CRARULE | CRA控制 | 可选必选说明：可选参数<br>参数含义：该参数用于配置Gx接口实时位置上报指示的来源。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- PCRF：PCRF。<br>- LOCAL：LOCAL。<br>- COMBINE：COMBINE。<br>默认值：无<br>配置原则：无 |
| TAI | TAI | 可选必选说明：条件可选参数<br>前提条件：该参数在“CRARULE”配置为“LOCAL” 或 “COMBINE”时为可选参数。<br>参数含义：该参数用于配置Change Reporting Action信元中是否开启TAI指示。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| ECGI | ECGI | 可选必选说明：条件可选参数<br>前提条件：该参数在“CRARULE”配置为“LOCAL” 或 “COMBINE”时为可选参数。<br>参数含义：该参数用于配置Change Reporting Action信元中是否开启ECGI指示。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CRACTRL]] · CRA控制参数（CRACTRL）

## 使用实例

如果希望Gx接口实时位置上报功能以本地配置为准，且本地配置TAI和ECGI都使能，则可以进行如下设置：

```
SET CRACtrl: CRARULE=LOCAL,TAI=ENABLE,ECGI=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CRACTRL.md`
