# 查询Qos Profile缺省承载QoS属性（LST EPSQOS4DEFBER）

- [命令功能](#ZH-CN_MMLREF_0000001124796818__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001124796818__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001124796818__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001124796818__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001124796818__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001124796818)

**适用NF：SGW-C、PGW-C**

该命令用来查询Qos Profile缺省承载QoS属性。

## [注意事项](#ZH-CN_MMLREF_0000001124796818)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001124796818)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001124796818)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | Qos Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用来指定Qos Profile名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD QOSPROFILE命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0000001124796818)

查询QosProfileName为“test”的缺省承载Qos属性：

```
%%LST EPSQOS4DEFBER:QOSPROFILENAME="test";%%
RETCODE = 0  操作成功。

缺省承载的QoS配置信息
---------------------
            Qos Profile名  =  test
                    QCI值  =  5
            ARP的优先级别  =  11
下行APN AMBR（千比特/秒）  =  500
上行APN AMBR（千比特/秒）  =  500
(结果个数 = 1)
---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001124796818)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Qos Profile名 | 该参数用来指定Qos Profile名称。 |
| QCI值 | 该参数用来指定QCI。 |
| ARP的优先级别 | 该参数用来指定ARP的优先级。 |
| 下行APN AMBR(千比特/秒) | 该参数用来指定下行集合比特率。 |
| 上行APN AMBR(千比特/秒) | 该参数用来指定上行集合比特率。 |
