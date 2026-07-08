---
id: UNC@20.15.2@MMLCommand@RMV NGGUTISELPLCY
type: MMLCommand
name: RMV NGGUTISELPLCY（删除AMF区域GUTI选网控制策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGGUTISELPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域GUTI选网功能管理
- AMF区域GUTI选网策略
status: active
---

# RMV NGGUTISELPLCY（删除AMF区域GUTI选网控制策略）

## 功能

**适用NF：AMF**

该命令用于删除AMF区域GUTI选网功能控制策略。

## 注意事项

- 该命令执行后立即生效。

- 该命令增加、修改或者删除后，针对新接入的用户立即生效，对于已经接入的用户不会立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREARANGE | 区域范围 | 可选必选说明：必选参数<br>参数含义：该参数用于设置指定区域GUTI选网功能的区域范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_AREA（所有区域）”：所有区域<br>- “AREA_CODE（指定区域编码）”：指定区域编码<br>默认值：无<br>配置原则：无 |
| GUTISELAREACODE | GUTI选网功能区域编码 | 可选必选说明：该参数在"AREARANGE"配置为"AREA_CODE"时为条件必选参数。<br>参数含义：该参数用于指定应用GUTI选网功能的某个区域。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。该区域编码必须先通过ADD GUTISELAREACODE进行添加；而区域内的跟踪区列表则通过ADD GUTISELAREAMEM进行添加。<br>默认值：无<br>配置原则：无 |
| CTRLOBJECT | 控制对象 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用指定区域GUTI选网功能的用户的识别对象。<br>数据来源：全网规划<br>取值范围：<br>- “USER_GROUP（用户群）”：用户群<br>- “SUB_NS（签约切片）”：签约切片<br>- “SUB_UUT（签约UE USAGE TYPE）”：签约UE USAGE TYPE<br>默认值：无<br>配置原则：无 |
| SUBGRPID | 用户群组标识 | 可选必选说明：该参数在"CTRLOBJECT"配置为"USER_GROUP"时为条件必选参数。<br>参数含义：该参数用于指定应用GUTI选网功能的用户群组。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。该用户群组标识通过ADD NGUSRGRP进行添加；群组内的用户标识列表通过ADD NGUSRGRPMEM进行添加。<br>默认值：无<br>配置原则：<br>当针对指定的区域，有多个用户（号段）需要进行GUTI选网时，建议通过本参数指定用户范围。<br>该值若不设置，默认值为4294967295。 |
| SST | 切片业务类型 | 可选必选说明：该参数在"CTRLOBJECT"配置为"SUB_NS"时为条件必选参数。<br>参数含义：该参数表示切片的业务类型，如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65534。<br>默认值：无<br>配置原则：<br>该值若不设置，默认值为65535。 |
| SD | 切片细分标识 | 可选必选说明：该参数在"CTRLOBJECT"配置为"SUB_NS"时为条件可选参数。<br>参数含义：该参数表示根据网络切片所提供的服务特点、所服务的对象差异，对某种网络切片的进一步细分。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>该值若不设置，默认值为FFFFFF。 |
| UUT | UE USAGE TYPE | 可选必选说明：该参数在"CTRLOBJECT"配置为"SUB_UUT"时为条件必选参数。<br>参数含义：该参数用于指定应用GUTI选网功能的UE Usage Type。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。该值若不设置，默认值为65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGGUTISELPLCY]] · AMF区域GUTI选网控制策略（NGGUTISELPLCY）

## 使用实例

删除区域“GUTISelZone”下，用户（从属的用户组ID为“1”）的AMF区域GUTI选网功能控制策略。

```
RMV NGGUTISELPLCY: AREARANGE=AREA_CODE, GUTISELAREACODE="GUTISelZone", CTRLOBJECT=USER_GROUP, SUBGRPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGGUTISELPLCY.md`
