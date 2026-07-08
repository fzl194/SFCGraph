---
id: UNC@20.15.2@MMLCommand@DSP SESSIONSUBDATA
type: MMLCommand
name: DSP SESSIONSUBDATA（显示会话签约信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SESSIONSUBDATA
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
- 查询会话签约信息
status: active
---

# DSP SESSIONSUBDATA（显示会话签约信息）

## 功能

**适用NF：SMF**

该命令用于查询5G会话上下文签约信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（用户IMSI号）<br>- MSISDN（用户MSISDN号）<br>默认值：无<br>配置原则：无 |
| IMSI | 国际移动用户标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定用户永久标识或者国际移动用户标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>可以通过DSP PDUSESSION简单查询获取IMSI后作为查询的输入参数。 |
| MSISDN | 移动台国际ISDN号码 | 可选必选说明：该参数在"QUERYTYPE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定一般公共订阅标识或移动台国际 ISDN 号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：<br>可以通过DSP PDUSESSION简单查询获取MSISDN后作为查询的输入参数。 |
| DNN | 签约的 DNN | 可选必选说明：该参数在"QUERYTYPE"配置为"IMSI"、"MSISDN"时为条件可选参数。<br>参数含义：该参数用于表示签约的 DNN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。区分大小写。<br>默认值：无<br>配置原则：<br>可以通过DSP PDUSESSION简单查询获取ReqApn后作为查询的输入参数。 |

## 操作的配置对象

- [会话签约信息（SESSIONSUBDATA）](configobject/UNC/20.15.2/SESSIONSUBDATA.md)

## 使用实例

查询类型为IMSI，IMSI为123031100100001的会话签约信息：

```
%%DSP SESSIONSUBDATA: QUERYTYPE=IMSI, IMSI="123038700100001";%%
RETCODE = 0  操作成功

Session Sub Data
----------------
            国际移动用户标识  =  123038700100001
          移动台国际ISDN号码  =  8613587000001
                  签约的 DNN  =  huawei.com
签约的会话 AMBR 上行比特速率  =  1 Kbps
签约的会话 AMBR 下行比特速率  =  1 Kbps
              签约的 QoS 5QI  =  6
       签约的 QoS 5QI 优先级  =  1
       签约的 QoS ARP 优先级  =  1
     签约的 QoS ARP 抢占能力  =  MAY_PREEMPT
   签约的 QoS ARP 被抢占能力  =  NOT_PREEMPTABLE
                默认会话类型  =  IPv4
            签约允许会话类型  =  IPv6 IPv4v6
        签约的固定 IPv4 地址  =  NULL
        签约的固定 IPv6 地址  =  NULL
      签约的固定IPv6地址前缀  =  NULL
              签约的计费特征  =  1111
              完整性保护指示  =  优选
                加密保护指示  =  优选
          UDM Bypass状态标记  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示会话签约信息（DSP-SESSIONSUBDATA）_64343872.md`
