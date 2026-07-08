# 查询SCTP端点（LST SCTPENDPOINT）

- [命令功能](#ZH-CN_CONCEPT_0209897324__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897324__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897324__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897324__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897324__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897324__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897324)

**适用NF：PGW-C、SMF**

此命令用于查询SCTP端点。

#### [注意事项](#ZH-CN_CONCEPT_0209897324)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897324)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897324)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENDPOINTNAME | 端点名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897324)

查询SCTP端点：

```
LST SCTPENDPOINT: ENDPOINTNAME="sctp_ep1";
```

```

RETCODE = 0  操作成功

SCTP端点
--------
    端点名称  =  sctp_ep1
      端口号  =  3868
      IP版本  =  IPV4
   IPv4地址1  =  10.1.1.1
   IPv4地址2  =  10.1.1.2
SCTP模板名称  =  sctp_tp1
   IPv6地址2  =  NULL
   IPv6地址1  =  NULL
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897324)

参见ADD SCTPENDPOINT的参数说明。
