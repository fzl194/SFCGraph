---
id: UNC@20.15.2@MMLCommand@RMV 5GCREMARK
type: MMLCommand
name: RMV 5GCREMARK（删除5GC QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: 5GCREMARK
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC Qos映射ToS_DSCP
status: active
---

# RMV 5GCREMARK（删除5GC QoS到TOS/DSCP的映射规则）

## 功能

**适用NF：SMF**

该命令用来删除5G用户QoS参数到IP DSCP（区别服务编码点）/TOS（服务类型）的映射配置。输入必选参数Qos Profile名时，支持批量删除。

## 注意事项

命令执行后只对新接入用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：必选参数<br>参数含义：该参数指定QoS Profile的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| FIVEQI | 5QI | 可选必选说明：必选参数<br>参数含义：该参数表示5G QoS Identifier。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP的优先级别 | 可选必选说明：必选参数<br>参数含义：该参数表示ARP的优先级别。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~15。<br>默认值：无<br>配置原则：<br>- 0：General，通用用户。如果某业务级别各个优先级的用户都没有配置DSCP，则用General配置的值。<br>- 1~15：用户的优先级，其中1的优先级最高。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/5GCREMARK]] · 5GC QoS到TOS/DSCP的映射规则（5GCREMARK）

## 使用实例

删除Qos Profile名称为“profile”，5QI值为5，ARP优先级为5的配置实例：

```
RMV 5GCREMARK:QOSPROFILENAME="profile",FIVEQI=5,ARPPL=5; 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5GC-QoS到TOS_DSCP的映射规则（RMV-5GCREMARK）_09652352.md`
