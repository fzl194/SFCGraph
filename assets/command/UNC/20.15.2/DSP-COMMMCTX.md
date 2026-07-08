---
id: UNC@20.15.2@MMLCommand@DSP COMMMCTX
type: MMLCommand
name: DSP COMMMCTX（显示移动性管理上下文的相关信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMMMCTX
command_category: 查询类
applicable_nf:
- MME
- SGSN
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 融合接入业务管理
- 融合用户数据库管理
status: active
---

# DSP COMMMCTX（显示移动性管理上下文的相关信息）

## 功能

**适用NF：MME、SGSN、AMF**

该命令用于查看移动性管理(MM)上下文的相关信息，包括用户信息、用户状态、当前跟踪区、安全信息等。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MM上下文的查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “BYIMSI（指定IMSI）”：指定IMSI<br>- “BYMSISDN（指定MSISDN）”：指定MSISDN<br>- “BYGUTI（指定4G用户的GUTI）”：指定4G用户的GUTI<br>- “BYPTMSI（指定PTMSI）”：指定PTMSI<br>- “BYIMEI（指定IMEI）”：指定IMEI<br>- “BYGUTI5G（指定5G用户的GUTI）”：指定5G用户的GUTI<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"QUERYOPT"配置为"BYIMSI"时为条件必选参数。<br>参数含义：该参数用于指定用户的IMSI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GUTI4G | 4G-GUTI | 可选必选说明：该参数在"QUERYOPT"配置为"BYGUTI"时为条件必选参数。<br>参数含义：该参数用于显示4G用户的全局设备临时标识，该参数当用户在运营商网络发起附着流程或跟踪区更新流程时分配给用户。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是19~20。<br>默认值：无<br>配置原则：无 |
| PTMSI | PTMSI | 可选必选说明：该参数在"QUERYOPT"配置为"BYPTMSI"时为条件必选参数。<br>参数含义：该参数用于指定P-TMSI号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~10。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：该参数在"QUERYOPT"配置为"BYIMEI"时为条件必选参数。<br>参数含义：该参数用于指定用户设备的国际移动设备标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~17。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"QUERYOPT"配置为"BYMSISDN"时为条件必选参数。<br>参数含义：该参数用于指定5G用户的MSISDN信息，当用户签约多个MSISDN时，仅显示第一个。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GUTI5G | 5G-GUTI | 可选必选说明：该参数在"QUERYOPT"配置为"BYGUTI5G"时为条件必选参数。<br>参数含义：该参数用于标识AMF分配给5G用户的全局唯一临时标识（5G-GUTI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是19~20。5G-GUTI的组成为[MCC] + [MNC] + [AMF Region ID] + [AMF Set ID] + [AMF Pointer] + [5G-TMSI]，其中MCC为3个十进制数字，MNC为2-3个十进制数字；AMF Region ID、AMF Set ID和AMF Pointer合成AMF Identifier，使用十六进制（0-9，a-f，A-F）表示，占6个字符；5G-TMSI是AMF内的唯一标识，使用十六进制表示，占8个字符。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [移动性管理上下文的相关信息（COMMMCTX）](configobject/UNC/20.15.2/COMMMCTX.md)

## 使用实例

查询IMSI为123031700100001用户移动性管理上下文的相关信息，执行如下命令：

```
%%DSP COMMMCTX: QUERYOPT=BYIMSI, IMSI="123031700100001";%%
RETCODE = 0  Operation succeeded

5G查询结果如下
------------------------------
                                                         IMSI  =  123031700100001
                                                      5G-GUTI  =  12303000041EF9C2F01
                                                       RM状态  =  已注册状态
                                                       CM状态  =  连接空闲状态
                                                      当前TAI  =  12303110101
                                                      当前gNB  =  12303110151
                                                      TAI列表  =  12303110101
                                                 移动管理能力  =  0400
                                                S1 UE网络能力  =  01000000
                                                   UE安全能力  =  FFFFFFFF
                                                          KSI  =  00
                                                     加密算法  =  SNOW 3G加密算法
                                                   完整性算法  =  SNOW 3G完整性保护算法
                                                  上行NAS计数  =  0x1
                                                  下行NAS计数  =  0x2
                                                   支持的功能  =  NULL
                                           签约的UE AMBR(bps)  =  BitRateUl:5000000000 BitRateDl:5000000000
                                                      Rat限制  =  NULL
                                             签约的注册定时器  =  0
                                                   UE使用类型  =  0
                                                    MPS优先级  =  false
                                                     禁止区域  =  NULL
                                               使用的RFSP索引  =  NULL
                                               使用的区域限制  =  NULL
                                               核心网类型限制  =  NULL
                                                     LADN信息  =  NULL
                                                   UE无线能力  =  NULL
                                                 MICO模式标识  =  NULL
                                                   UE时间区域  =  +08:00
                                            最后访问注册的TAI  =  NULL
                                                    请求的DRX  =  NULL
                                                      RRC状态  =  NULL
                                                       POD ID  =  uncpod-0
                                                 寻呼处理标识  =  TRUE
                                        请求通过NAS传输短消息  =  SMS over NAS not supported
                                            通过NAS传输短消息  =  SMS over NAS not allowed
                                                     漫游属性  =  本网用户
                                                     可达标志  =  不可达
                                          来自UDM的RFSP Index  =  NULL
                                          来自PCF的RFSP Index  =  NULL
                                    来自UDM的服务区域限制列表  =  NULL
                                    来自PCF的服务区域限制列表  =  NULL
                                           AM策略中的Triggers  =  NULL
                                           UE策略中的Triggers  =  NULL
                                            AM策略中的PRA列表  =  NULL
                                            UE策略中的PRA列表  =  NULL
                                               请求的网络切片  =  NULL
                                               签约的网络切片  =  1-010101;default:1-010101
                                               配置的网络切片  =  1-010101
                                               允许的网络切片  =  1-010101
                                                  SMS签约数据  =  SmsSubscribed:false; SharedSmsSubsDataId:NULL
                                                          PEI  =  NULL
                                                 NR小区标识符  =  NULL
                                                    使用的DRX  =  NULL
                                               UE信令抑制状态  =  NULL
                                                 惯性运行状态  =  关闭
                                             惯性运行起始时间  =  NULL
                                                    UDM实例ID  =  udm_instance_0
                                                       MSISDN  =  8613517000001
                                                    签约的DNN  =  NULL
                                               用户上下文类型  =  NULL
                                            AMF全局唯一标识符  =  NULL
                                             N2接口的容灾状态  =  NULL
                                               冲突处理优先级  =  0
                                  各基于业务接口SBI的容灾状态  =  NULL
                                               信息不可信标识  =  NULL
                                           UDM Bypass状态标记  =  否
                                                POD版本号信息  =  20.2.B062
                                                 无线接入类型  =  NR
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示移动性管理上下文的相关信息（DSP-COMMMCTX）_58365337.md`
