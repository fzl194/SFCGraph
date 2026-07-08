---
id: UNC@20.15.2@MMLCommand@DSP NGMMCTX
type: MMLCommand
name: DSP NGMMCTX（显示5G移动性管理上下文）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGMMCTX
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

# DSP NGMMCTX（显示5G移动性管理上下文）

## 功能

**适用NF：AMF**

该命令用于查询5G移动性管理（MM）上下文的相关信息，包括用户信息、用户状态、当前跟踪区、安全信息等。

## 注意事项

- 此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、GUTI。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。
- 在灰度升级期间执行该命令，只允许查询高版本POD上的用户。
- 用户去注册时，AMF会将下发给UE的MPS能力和MCS能力重置为“NOT_SUPPORT（不支持）”。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MM上下文的查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（IMSI）”：IMSI<br>- “MSISDN（MSISDN）”：MSISDN<br>- “IMEI（IMEI）”：IMEI<br>- “GUTI（GUTI）”：GUTI<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"QUERYOPT"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的IMSI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"QUERYOPT"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的MSISDN信息，当用户签约多个MSISDN时，仅显示第一个。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：该参数在"QUERYOPT"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于指定用户设备的国际移动设备标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GUTI | 5G-GUTI | 可选必选说明：该参数在"QUERYOPT"配置为"GUTI"时为条件必选参数。<br>参数含义：该参数用于标识AMF分配给5G用户的全局唯一临时标识（5G-GUTI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是19~20。5G-GUTI的组成为[MCC] + [MNC] + [AMF Region ID] + [AMF Set ID] + [AMF Pointer] + [5G-TMSI]，其中MCC为3个十进制数字，MNC为2-3个十进制数字；AMF Region ID、AMF Set ID和AMF Pointer合成AMF Identifier，使用十六进制（0-9，a-f，A-F）表示，占6个字符；5G-TMSI是AMF内的唯一标识，使用十六进制表示，占8个字符。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGMMCTX]] · 5G移动性管理上下文（NGMMCTX）

## 使用实例

查询IMSI为123031234567890用户的MM上下文，执行如下命令：

```
%%DSP NGMMCTX: QUERYOPT=IMSI, IMSI="123031234567890";%%
RETCODE = 0  操作成功

结果如下
------------------------
                     POD ID  =  uncpod-0
                       IMSI  =  123031234567890
                     MSISDN  =  8613512345678
                        PEI  =  NULL
                    5G-GUTI  =  123030000416FEC6F36
                   漫游属性  =  本网用户
                     RM状态  =  已注册状态
                     CM状态  =  已连接状态
                    RRC状态  =  Connected
                   可达标志  =  可达
             UE信令抑制状态  =  NULL
                    当前TAI  =  12303110101
                 当前gNB     =  12303110151
               NR小区标识符  =  12303120110201
                    TAI列表  =  12303110101
          最后访问注册的TAI  =  NULL
                 UE时间区域  =  +08:00
               移动管理能力  =  0400
              S1 UE网络能力  =  01000000
                 UE无线能力  =  NULL
                 UE安全能力  =  FFFFFFFF
                        KSI  =  00
                   加密算法  =  SNOW 3G加密算法
                 完整性算法  =  SNOW 3G完整性保护算法
                上行NAS计数  =  0x2
                下行NAS计数  =  0x3
      请求通过NAS传输短消息  =  SMS over NAS not supported
             请求的网络切片  =  NULL
                  请求的DRX  =  NULL
                 支持的功能  =  NULL
                SMS签约数据  =  SmsSubscribed:false; SharedSmsSubsDataId:NULL
         签约的UE AMBR(bps)  =  BitRateUl:2147483648 BitRateDl:2147483648
             签约的网络切片  =  1-010101;default:1-010101
                    Rat限制  =  WLAN
                   禁止区域  =  NULL
  来自UDM的服务区域限制列表  =  NULL
             核心网类型限制  =  NULL
           签约的RFSP Index  =  6
           签约的注册定时器  =  3240
                 UE使用类型  =  11
                  MPS优先级  =  true
                   LADN信息  =  NULL
               MICO模式标识  =  NULL
        来自PCF的RFSP Index  =  5
  来自PCF的服务区域限制列表  =  NULL
         AM策略中的Triggers  =  LOC_CH
          AM策略中的PRA列表  =  NULL
         UE策略中的Triggers  =  NULL
               寻呼处理标识  =  TRUE
          UE策略中的PRA列表  =  NULL
             使用的区域限制  =  NULL
             使用的RFSP索引  =  5
                  使用的DRX  =  NULL
          通过NAS传输短消息  =  SMS over NAS not allowed
             配置的网络切片  =  1-010101
             允许的网络切片  =  1-010101
               惯性运行状态  =  关闭
           惯性运行起始时间  =  2020-01-01T08:00:01+08:00
                  UDM实例ID  =  udm_instance_0
             用户上下文类型  =  NULL
          AMF全局唯一标识符  =  460-03-1-1-0
           N2接口的容灾状态  =  O-AMF Takeover
             冲突处理优先级  =  0
各基于业务接口SBI的容灾状态  =  N8:1-N12:1-N14:1-N15:0-N20:0-N22:1-NLg:0-NLs:1
             信息不可信标识  =  NULL
                  签约的DNN  =  huawei12.com; abc
         UDM Bypass状态标记  =  否
              POD版本号信息  =  20.2.B062
               无线接入类型  =  5G接入
          下发给UE的MPS能力  =  支持
          下发给UE的MCS能力  =  支持
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示5G移动性管理上下文（DSP-NGMMCTX）_09651524.md`
