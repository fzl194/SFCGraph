---
id: UNC@20.15.2@MMLCommand@SET OSPFGR
type: MMLCommand
name: SET OSPFGR（设置OSPF的平滑重启）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OSPFGR
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF的平滑重启配置
status: active
---

# SET OSPFGR（设置OSPF的平滑重启）

## 功能

该命令用于配置设备平滑重启Helper模式。

## 注意事项

- 该命令执行后立即生效。
- 只有执行MOD OSPF配置了OPAQCAPFLG才能使用此命令。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| HELPERROLEFLAG | PLANNEDONLYFLG | IGNEXTELSAFLG | NEVERFLAG | HELPERFLAG | HELPERFILTERTYPE |
| --- | --- | --- | --- | --- | --- |
| FALSE | FALSE | FALSE | FALSE | FALSE | none |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| HELPERROLEFLAG | 使能Helper模式 | 可选必选说明：必选参数<br>参数含义：使能Helper模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无<br>配置原则：当HELPERROLEFLAG配置为TRUE时，至少需要配置PLANNEDONLYFLG、IGNEXTELSAFLG、NEVERFLAG或HELPERFILTERTYPE四个参数其中一个。 |
| PLANNEDONLYFLG | 只支持计划GR | 可选必选说明：条件可选参数<br>前提条件：该参数在“HELPERROLEFLAG”配置为“TRUE”时为可选参数。<br>参数含义：在设备上支持计划内的平滑重启。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：缺省情况下，设备支持planned-GR和unplanned-GR。 |
| IGNEXTELSAFLG | 不检查Type-5和Type-7类的LSA | 可选必选说明：条件可选参数<br>前提条件：该参数在“HELPERROLEFLAG”配置为“TRUE”时为可选参数。<br>参数含义：不检查Type-5和Type-7类的LSA。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| NEVERFLAG | 不支持Helper模式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“HELPERROLEFLAG”配置为“TRUE”时为可选参数。<br>参数含义：不支持Helper模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| HELPERFLAG | 使能GR | 可选必选说明：必选参数<br>参数含义：使能GR。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| HELPERFILTERTYPE | Helper过滤类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“HELPERROLEFLAG”配置为“TRUE”时为可选参数。<br>参数含义：Helper过滤类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl_name：ACL名称。<br>- ip_prefix：IP前缀过滤策略名称。<br>- acl_num：ACL号。<br>- none：空。<br>默认值：无 |
| HELPERROLEVALUE | Helper过滤值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HELPERFILTERTYPE”配置为“acl_name”、“ip_prefix” 或 “acl_num”时为必选参数。<br>参数含义：Helper过滤值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |

## 操作的配置对象

- [OSPF的平滑重启配置（OSPFGR）](configobject/UNC/20.15.2/OSPFGR.md)

## 使用实例

使能OSPF进程1的平滑重启Helper模式的策略特性，配置本地Helper策略为只支持Planned GR：

```
SET OSPFGR:PROCID=1,PLANNEDONLYFLG=TRUE,HELPERROLEFLAG=TRUE,NEVERFLAG=FALSE,HELPERFLAG=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置OSPF的平滑重启（SET-OSPFGR）_49961154.md`
