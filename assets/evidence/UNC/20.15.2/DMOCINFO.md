# 显示Diameter流控信息(DSP DMOCINFO)

- [命令功能](#ZH-CN_TOPIC_0000001172226069__1.3.1.1)
- [注意事项](#ZH-CN_TOPIC_0000001172226069__1.3.2.1)
- [本地用户权限](#ZH-CN_TOPIC_0000001172226069__1.3.3.1)
- [网管用户权限](#ZH-CN_TOPIC_0000001172226069__1.3.4.1)
- [参数说明](#ZH-CN_TOPIC_0000001172226069__1.3.5.1)
- [使用实例](#ZH-CN_TOPIC_0000001172226069__1.3.6.1)
- [输出结果说明](#ZH-CN_TOPIC_0000001172226069__1.3.7.1)

#### [命令功能](#ZH-CN_TOPIC_0000001172226069)

**适用网元：SGSN、MME**

此命令用于查询Diameter Overload Indication Conveyance（DOIC）流控信息 。

#### [注意事项](#ZH-CN_TOPIC_0000001172226069)

无。

#### [本地用户权限](#ZH-CN_TOPIC_0000001172226069)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_TOPIC_0000001172226069)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_TOPIC_0000001172226069)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的进程类型。<br>数据来源：整网规划<br>取值范围：<br>- “LCP（LCP进程）”<br>- “SGP（SGP进程）”<br>默认值：<br>“LCP（LCP进程）”<br>配置原则：无 |
| RUNAME | RU名称 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定<br>SPU<br>资源单元名。该参数可以通过<br>[DSP RU](../../../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前提条件：此参数在<br>“进程类型”<br>设置为<br>“SGP（SGP进程）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0~63 位字符串<br>默认值：无<br>配置原则：无 |
| PROCID | 进程号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示查询的目的进程号。<br>前提条件：此参数在<br>“进程类型”<br>设置为<br>“SGP（SGP进程）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：无 |
| QRYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：整网规划<br>取值范围：<br>- “MEMORY（内存）”<br>- “DDB（数据库）”<br>默认值：<br>“MEMORY（内存）”<br>配置原则：无 |
| DMOCTYPE | Diameter流控类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter流控信息类型。<br>数据来源：整网规划<br>取值范围：<br>- “ALL（所有类型）”<br>- “BYHOSTNAME（基于HOSTNAME）”<br>- “BYREALMNAME（基于REALMNAME）”<br>默认值：<br>“ALL（所有类型）”<br>配置原则：无 |
| HOSTNAME | 主机名 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定Diameter流控信息的主机名。<br>数据来源：整网规划<br>前提条件：此参数在<br>“Diameter流控类型”<br>设置为<br>“BYHOSTNAME（基于HOSTNAME）”<br>后生效。<br>取值范围：字符串类型，输入长度范围为0～127。<br>默认值：无<br>配置原则：无 |
| REALMNAME | 域名 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定Diameter流控信息的主机域名。<br>数据来源：整网规划<br>前提条件：此参数在<br>“Diameter流控类型”<br>设置为<br>“BYREALMNAME（基于REALMNAME）”<br>后生效。<br>取值范围：字符串类型，输入长度范围为0～127。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_TOPIC_0000001172226069)

查询LCP进程流控记录信息：

DSP DMOCINFO: PROCTYPE=LCP, DMOCTYPE=ALL;

```
O&M    #1
%%DSP DMOCINFO: PROCTYPE=LCP, DMOCTYPE=ALL;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
                    进程类型  =  LCP进程
                      RU名称  =  LINK_SP_RU_0064
                      进程号  =  0
                    查询类型  =  内存
            Diameter流控类型  =  所有类型
                      主机名  =  NULL
                        域名  =  HSS4301.HUAWEI03.COM.CN
                        索引  =  1
                  OC-Feature  =  默认算法
             Sequence Number  =  0
           Validity Duration  =  60
        Reduction Percentage  =  99
              Overload State  =  流控结束
  最近的Diameter流控启动时间  =  2021-01-10 20:18:10+08:00
  最近的Diameter流控结束时间  =  2021-01-10 20:19:10+08:00
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_TOPIC_0000001172226069)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 进程类型 | 查询出的流控信息的进程类型。 |
| RU名称 | 查询出的SPU资源单元名。 |
| 进程号 | 查询出的流控信息的进程序号。 |
| 查询类型 | 查询出的流控信息的查询类型。 |
| Diameter流控信息类型 | Diameter流控信息类型。 |
| 主机名 | Diameter流控信息的主机名。 |
| 域名 | Diameter流控信息的域名。 |
| 索引 | 对应<br>**ADD DMOC**<br>命令中的“索引”参数。 |
| OC-Feature | Diameter流控算法。 |
| Sequence Number | Diameter流控序列号。 |
| Validity Duration | Diameter流控有效时长。 |
| Reduction Percentage | Diameter流控消息减少概率。 |
| Overload State | Diameter流控状态。 |
| 最近的Diameter流控启动时间 | 最近的Diameter流控启动时间。<br>说明：如果时间是无效值，默认赋值为2000-01-01 00:00:00加上当地对应时区时间，比如中国时区是加8小时，时间为2000-01-01 00:00:00+08:00。 |
| 最近的Diameter流控结束时间 | 最近的Diameter流控结束时间。<br>说明：如果时间是无效值，默认赋值为2000-01-01 00:00:00加上当地对应时区时间，比如中国时区是加8小时，时间为2000-01-01 00:00:00+08:00。 |
