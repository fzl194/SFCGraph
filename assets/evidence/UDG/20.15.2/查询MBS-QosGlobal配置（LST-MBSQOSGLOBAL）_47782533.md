# 查询MBS QosGlobal配置（LST MBSQOSGLOBAL）

- [命令功能](#ZH-CN_CONCEPT_0000203347782533__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203347782533__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203347782533__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203347782533__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203347782533__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000203347782533__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203347782533)

**适用NF：UPF**

该命令用于查询MBS会话的QOS功能配置。

#### [注意事项](#ZH-CN_CONCEPT_0000203347782533)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203347782533)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203347782533)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000203347782533)

查询MBS会话的QOS功能开关配置：

```
LST MBSQOSGLOBAL:;
```

```

RETCODE = 0  操作成功

MBS整机QoS配置
----------------------------
 MBS QoS 功能开关  =  ENABLE
   MBS QosCar 功能 =  DISABLE
MBS QosShape 功能  =  ENABLE
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000203347782533)

参见SET MBSQOSGLOBAL的参数说明。
