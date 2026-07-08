# 查询IMSI和MSISDN号段（LST IMSIMSISDNSEG）

- [命令功能](#ZH-CN_CONCEPT_0209897131__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897131__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897131__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897131__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897131__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897131__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897131)

**适用NF：PGW-C、SMF**

该命令用于查询IMSI/MSISDN号码段。

#### [注意事项](#ZH-CN_CONCEPT_0209897131)

LST IMSIMSISDNSEG时如果显示有%3f表示的是通配符“？”。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897131)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897131)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：如果参数不提供则查询所有IMSI/MSISDN号码段。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897131)

- 查询IMSI和MSISDN号段：
  ```
  LST IMSIMSISDNSEG: SEGMENTNAME="huawei";
  ```
  ```

  RETCODE = 0  操作成功

  IMSI或MSISDN号段信息
  --------------------
  IMSI/MSISDN号段名称  =  huawei
  IMSI/MSISDN号段类型  =  IMSI
       号段起始字符串  =  130
       号段结束字符串  =  139
       通配号段字符串  =  NULL
   锁定IMSIMSISDN号段  =  不使能
  (结果个数 = 1)

  ---    END
  ```
- 查询所有IMSI和MSISDN号段：
  ```
  LST IMSIMSISDNSEG:;
  ```
  ```

  RETCODE = 0  操作成功

  IMSI或MSISDN号段信息
  --------------------
  IMSI/MSISDN号段名称  =  huawei
  IMSI/MSISDN号段类型  =  IMSI
       号段起始字符串  =  130
       号段结束字符串  =  139
       通配号段字符串  =  NULL
   锁定IMSIMSISDN号段  =  不使能
  (结果个数 = 1)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897131)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 锁定IMSIMSISDN号段 | 用于锁定或解锁标识。当IMSI/MSISDN号码段锁定后，后续该IMSI/MSISDN号码段内的用户会激活失败，已经在线的用户无影响。通过LCK IMSIMSISDNSEG配置。 |

其余输出项请参见ADD IMSIMSISDNSEG的参数说明。
