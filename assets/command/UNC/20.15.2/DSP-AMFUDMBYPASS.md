---
id: UNC@20.15.2@MMLCommand@DSP AMFUDMBYPASS
type: MMLCommand
name: DSP AMFUDMBYPASS（显示用户UDM Bypass信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: AMFUDMBYPASS
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF的UDM故障BYPASS功能
status: active
---

# DSP AMFUDMBYPASS（显示用户UDM Bypass信息）

## 功能

**适用NF：AMF**

该命令用于查询5G用户UDM Bypass信息。

## 注意事项

此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、GUTI。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（IMSI）”：IMSI<br>- “MSISDN（MSISDN）”：MSISDN<br>- “IMEI（IMEI）”：IMEI<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"QUERYOPT"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的IMSI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"QUERYOPT"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的MSISDN信息，当用户签约多个MSISDN时，仅显示第一个。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：该参数在"QUERYOPT"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于指定用户设备的国际移动设备标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户UDM Bypass信息（AMFUDMBYPASS）](configobject/UNC/20.15.2/AMFUDMBYPASS.md)

## 使用实例

查询IMSI为123451234567890用户的UDM Bypass信息，执行如下命令：

```
%%DSP AMFUDMBYPASS:QUERYOPT=IMSI,IMSI="123451234567890";%%
RETCODE = 0  操作成功

结果如下
------------------------
                   IMSI  =  123451234567890
                 MSISDN  =  8612345678900
                   IMEI  =  NULL
     UDM Bypass状态标记  =  是
 进入UDM Bypass状态时间  =  "2024-07-26T08:36:46+08:00"
            UDM交互状态  =  Bypass
 
(结果个数  = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示用户UDM-Bypass信息（DSP-AMFUDMBYPASS）_50109442.md`
