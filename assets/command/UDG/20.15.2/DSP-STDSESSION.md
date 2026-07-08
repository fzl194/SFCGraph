---
id: UDG@20.15.2@MMLCommand@DSP STDSESSION
type: MMLCommand
name: DSP STDSESSION（显示用户上下文）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: STDSESSION
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 会话标准信息查询
status: active
---

# DSP STDSESSION（显示用户上下文）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

用来查看指定用户上下文信息。

## 注意事项

根据IMEI查询用户只匹配前14位。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：查询方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：指定待查询用户的IMSI号。<br>- MSISDN：指定待查询用户的MSISDN号。<br>- IMEI：指定待查询用户的IMEI号。<br>默认值：无<br>配置原则：无 |
| IMSI | 用户的IMSI信息。 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“IMSI”时为必选参数。<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| IMEI | 用户的IMEI信息。 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“IMEI”时为必选参数。<br>参数含义：用户的IMEI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。每个字符必须为0~9的数字。 IMEI号的组成： 1、前6位或者8位是型号核准码(TAC)，用来区分手机品牌和型号。 2、接着2位是最后装配号(FAC)，代表最终装配地代码，仅在早期机型中存在。 3、后6位是串号(SNR)，代表生成顺序号。<br>默认值：无<br>配置原则：无 |
| MSISDN | 用户的MSISDN信息。 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/STDSESSION]] · 用户上下文（STDSESSION）

## 使用实例

查询用户上下文，MSISDN为“85362641010”：

```
DSP STDSESSION: QUERYTYPE=MSISDN,MSISDN="85362641010";
```

```

RETCODE = 0  操作成功

上下文信息
------------

                    Pod Name  =  ssgpod-0
                        IMSI  =  60456789012342
                        IMEI  =  123456789012371
                      MSISDN  =  12341234
                  Local Seid  =  0x00000000008003f1
                   Peer Seid  =  0x0000000000000001
             Local Signal IP  =  172.16.24.91
              Peer Signal IP  =  192.168.31.24
           IPv4 VPN Instance  =  NULL
           IPv6 VPN Instance  =  NULL
                         APN  =  060apn1.com
            Virtual APN Name  =  NULL
                    PDP Type  =  IPv4
           IPv4 Address Type  =  EXTERNAL ALLOC IP ADDRESS
            IPv4 PDP Address  =  10.165.2.96
           IPv6 Address Type  =  NULL
            IPv6 PDP Address  =  NULL
        IPv4 Redundancy Flag  =  false
        IPv6 Redundancy Flag  =  NULL
          IPv4 Conflict Flag  =  NULL
          IPv6 Conflict Flag  =  NULL
            Delegated Prefix  =  NULL
                    RAT Type  =  NR
                   Role Type  =  UPF
                   User Type  =  home
                   DCNR Flag  =  false
  Overload QoS Control Level  =  NULL
               DNAI VPN Flag  =  false
Session Activation Timestamp  =  22:22:39 11/12/2024(MM/DD/YYYY)
                   DNAI Flag  =  false
   User Location Information  =  NULL
          Common Policy Name  =  NULL
                   L2TP Flag  =  false
                   CP NodeID  =  0.0.0.0
                      SNSSAI  =  NULL
       MultiDnn Session Type  =  NULL
            Tethering Switch  =  DISABLE
                    NAT Flag  =  false
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示用户上下文（DSP-STDSESSION）_43134487.md`
