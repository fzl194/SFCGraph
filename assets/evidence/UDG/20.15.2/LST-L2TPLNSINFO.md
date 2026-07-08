# 查询L2TP组的LNS信息（LST L2TPLNSINFO）

- [命令功能](#ZH-CN_CONCEPT_0000204661600085__1.3.1.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000204661600085__1.3.2.1)
- [参数说明](#ZH-CN_CONCEPT_0000204661600085__1.3.3.1)
- [使用实例](#ZH-CN_CONCEPT_0000204661600085__1.3.4.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000204661600085__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000204661600085)

**适用NF：PGW-U、UPF**

用于查询L2TP组绑定的LNS信息。

#### [操作用户权限](#ZH-CN_CONCEPT_0000204661600085)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000204661600085)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | L2TP组号 | 可选必选说明：可选参数<br>参数含义：指定L2TP组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1500。<br>默认值：无<br>配置原则：该参数使用ADD L2TPGROUP命令配置生成。 |
| LNSNO | LNS序号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定添加LNS的序号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000204661600085)

查询L2TP组绑定的LNS信息：

```
LST L2TPLNSINFO:;
```

```

RETCODE = 0 操作成功。

RETCODE = 0  Operation succeeded

L2tp Group Lns Info
----------------------
                   L2TP Group ID  =  1
             LNS Sequence Number  =  1
                   Lns IP version = IPV4
                 LNS IPv4 Address = 10.1.1.1
                 LNS IPv6 Address = ::
                     LNS Password = *****
             Confirm LNS Password = *****
(Number of results = 1)

--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000204661600085)

参见ADD L2TPLNSINFO的参数说明。
