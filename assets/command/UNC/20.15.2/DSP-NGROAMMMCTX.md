---
id: UNC@20.15.2@MMLCommand@DSP NGROAMMMCTX
type: MMLCommand
name: DSP NGROAMMMCTX（显示5G漫游用户移动性管理上下文）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGROAMMMCTX
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

# DSP NGROAMMMCTX（显示5G漫游用户移动性管理上下文）

## 功能

**适用NF：AMF**

该命令用于查询5G漫游用户移动性管理上下文相关信息。

## 注意事项

此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、GUTI。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定漫游用户MM上下文的查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（IMSI）”：IMSI<br>- “MSISDN（MSISDN）”：MSISDN<br>- “IMEI（IMEI）”：IMEI<br>- “GUTI（GUTI）”：GUTI<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"QUERYOPT"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"QUERYOPT"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的MSISDN信息，当用户签约多个MSISDN时，仅显示第一个。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：该参数在"QUERYOPT"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于指定用户设备的国际移动设备标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~30。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GUTI | GUTI | 可选必选说明：该参数在"QUERYOPT"配置为"GUTI"时为条件必选参数。<br>参数含义：该参数用于标识AMF分配给5G用户的全局唯一临时标识（5G-GUTI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是19~20。5G-GUTI的组成为[MCC] + [MNC] + [AMF Region ID] + [AMF Set ID] + [AMF Pointer] + [5G-TMSI]，其中MCC为3个十进制数字，MNC为2-3个十进制数字；AMF Region ID、AMF Set ID和AMF Pointer合成AMF Identifier，使用十六进制（0-9，a-f，A-F）表示，占6个字符；5G-TMSI是AMF内的唯一标识，使用十六进制表示，占8个字符。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGROAMMMCTX]] · 5G漫游用户移动性管理上下文（NGROAMMMCTX）

## 使用实例

查询IMSI为123451234567890用户的MM漫游上下文，执行如下命令：

```
%%DSP NGROAMMMCTX: QUERYOPT=IMSI, IMSI="123451234567890";%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
                     MSISDN  =  8613512345678
                       IMSI  =  123451234567890
                       IMEI  =  NULL
                       GUTI  =  12303000041405502F8
             请求的网络切片  =  NULL
             配置的网络切片  =  1-010101
             允许的网络切片  =  1-010101
           漫游切片映射关系  =  1-010101:2-010101;1-010102:2-010101
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGROAMMMCTX.md`
