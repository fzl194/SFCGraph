---
id: UNC@20.15.2@MMLCommand@DSP CPPDPCHGINFO
type: MMLCommand
name: DSP CPPDPCHGINFO（查询计费上下文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CPPDPCHGINFO
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费维护
- 用户计费信息
status: active
---

# DSP CPPDPCHGINFO（查询计费上下文信息）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询用户在内容计费及PDP计费情况下的上下文信息，检查话单信息或CCR消息信息。

## 注意事项

所查询到的用户配额用量为SMF/PGW-C上已收集但未上报的部分。这部分配额用量既不是用户上线以来的总流量，也不是上次上报计费中心以来的总流量，而是上次上报计费中心以后从UPF/PGW-U获取的还未上报计费中心的流量。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIBERID | 用户标识类型 | 可选必选说明：必选参数<br>参数含义：指定需要查询的用户标识类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用户的IMSI号。<br>- MSISDN：用户的MSISDN号。<br>- IPv4：用户的IPv4地址。<br>- IPv6：用户的IPv6地址。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“SUBSCRIBERID”配置为“IMSI”时为必选参数。<br>参数含义：用户的IMSI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：配置IMSI表示查询指定IMSI号的用户的计费信息。 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“SUBSCRIBERID”配置为“MSISDN”时为必选参数。<br>参数含义：用户的MSISDN号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：配置MSISDN表示查询指定的MSISDN号的用户的计费信息。 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SUBSCRIBERID”配置为“IPv4”时为必选参数。<br>参数含义：用户的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：配置IPv4表示查询指定的IPv4地址的用户的计费信息。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SUBSCRIBERID”配置为“IPv6”时为必选参数。<br>参数含义：IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。<br>默认值：无<br>配置原则：配置IPv6表示查询指定的IPv6地址的用户的计费信息。 |
| NSAPI | NSAPI | 可选必选说明：可选参数<br>参数含义：用户的NSAPI号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [计费上下文信息（CPPDPCHGINFO）](configobject/UNC/20.15.2/CPPDPCHGINFO.md)

## 使用实例

查询IMSI号为231011223344551的用户的上下文信息：

```
DSP CPPDPCHGINFO:SUBSCRIBERID=IMSI,IMSI="231011223344551";
```

```

计费上下文信息
-------------------------
Result   =  
                   IMSI = 231011223344551
                 MSISDN = 8613801040011
               IPv4地址 = 192.168.1.1
                  NSAPI = 5
                    APN = huawei
           User profile = huawei
           ChargingType = Prepaid
            CCFH status = 0
                Roaming = Empty
        PDP create time = 2016-03-09 16:01:01
     Last activity time = Empty
     
   Online chargine info:
   --------------------- 
           Rating group = 100
             Service ID = 100
                CC-time = 1000 S
          Total octets  = 1000 B
               Duration = 200 S
         Up-link volume = 0-100 B
       Down-link volume = 0-300 B
             Valid time = 100 S
 Volume quota threshold = 0-200 B
   Time quota threshold = 200 S
  
   Offline charging info:
   --------------------- 
           Rating group = 100
             Service ID = 100
   Time quota mechanism = QCT (10 S)
               Duration = 400 S
         Up-link volume = 100 B
       Down-link volume = 300 B
            Report time = 2016-03-09 16:01:01
      Last charged time = Empty
       Change condition = Threshold
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询计费上下文信息（DSP-CPPDPCHGINFO）_09897010.md`
