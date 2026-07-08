---
id: UNC@20.15.2@MMLCommand@DSP SMFMBSSESSION
type: MMLCommand
name: DSP SMFMBSSESSION（显示MB-SMF会话上下文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMFMBSSESSION
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- MB-SMF组播广播管理
- 显示MB-SMF组播广播会话上下文
status: active
---

# DSP SMFMBSSESSION（显示MB-SMF会话上下文信息）

## 功能

**适用NF：SMF**

该命令用于查询MB-SMF组播广播会话上下文的相关信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- TMGI（TMGI）<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家代码 | 可选必选说明：该参数在"QUERYTYPE"配置为"TMGI"时为条件必选参数。<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。仅支持0-9的数字。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"QUERYTYPE"配置为"TMGI"时为条件必选参数。<br>参数含义：该参数用于指定移动网号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。仅支持0-9的数字。<br>默认值：无<br>配置原则：无 |
| MBSSERVICEID | Mbs Service ID | 可选必选说明：该参数在"QUERYTYPE"配置为"TMGI"时为条件必选参数。<br>参数含义：该参数用于指定Mbs Service ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：<br>Mbs Service ID编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFMBSSESSION]] · MB-SMF组播广播会话（SMFMBSSESSION）

## 使用实例

当需要查询MCC为123，MNC为03，MBSSERVICEID为000001的TMGI广播会话上下文信息时，执行如下命令：

```
%%DSP SMFMBSSESSION: QUERYTYPE=TMGI, MCC="123", MNC="03", MBSSERVICEID="000001";%%
RETCODE = 0  操作成功

结果如下
----------------
                   TMGI  =  123-03-000001
           会话激活时间  =  2022-11-24 16:41:56
            QoSFlow标识  =  1
       5QI的Qos类别标识  =  3
      QoSFlow 5QI优先级  =  NULL
          QoS ARP优先级  =  1
        QoS ARP抢占能力  =  NOT_PREEMPT
      QoS ARP被抢占能力  =  PREEMPTABLE
    QoS最大下行比特速率  =  5 Mbps
QoS可保证的下行比特速率  =  1 Mbps
 会话 AMBR 下行比特速率  =  NULL
           平均窗口大小  =  2000
           最大数据峰值  =  NULL
                请求TAI  =  1230354EFFF;1230300EF36;1230300EF35;12303000003
    AMF服务网络功能标识  =  amf_instance_10
    UPF服务网络功能标识  =  upf_instance_1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示MB-SMF会话上下文信息（DSP-SMFMBSSESSION）_32892345.md`
