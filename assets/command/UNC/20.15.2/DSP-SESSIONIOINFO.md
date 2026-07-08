---
id: UNC@20.15.2@MMLCommand@DSP SESSIONIOINFO
type: MMLCommand
name: DSP SESSIONIOINFO（显示会话惯性运行信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SESSIONIOINFO
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 查询会话惯性运行信息
status: active
---

# DSP SESSIONIOINFO（显示会话惯性运行信息）

## 功能

**适用NF：SMF**

该命令用于查询5G会话上下文惯性运行信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（用户IMSI号）<br>- MSISDN（用户MSISDN号）<br>- MEI（用户MEI号）<br>默认值：无<br>配置原则：无 |
| IMSI | 国际移动用户标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定用户永久标识或者国际移动用户标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| MSISDN | 移动台国际 ISDN 号码 | 可选必选说明：该参数在"QUERYTYPE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定一般公共订阅标识或移动台国际 ISDN 号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| MEI | IMEI | 可选必选说明：该参数在"QUERYTYPE"配置为"MEI"时为条件必选参数。<br>参数含义：该参数用于指定永久设备标识或国际移动设备标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~16。<br>默认值：无<br>配置原则：无 |
| PDUSESSIONID | PDU 会话标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定 PDU 会话 ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [会话惯性运行信息（SESSIONIOINFO）](configobject/UNC/20.15.2/SESSIONIOINFO.md)

## 使用实例

查询类型为IMSI，IMSI为123031100100001，PDUSESIONID为5的会话惯性运行信息：

```
%%DSP SESSIONIOINFO: QUERYTYPE=IMSI, IMSI="123038700100001", PDUSESSIONID=5;%%
RETCODE = 0  操作成功

Session IO Info
----------------
               国际移动用户标识  =  123038700100001
                           IMEI  =  NULL
           移动台国际 ISDN 号码  =  8613587000001
                   PDU 会话标识  =  5
                    惯性运行状态 =  PREINERTIALOPER
            进入(预)惯性运行时间 =  2021-11-11 01:57:36+00:00
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示会话惯性运行信息（DSP-SESSIONIOINFO）_80169068.md`
