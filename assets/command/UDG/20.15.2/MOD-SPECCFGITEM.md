---
id: UDG@20.15.2@MMLCommand@MOD SPECCFGITEM
type: MMLCommand
name: MOD SPECCFGITEM（修改产品内部需要调整规格比例的项目）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: SPECCFGITEM
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 用户面服务管理
- 业务运维
- 业务规格管理
- 内部规格调整管理
status: active
---

# MOD SPECCFGITEM（修改产品内部需要调整规格比例的项目）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](修改产品内部需要调整规格比例的项目（MOD SPECCFGITEM）_55657468.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，此命令配置不正确可能导致业务资源不足引发告警以及用户业务受损，或者触发系统内存不足导致进程复位或者虚机复位，需要评估清楚风险后再操作。

该命令用于修改产品内部需要调整规格比例项目的调整比例。

## 注意事项

- 该命令执行后需要复位相应的微服务才能生效。
- 该命令配置前必须通过华为工程师根据产品承载的业务范围和场景进行评估，确定调整比例。
- 该命令配置的调整比例如果过小，可能导致资源不足产生告警。
- 该命令配置的调整比例如果过大，可能超出产品总体资源的范围。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ITEMNAME | 内部配置项名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要调整规格的内部配置项名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127，不区分大小写。<br>默认值：无<br>配置原则：配置项名称应当与实际业务使用的名称相符，如果不匹配则无法生效，可通过命令DSP SPECCFGINFO查询当前支持规格配置的项目。 |
| SERVICETYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于制定配置项规格调整生效的微服务范围。<br>数据来源：本端规划<br>取值范围：字符串类型，长度1~127，不区分大小写。<br>默认值：无<br>配置原则：具体可配置的微服务类型可通过DSP SPECCFGINFO查询。 |
| ITEMRATE | 配置项规格调整比例 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规格配置项调整的百分比。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1~1000，表示规格调整比例调整范围为1%~1000%。<br>默认值：无<br>配置原则：此参数需要根据实际业务需要进行调整，调整阈值必须由华为工程师确认影响后才可执行。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SPECCFGITEM]] · 产品内部需要调整规格比例的项目（SPECCFGITEM）

## 使用实例

根据当前业务评估，“SRR_PER_PDP”资源规格依然存在不足，需要将该资源规格扩充到150%，可以按如下方式操作：

```
MOD SPECCFGITEM:ITEMNAME="SRR_PER_PDP", SERVICETYPE="SessionSGExecSvc", ITEMRATE="150";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-SPECCFGITEM.md`
