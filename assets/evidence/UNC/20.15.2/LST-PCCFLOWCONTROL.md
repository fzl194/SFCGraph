# 查询PCC流控配置（LST PCCFLOWCONTROL）

- [命令功能](#ZH-CN_CONCEPT_0000201134160974__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201134160974__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201134160974__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201134160974__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201134160974__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000201134160974__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201134160974)

**适用NF：PGW-C、SMF**

此命令用于查询UNC重授权请求的消息发送速率和SMF接收PCF的Npcf_SMPolicyControl_UpdateNotify消息的速率。

#### [注意事项](#ZH-CN_CONCEPT_0000201134160974)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201134160974)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201134160974)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000201134160974)

查询PCC流控配置：

```
LST PCCFLOWCONTROL:;
```

```

RETCODE = 0  操作成功

PCC流控配置参数
---------------
Revalidation发送速率  =  25
UpdateNotify消息接收速率 = 2000
TerminateNotify消息接收速率 = 2000
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000201134160974)

参见SET PCCFLOWCONTROL的参数说明。
