---
id: UDG@20.15.2@MMLCommand@SET GLOBALIMS
type: MMLCommand
name: SET GLOBALIMS（设置全局IMS配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLOBALIMS
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- VOLTE管理
- 全局IMS配置
status: active
---

# SET GLOBALIMS（设置全局IMS配置）

## 功能

**适用NF：PGW-U、UPF**

![](设置全局IMS配置（SET GLOBALIMS）_82837830.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，系统只配置了语音APN才能打开该开关。

该命令用来配置IMS互通相关的设置。当IMS使能开关打开时，才可以对IMS信令空口增强开关以及P-CSCF缺省组进行配置。当运营商需要控制IMS互通相关的参数时，可使用该命令对全局IMS配置参数进行配置。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- P-CSCF缺省组在系统内只能存在一个，未通过本命令明确指定时，则认为系统中没有缺省组。
- SGW-U/I-UPF上，使能ApnImsAttr配置会触发PF的SIP信令解析，可能影响性能。
- PGW-U/PSA-UPF上，如果数据APN下发有QCI为5的业务承载，会触发PF的filter匹配和SIP信令解析，可能会影响性能；filter匹配依赖ADD APNIMSSIGFLTR配置，如果配置错误，可能会导致匹配失败报文被丢弃。
- 该配置可能会影响地址池的地址租约功能，如果参数APN为语音的APN，需要开启地址池下的IMS开关，地址租约功能才对此APN生效；如果数据APN的IMS开关配置错误，可能会导致该APN的地址租约功能失效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IMSSWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSSWITCH | IMS功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于打开或关闭IMS功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：系统只配置了语音APN才能打开该开关。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLOBALIMS]] · 全局IMS配置（GLOBALIMS）

## 使用实例

当用户需要配置全局IMS开关时，进行如下设置：

```
SET GLOBALIMS:IMSSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-GLOBALIMS.md`
