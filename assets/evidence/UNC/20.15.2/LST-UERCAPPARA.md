# 查询UE Radio Capability信元参数（LST UERCAPPARA）

- [命令功能](#ZH-CN_CONCEPT_0000001725069542__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001725069542__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001725069542__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001725069542__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001725069542__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001725069542__1.3.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001725069542__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001725069542)

**适用网元：SGSN、MME**

该命令用于查看UE无线能力的告警阈值。

#### [注意事项](#ZH-CN_CONCEPT_0000001725069542)

该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001725069542)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001725069542)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001725069542)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000001725069542)

查询UE Radio Capability信元参数 “上报告警百分比” ；

LST UERCAPPARA:;

```
%%LST UERCAPPARA:;%% 
RETCODE = 0  操作成功  
查询结果如下 
------------ 
上报告警百分比  =  95 
(结果个数 = 1)  
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001725069542)

请参考 [**SET UERCAPPARA**](设置UE Radio Capability信元参数（SET UERCAPPARA）_72749349.md) 命令的参数标识。
