---
id: UNC@20.15.2@MMLCommand@DSP NGMMCTXEXT
type: MMLCommand
name: DSP NGMMCTXEXT（显示5G移动性管理上下文扩展信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGMMCTXEXT
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# DSP NGMMCTXEXT（显示5G移动性管理上下文扩展信息）

## 功能

**适用NF：AMF**

该命令用于查询5G移动性管理（MM）上下文的相关信息，包括用户信息、签约eDRX相关信息等。

## 注意事项

此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、GUTI。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MM上下文的查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（IMSI）”：IMSI<br>- “MSISDN（MSISDN）”：MSISDN<br>- “IMEI（IMEI）”：IMEI<br>- “GUTI（GUTI）”：GUTI<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"QUERYOPT"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的IMSI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"QUERYOPT"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的MSISDN信息，当用户签约多个MSISDN时，仅显示第一个。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GUTI | GUTI | 可选必选说明：该参数在"QUERYOPT"配置为"GUTI"时为条件必选参数。<br>参数含义：该参数用于标识AMF分配给5G用户的全局唯一临时标识（5G-GUTI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~22。5G-GUTI的组成为[MCC] + [MNC] + [AMF Region ID] + [AMF Set ID] + [AMF Pointer] + [5G-TMSI]，其中MCC为3个十进制数字，MNC为2-3个十进制数字；AMF Region ID、AMF Set ID和AMF Pointer合成AMF Identifier，使用十六进制（0-9，a-f，A-F）表示，占6个字符；5G-TMSI是AMF内的唯一标识，使用十六进制表示，占8个字符。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：该参数在"QUERYOPT"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于指定用户设备的国际移动设备标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~30。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGMMCTXEXT]] · 5G移动性管理上下文扩展信息（NGMMCTXEXT）

## 使用实例

查询IMSI为123031234567890用户的MM扩展上下文信息，执行如下命令：

```
%%DSP NGMMCTXEXT:QUERYOPT=IMSI, IMSI="123031234567890";%%
RETCODE = 0  操作成功

结果如下
--------
                        IMSI  =  123031234567890
                      MSISDN  =  8613518000001
                        GUTI  =  1230300004193011DB6
                        IMEI  =  NULL
        NR用户签约的寻呼周期  =  NULL
NR用户签约的寻呼时间窗口时长  =  NULL
                  NRUSEDEDRX  =  NULL
NR用户使用的寻呼时间窗口时长  =  NULL
  NR用户寻呼时间窗口开启时间  =  NULL
        来自PCF的SMF选择数据  =  NULL
来自PCF的MEC本地专网分流策略  =  NULL
              动态运营商全称  =  FullName
              动态运营商简称  =  ShortName
                MICO状态标记  =  否
              周期性定位阶段  =  Invalid
            网络切片替换信息  =  1-010101:UNAVAILABLE,1-000011
                 FWA用户标识  =  否
                寻呼分组标识  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGMMCTXEXT.md`
