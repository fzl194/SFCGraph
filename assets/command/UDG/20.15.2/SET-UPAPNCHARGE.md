---
id: UDG@20.15.2@MMLCommand@SET UPAPNCHARGE
type: MMLCommand
name: SET UPAPNCHARGE（设置APN的计费配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPAPNCHARGE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
max_records: 20000
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- APN计费控制
status: active
---

# SET UPAPNCHARGE（设置APN的计费配置）

## 功能

**适用NF：PGW-U、UPF**

![](设置APN的计费配置（SET UPAPNCHARGE）_29940708.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改默认配额使能开关会影响用户业务访问时延。

该命令用于设置指定APN的用户在进行在线计费业务时，是否使用默认配额。主要应用场景是，当支持使用默认配额时，新业务请求的首个报文，在向SMF申请配额时，UPF不缓存这个报文，允许其通过；非新业务场景申请配额期间的报文，UPF不丢包，允许其通过。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为20000。
- 修改默认配额使能开关会影响用户业务访问时延，举例：用户配额耗尽申请配额期间如果默认配额使能开关关闭用户的业务报文会阻塞，导致业务访问时延变大。
- 功能开启依赖配置DefaultQuota的配额，应提前使用命令ADD/MOD URR和SET SRVCOMMONPARA设置默认配额的大小。
- 默认配额需要合理规划，配置过小时，配额耗尽后会导致业务阻塞，导致业务访问时延变大。配置过大时，当配额申请失败会导致申请配额期间的流量免费通过，造成运营商计费损失。
- DefaultQuota功能开启后，允许用户业务报文在申请配额期间先行通过，如果后续未申请到配额或配额下发过小，会导致使用量上报超过配额。
- 功能依赖APN配置，应提前使用命令ADD APN设置相应APN。
- 最大规格与ADD APN相同，每增加一个APN会自动生成一条配置，开关默认取值为INHERIT，APN删除时会自动删除对应APN的UPAPNCHARGE配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| DFTQTSWITCH | 默认配额使能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置在线计费是否支持默认配额应用，当取值为INHERIT时，默认配额使能开关继承SET UPDEFAULTQUOTA命令下DFTQTSWITCH参数配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承SET UPDEFAULTQUOTA命令下的同名参数。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| DFTQTNEWSER | 新业务默认配额使能开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTQTSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置新业务触发申请配额期间是否允许使用默认配额。当取值为INHERIT时，新业务默认配额使能开关继承SET UPDEFAULTQUOTA命令下DFTQTNEWSER参数配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承SET UPDEFAULTQUOTA命令下的同名参数。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| DFTQTOTHER | 非新业务场景默认配额使能开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTQTSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置非新业务场景申请配额期间是否允许使用默认配额。当取值为INHERIT时，非新业务场景默认配额使能开关继承SET UPDEFAULTQUOTA命令下DFTQTOTHER参数配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承SET UPDEFAULTQUOTA命令下的同名参数。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPAPNCHARGE]] · APN计费配置（UPAPNCHARGE）

## 使用实例

apn1的用户默认配额开关设置为使能状态：

```
SET UPAPNCHARGE: APN="apn1", DFTQTSWITCH=ENABLE, DFTQTNEWSER=ENABLE, DFTQTOTHER=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-UPAPNCHARGE.md`
