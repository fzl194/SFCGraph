---
id: UDG@20.15.2@MMLCommand@SET APNTRFCDFDSWITCH
type: MMLCommand
name: SET APNTRFCDFDSWITCH（设置大流量攻击防护APN开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNTRFCDFDSWITCH
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- DDoS防护
- 大流量攻击防护APN开关
status: active
---

# SET APNTRFCDFDSWITCH（设置大流量攻击防护APN开关）

## 功能

**适用NF：UPF**

![](设置大流量攻击防护APN开关（SET APNTRFCDFDSWITCH）_86530451.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确认TrfcDfdPara配置合理，否则可能导致用户丢包或去活。

该命令用于配置指定APN下大流量攻击检测开关是否开启。某一周期内某用户下行报文数与上行报文数之比大于TRFCDFDPARA命令设定的阈值，则认为该用户存在下行大流量攻击行为。对这种大流量攻击行为的检测即为大流量攻击检测。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条。
- APN下的上行大流量攻击检测开关没有配置记录，缺省为继承全局TRFCDFDSWITCH配置。
- APN下的下行大流量攻击检测开关没有配置记录，缺省为继承全局TRFCDFDSWITCH配置。
- 使能该功能前，请检查TrfcDfdPara配置是否合理，否则开启后会被误识别为攻击流量，导致用户丢包或去活。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| UPSWITCH | 上行大流量攻击防护APN功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否开启APN内上行大流量攻击检测功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承全局。<br>- ENABLE：使能。<br>- DISABLE：去使能。<br>默认值：无<br>配置原则：INHERIT：继承全局上行大流量攻击检测功能。 ENABLE：基于APN开启上行大流量攻击检测功能。 DISABLE：去使能，基于APN关闭上行大流量攻击检测功能。 |
| DOWNSWITCH | 下行大流量攻击防护APN功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否开启APN内下行大流量攻击检测功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承全局。<br>- ENABLE：使能。<br>- DISABLE：去使能。<br>默认值：无<br>配置原则：INHERIT：继承全局下行大流量攻击检测功能。 ENABLE：基于APN开启下行大流量攻击检测功能。 DISABLE：去使能，基于APN关闭下行大流量攻击检测功能。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APNTRFCDFDSWITCH]] · APN大流量攻击防护配置（APNTRFCDFDSWITCH）

## 使用实例

在CPU达到设定的阈值需要开启大流量攻击检测的场景下，设置APN为apn1.com的APN内上行大流量攻击检测为开启，下行大流量攻击检测为开启：

```
SET APNTRFCDFDSWITCH: APN="apn1.com", UPSWITCH=ENABLE, DOWNSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-APNTRFCDFDSWITCH.md`
