---
id: UDG@20.15.2@MMLCommand@SET URRGRPBINDING
type: MMLCommand
name: SET URRGRPBINDING（设置用户模板的URR组绑定关系）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: URRGRPBINDING
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- 用户模板
status: active
---

# SET URRGRPBINDING（设置用户模板的URR组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

![](设置用户模板的URR组绑定关系（SET URRGRPBINDING）_82837281.assets/notice_3.0-zh-cn.png)

建议用户模板下的同时配置缺省URR组和缺省信令URR组，否则可能导致使用该用户模板的用户的部分流量无法计费。

该命令用于设置用户模板的使用量上报规则组绑定关系。用于指定用户模板默认的计费策略，包括业务使用量上报规则组，信令使用量上报规则组，重定向使用量上报规则组和TCP重传使用量上报规则组。

## 注意事项

- 该命令执行后立即生效。
- 如果UserProfile下不绑定业务使用量上报规则组和信令使用量上报规则组，只有在线计费且UserProfile没有绑定任何Rule时，用户的数据包按全局使用量上报规则组计费，否则不计费。
- 当基于Rule匹配不到对应的使用量上报规则组时，如果UserProfile下使用URRGrpBinding命令配置了对应的使用量上报规则组，则可使用UserProfile下的计费策略进行计费：
    - 业务使用量上报规则组：当用户在匹配不到Rule下URRGroup时使用。
    - 信令使用量上报规则组：Rule下没有配置信令使用量上报规则组时使用，此时没有关联到业务的信令报文会按此计费。
    - TCP重传使用量上报规则组：当需要对TCP重传报文进行计费时使用。配置该属性，可能导致CPU占用率上升。
    - 重定向使用量上报规则组：对URL重定向或Captive Portal重定向报文进行计费时使用。
- 对于每个UserProfile，初始的使用量上报规则组名称和TCP重传计费标识均为空。
- Rule、Filter、Flowfilter、Userprofile和URRGrpBinding相关配置在特定组合下需要兜底配置，否则可能会影响计费准确性。
- 该命令设定后的数据，需要通过LST USERPROFILE命令进行查看。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| DFTURRGRPNAME | 缺省URR组名称 | 可选必选说明：可选参数<br>参数含义：指定缺省URR组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD URRGROUP命令配置生成。<br>- 输入单空格将删除该参数已有配置项。 |
| DFTSIGURRGNAME | 缺省信令URR组名称 | 可选必选说明：可选参数<br>参数含义：指定缺省信令URR组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD URRGROUP命令配置生成。<br>- 输入单空格将删除该参数已有配置项。 |
| REDURRGRPNAME | 重定向URR组名称 | 可选必选说明：可选参数<br>参数含义：指定重定向URR组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD URRGROUP命令配置生成。<br>- 输入单空格将删除该参数已有配置项。 |
| TCPCHGPROFLAG | TCP重传计费标识 | 可选必选说明：可选参数<br>参数含义：指定TCP重传计费标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NOTCONFIG：未配置。<br>- CHARGING：计费。<br>- NOCHARGING：不计费。<br>默认值：无<br>配置原则：<br>- NOTCONFIG：未指定TCP重传特殊计费。<br>- CHARGING：指定TCP重传计费为计费。<br>- NOCHARGING：指定TCP重传计费为不计费。 |
| TCPURRGRPNAME | TCP重传URR组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TCPCHGPROFLAG”配置为“CHARGING”时为必选参数。<br>参数含义：指定TCP重传URR组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| GLBDFTURRGSW | 继承全局缺省URR组配置开关 | 可选必选说明：可选参数<br>参数含义：该参数用来指定当缺省URR组未配置时是否继承全局缺省URR组SET SPECTRAFURRGRP配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：如果该用户模板期望严格按照规则配置进行计费，在规则未绑定URR时不通过缺省费率进行计费，则需要将此配置设置为DISABLE。 |
| GLBDFTSIGURRGSW | 继承全局缺省信令URR组开关 | 可选必选说明：可选参数<br>参数含义：该参数用来指定当缺省信令URR组未配置时是否继承全局缺省URR组SET SPECTRAFURRGRP配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：如果该用户模板期望严格按照规则配置进行计费，在规则未绑定URR时不通过缺省费率进行计费，则需要将此配置设置为DISABLE。 |

## 操作的配置对象

- [用户模板的URR组绑定关系（URRGRPBINDING）](configobject/UDG/20.15.2/URRGRPBINDING.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00013]]

## 使用实例

假如运营商希望为用户模板添加TCP重传使用量上报规则，并打开TCP重传计费：

```
SET URRGRPBINDING: USERPROFILENAME="testuserprofilename", TCPCHGPROFLAG=CHARGING, TCPURRGRPNAME="testurrgrpname";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置用户模板的URR组绑定关系（SET-URRGRPBINDING）_82837281.md`
