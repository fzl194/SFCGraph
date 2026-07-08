---
id: UNC@20.15.2@MMLCommand@DSP SESSIONQOSINFO
type: MMLCommand
name: DSP SESSIONQOSINFO（显示会话QoS信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SESSIONQOSINFO
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 查询会话QoS信息
status: active
---

# DSP SESSIONQOSINFO（显示会话QoS信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询2G/3G/4G/5G会话上下文QoS信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（用户IMSI号）<br>- MSISDN（用户MSISDN号）<br>- MEI（用户MEI号）<br>默认值：无<br>配置原则：无 |
| IMSI | 国际移动用户标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定用户永久标识或者国际移动用户标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>该参数为23G/4G的输出参数。5G时对应输出为SUPI。 |
| MSISDN | 移动台国际 ISDN 号码 | 可选必选说明：该参数在"QUERYTYPE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定一般公共订阅标识或移动台国际 ISDN 号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| MEI | IMEI | 可选必选说明：该参数在"QUERYTYPE"配置为"MEI"时为条件必选参数。<br>参数含义：该参数用于指定永久设备标识或国际移动设备标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~16。<br>默认值：无<br>配置原则：无 |
| WLNETWKTYPE | 无线网络类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"MSISDN"、"IMSI"、"MEI"时为条件必选参数。<br>参数含义：该参数用于指定无线网络类型。<br>数据来源：本端规划<br>取值范围：<br>- NW2G3G4G（2/3/4G网络）<br>- NW5G（5G网络）<br>默认值：无<br>配置原则：无 |
| EBIORNSAPI | 承载/网络业务接入点标识 | 可选必选说明：该参数在"WLNETWKTYPE"配置为"NW2G3G4G"时为条件必选参数。<br>参数含义：该参数用于指定链接的 EPS 承载标识或者网络层服务接入点标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：<br>可以通过DSP PDUSESSION简单查询获取EBIORNSAPI后作为查询的输入参数。 |
| PDUSESSIONID | PDU 会话标识 | 可选必选说明：该参数在"WLNETWKTYPE"配置为"NW5G"时为条件必选参数。<br>参数含义：该参数用于指定 PDU 会话 ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：<br>可以通过DSP PDUSESSION简单查询获取PDUSESSIONID后作为查询的输入参数。 |
| QFI | QoS流ID | 可选必选说明：该参数在"WLNETWKTYPE"配置为"NW5G"时为条件可选参数。<br>参数含义：该参数用于指定QoS流ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~63。<br>默认值：无<br>配置原则：<br>可以通过DSP PDUSESSION简单查询获取QOSQFIS后作为查询的输入参数。 |
| ACCESSTYPE234G | 接入方式 | 可选必选说明：该参数在"WLNETWKTYPE"配置为"NW2G3G4G"时为条件可选参数。<br>参数含义：该参数用于指定接入类型。<br>数据来源：本端规划<br>取值范围：<br>- AT_3GPP_ACCESS（3GPP_ACCESS）<br>- AT_UNTRUSTED_NON_3GPP_ACCESS（UNTRUSTED_NON_3GPP_ACCESS）<br>- AT_TRUSTED_NON_3GPP_ACCESS（TRUSTED_NON_3GPP_ACCESS）<br>默认值：AT_3GPP_ACCESS<br>配置原则：<br>该值若不设置，默认值为AT_3GPP_ACCESS。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SESSIONQOSINFO]] · 会话QoS信息（SESSIONQOSINFO）

## 使用实例

查询类型为IMSI，IMSI为123031100100001，无线网络类型为NW5G，PDUSESIONID为5，QFI为1的会话QoS信息：

```
%%DSP SESSIONQOSINFO: QUERYTYPE=IMSI, IMSI="123038700100001", WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;%%
RETCODE = 0  操作成功

Session QoS Info
----------------
               国际移动用户标识  =  123038700100001
                           IMEI  =  NULL
           移动台国际 ISDN 号码  =  8613587000001
        承载/网络业务接入点标识  =  0
                     签约的 DNN  =  huawei.com
                   PDU 会话标识  =  5
                    QosFlow QFI  =  NULL
                 本端节点的角色  =  SMF
                 协商的 QCI/5QI  =  6
          协商的 QoS ARP 优先级  =  1
        协商的 QoS ARP 抢占能力  =  MAY_PREEMPT
      协商的 QoS ARP 被抢占能力  =  NOT_PREEMPTABLE
          协商的 QoS 5QI 优先级  =  1
             协商的上行最大速率  =  NULL
             协商的下行最大速率  =  NULL
           协商的上行保证比特率  =  NULL
           协商的下行保证比特率  =  NULL
   协商的会话 AMBR 上行比特速率  =  1 Kbps
   协商的会话 AMBR 下行比特速率  =  1 Kbps
                   平均窗口大小  =  0
                   最大数据峰值  =  0
从策略而来的反射 QoS 定时器信息  =  0
                 签约的 QoS 5QI  =  6
          签约的 QoS 5QI 优先级  =  1
          签约的 QoS ARP 优先级  =  1
        签约的 QoS ARP 抢占能力  =  MAY_PREEMPT
      签约的 QoS ARP 被抢占能力  =  NOT_PREEMPTABLE
   签约的会话 AMBR 上行比特速率  =  1 Kbps
   签约的会话 AMBR 下行比特速率  =  1 Kbps
                        POD名称  =  sm2-pod-0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示会话QoS信息（DSP-SESSIONQOSINFO）_64343871.md`
