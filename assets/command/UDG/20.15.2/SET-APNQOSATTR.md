---
id: UDG@20.15.2@MMLCommand@SET APNQOSATTR
type: MMLCommand
name: SET APNQOSATTR（设置ApnQosAttr配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNQOSATTR
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 流量管理
- APN的QoS属性配置
status: active
---

# SET APNQOSATTR（设置ApnQosAttr配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置指定APN的带宽控制功能开关。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 系统最多支持配置10000条ApnQosAttr。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CARSHAPESWUL | CARSHAPEUL | CARSHAPESWDL | CARSHAPEDL |
| --- | --- | --- | --- | --- |
| 初始值 | INHERIT | NULL | INHERIT | NULL |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| CARSHAPESWUL | 上行Qos开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置上行Qos使能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承全局。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：<br>- INHERIT：继承SET QOSSHAPE/QOSCAR配置的上行带宽QoS控制，SET QOSSHAPE配置优先级高于SET QOSCAR。先继承SET QOSSHAPE的配置，若无配置再继承SET QOSCAR。<br>- ENABLE：上行带宽使用QoS控制。<br>- DISABLE：上行带宽不使用QoS控制。 |
| CARSHAPEUL | 上行CAR/SHAPE开关 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CARSHAPESWUL”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于配置上行使能CAR或SHAPE。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CAR：使能CAR。<br>- SHAPE：使能SHAPE。<br>默认值：无<br>配置原则：无 |
| CARSHAPESWDL | 下行Qos开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置下行Qos使能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承全局。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：<br>- INHERIT：继承SET QOSSHAPE/QOSCAR配置的下行带宽QoS控制，SET QOSSHAPE配置优先级高于SET QOSCAR。先继承SET QOSSHAPE的配置，若无配置再继承SET QOSCAR。<br>- ENABLE：下行带宽使用QoS控制。<br>- DISABLE：下行带宽不使用QoS控制。 |
| CARSHAPEDL | 下行CAR/SHAPE开关 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CARSHAPESWDL”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于配置下行使能CAR或SHAPE。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CAR：使能CAR。<br>- SHAPE：使能SHAPE。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ApnQosAttr配置（APNQOSATTR）](configobject/UDG/20.15.2/APNQOSATTR.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00049]]

## 使用实例

配置APN为apn1.com，用户的下行CARSHAPE继承全局功能。上行CARSHAPE使能CAR功能：

```
SET APNQOSATTR: APN="apn1.com", CARSHAPESWUL=ENABLE, CARSHAPEUL=CAR, CARSHAPESWDL=INHERIT;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置ApnQosAttr配置（SET-APNQOSATTR）_82837665.md`
