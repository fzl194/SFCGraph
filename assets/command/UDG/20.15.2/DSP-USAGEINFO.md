---
id: UDG@20.15.2@MMLCommand@DSP USAGEINFO
type: MMLCommand
name: DSP USAGEINFO（查询会话上下文用量信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: USAGEINFO
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 查询会话用量信息
status: active
---

# DSP USAGEINFO（查询会话上下文用量信息）

## 功能

**适用NF：UPF**

命令用来显示用户未上报给SMF的用量信息，检查N4接口消息中Usage Report信息的正确性。

## 注意事项

在业务进行期间，由于用户的用量时刻变化，查询到的数据信息仅能代表查询时刻的用量，可能与上报给SMF的N4接口消息中的Usage Report信息存在差异。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERID | 用户标识类型 | 可选必选说明：必选参数<br>参数含义：指定需要查询的用户标识类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用户的IMSI号。<br>- MSISDN：用户的MSISDN号。<br>- IPv4：用户的IPv4地址。<br>- IPv6：用户的IPv6地址。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERID”配置为“IMSI”时为必选参数。<br>参数含义：用户的IMSI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：配置IMSI表示查询指定IMSI号的用户的计费信息。 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERID”配置为“MSISDN”时为必选参数。<br>参数含义：用户的MSISDN号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：配置MSISDN表示查询指定的MSISDN号的用户的计费信息。 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERID”配置为“IPv4”时为必选参数。<br>参数含义：用户的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：配置IPv4表示查询指定的IPv4地址的用户的计费信息。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERID”配置为“IPv6”时为必选参数。<br>参数含义：用户的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。<br>默认值：无<br>配置原则：配置IPv6表示查询指定的IPv6地址的用户的计费信息。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@USAGEINFO]] · 会话上下文用量信息（USAGEINFO）

## 使用实例

查询IMSI号为131456789012342的用户的用量信息：

```
DSP USAGEINFO: USERID=IMSI, IMSI="131456789012342";
```

```

Session Usage Information
-------------------------
Result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

Session on Pod: isu-pod-0
-------------------------------
                               IMSI = 131456789012342
                             MSISDN = NULL
                               IPv4 = 192.168.1.10
                               IPV6 = fc02:abcd:1234:5678:9abc:def0:1234:5678
                                APN = 064apn1.com
             Session Establish Time = 2024-10-29 15:24:20
           Session Last Packet Time = 2024-10-29 15:24:24

Usage Info:
-----------
                             URR ID = 49462(Dynamic)
                     BearerSequence = 1
               Time Quota Mechanism = Normal
                         Time Quota = NA
                     Time Threshold = 3600 s
                           Duration = 1 s
                       Volume Quota = NA
                   Volume Threshold = 10240000 B (Up: NA; Down: NA)
                       Total Volume = 2004 B
                     Up-link Volume = 1325 B
                   Down-link Volume = 679 B
                 Service Start Time = 2024-10-29 15:24:20
                   Service End Time = 2024-10-29 15:24:24
               Time Of First Packet = 2024-10-29 15:24:23
                Time Of Last Packet = 2024-10-29 15:24:24

                             URR ID = 27001(Predefined)
                     BearerSequence = 1
               Time Quota Mechanism = Normal
                         Time Quota = 60 s
                     Time Threshold = 60 s
                           Duration = 4 s
                       Volume Quota = 1024000 B
                   Volume Threshold = 1024000 B (Up: NA; Down: NA)
                       Total Volume = 2004 B
                     Up-link Volume = 1325 B
                   Down-link Volume = 679 B
                 Service Start Time = 2024-10-29 15:24:20
                   Service End Time = 2024-10-29 15:24:24
               Time Of First Packet = 2024-10-29 15:24:23
                Time Of Last Packet = 2024-10-29 15:24:24

                             URR ID = 17001(Predefined)
                     BearerSequence = 1
               Time Quota Mechanism = Normal
                         Time Quota = NA
                     Time Threshold = 360 s
                           Duration = 1 s
                       Volume Quota = NA
                   Volume Threshold = 102400 B (Up: NA; Down: NA)
                       Total Volume = 2004 B
                     Up-link Volume = 1325 B
                   Down-link Volume = 679 B
                 Service Start Time = 2024-10-29 15:24:20
                   Service End Time = 2024-10-29 15:24:24
               Time Of First Packet = 2024-10-29 15:24:23
                Time Of Last Packet = 2024-10-29 15:24:24

                             URR ID = 27002(Predefined)
                     BearerSequence = 1
               Time Quota Mechanism = Normal
                         Time Quota = 60 s
                     Time Threshold = 60 s
                           Duration = 4 s
                       Volume Quota = 1024000 B
                   Volume Threshold = 1024000 B (Up: NA; Down: NA)
                       Total Volume = 0 B
                     Up-link Volume = 0 B
                   Down-link Volume = 0 B
                 Service Start Time = 2024-10-29 15:24:20
                   Service End Time = 2024-10-29 15:24:24
               Time Of First Packet = NA
                Time Of Last Packet = NA

                             URR ID = 17002(Predefined)
                     BearerSequence = 1
               Time Quota Mechanism = Normal
                         Time Quota = NA
                     Time Threshold = 360 s
                           Duration = 0 s
                       Volume Quota = NA
                   Volume Threshold = 102400 B (Up: NA; Down: NA)
                       Total Volume = 0 B
                     Up-link Volume = 0 B
                   Down-link Volume = 0 B
                 Service Start Time = 2024-10-29 15:24:20
                   Service End Time = 2024-10-29 15:24:24
               Time Of First Packet = NA
                Time Of Last Packet = NA

Online charging service volume rate info
               URRID   BeaerID        UrrType           LinkedURR             RG            SID      Up-link Volume    Down-link Volume   Rate(%)
   27001(Predefined)         1      Aggregate                   -            211           2101                1325                 679      100%
   27002(Predefined)         1      Aggregate                   -            212           2102                   0                   0        0%

Offline charging service volume rate info
               URRID   BeaerID        UrrType           LinkedURR             RG            SID      Up-link Volume    Down-link Volume   Rate(%)
   17001(Predefined)         1      Aggregate      49462(Dynamic)            111           1101                1325                 679      100%
   17002(Predefined)         1      Aggregate      49462(Dynamic)            112           1102                   0                   0        0%
                                                                                                                                                                                                                                                                                                                                                                                                                          
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-USAGEINFO.md`
