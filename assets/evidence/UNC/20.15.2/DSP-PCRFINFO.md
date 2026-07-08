# 显示PCRF具体信息（DSP PCRFINFO）

- [命令功能](#ZH-CN_CONCEPT_0209897072__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897072__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897072__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897072__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897072__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897072__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897072)

**适用NF：PGW-C、GGSN**

该命令用于查询指定PCRF的详细信息，包括主机名、域名、地址以及supported features协商结果等。

#### [注意事项](#ZH-CN_CONCEPT_0209897072)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897072)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897072)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定被查询的PCRF主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897072)

查询主机名为“pcrf1”的PCRF详细信息：

```
DSP PCRFINFO:HOSTNAME="pcrf1";
```

```

RETCODE = 0  操作成功

PCRF具体信息
------------
结果  =  
Pcrf config information
-----------------------
                           host = pcrf1
                          realm = www.huawei.com
                           dscp = 255
                            wal = 0
                            vpn = vpn1
 supported features negotiation = DISABLE
                 feature config = rel8 
     feature negotiation result = NULL
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897072)

| 输出项名称 | 输出项解释 |
| --- | --- |
| host | PCRF主机名。 |
| realm | 域名。 |
| ip | IP地址。 |
| port | 端口号。 |
| sctp-endpoint | SCTP端点名。 |
| supported features negotiation | Supported features协商开关。 |
| feature config | 配置的feature。 |
| feature negotiation result | feature协商结果。 |
| wal | PCRF的流控阈值。 |
| dscp | PCC信令报文的DSCP值。 |
