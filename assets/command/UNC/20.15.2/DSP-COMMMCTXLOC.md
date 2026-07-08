---
id: UNC@20.15.2@MMLCommand@DSP COMMMCTXLOC
type: MMLCommand
name: DSP COMMMCTXLOC（显示移动管理位置信息上下文）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMMMCTXLOC
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 融合接入业务管理
- 融合用户数据库管理
status: active
---

# DSP COMMMCTXLOC（显示移动管理位置信息上下文）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于查看移动性管理(MM)上下文的位置相关信息，包括当前跟踪区等。

## 注意事项

无

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MM上下文的查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “BYIMSI（指定IMSI）”：指定IMSI<br>- “BYMSISDN（指定MSISDN）”：指定MSISDN<br>- “BYGUTI（指定4G用户的GUTI）”：指定4G用户的GUTI<br>- “BYPTMSI（指定PTMSI）”：指定PTMSI<br>- “BYIMEI（指定IMEI）”：指定IMEI<br>- “BYGUTI5G（指定5G用户的GUTI）”：指定5G用户的GUTI<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"QUERYOPT"配置为"BYIMSI"时为条件必选参数。<br>参数含义：该参数用于指定用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GUTI4G | 4G-GUTI | 可选必选说明：该参数在"QUERYOPT"配置为"BYGUTI"时为条件必选参数。<br>参数含义：该参数用于显示4G用户的全局设备临时标识，该参数当用户在运营商网络发起附着流程或跟踪区更新流程时分配给用户。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是19~20。<br>默认值：无<br>配置原则：无 |
| PTMSI | PTMSI | 可选必选说明：该参数在"QUERYOPT"配置为"BYPTMSI"时为条件必选参数。<br>参数含义：该参数用于指定P-TMSI号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~10。<br>默认值：无<br>配置原则：无 |
| IMEI | ME标识 | 可选必选说明：该参数在"QUERYOPT"配置为"BYIMEI"时为条件必选参数。<br>参数含义：该参数用于指定用户设备的国际移动设备标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~17。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"QUERYOPT"配置为"BYMSISDN"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的MSISDN信息，当用户签约多个MSISDN时，仅显示第一个。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GUTI5G | 5G-GUTI | 可选必选说明：该参数在"QUERYOPT"配置为"BYGUTI5G"时为条件必选参数。<br>参数含义：该参数用于标识AMF分配给5G用户的全局唯一临时标识（5G-GUTI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是19~20。5G-GUTI的组成为[MCC] + [MNC] + [AMF Region ID] + [AMF Set ID] + [AMF Pointer] + [5G-TMSI]，其中MCC为3个十进制数字，MNC为2-3个十进制数字；AMF Region ID、AMF Set ID和AMF Pointer合成AMF Identifier，使用十六进制（0-9，a-f，A-F）表示，占6个字符；5G-TMSI是AMF内的唯一标识，使用十六进制表示，占8个字符。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [移动管理位置信息上下文（COMMMCTXLOC）](configobject/UNC/20.15.2/COMMMCTXLOC.md)

## 使用实例

查询IMSI为123031700100001用户移动性管理上下文的相关位置信息，执行如下命令：

```
%%DSP COMMMCTXLOC: QUERYOPT=BYIMSI, IMSI="123031700100001";%%
RETCODE = 0  Operation succeeded

5G查询结果如下
------------------------------
               IMSI  =  123031700100001
             MSISDN  =  8613517000001
            5G-GUTI  =  12303000041EF9C2F01
            当前TAI  =  12303110101
            当前gNB  =  12303110151
       NR小区标识符  =  12303810110201
            TAI列表  =  12303110101
  最后访问注册的TAI  =  NULL
（结果个数 = 1）

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示移动管理位置信息上下文（DSP-COMMMCTXLOC）_77419800.md`
