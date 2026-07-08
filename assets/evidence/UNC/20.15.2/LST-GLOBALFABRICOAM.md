# 查询OAM全局配置（LST GLOBALFABRICOAM）

- [命令功能](#ZH-CN_CONCEPT_0192520025__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0192520025__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0192520025__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0192520025__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0192520025__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0192520025__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0192520025)

该命令用于查询全局OAM相关配置：包括OAM使能，OAM报文检测周期，OAM报文超时检测倍数。

#### [注意事项](#ZH-CN_CONCEPT_0192520025)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0192520025)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0192520025)

无。

#### [使用实例](#ZH-CN_CONCEPT_0192520025)

查询全局OAM相关配置：

```
LST GLOBALFABRICOAM:;
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
              OAM使能  =  使能
  OAM报文发送周期（ms） =  200
   OAM报文超时检测倍数  =  15
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0192520025)

参见 [**SET GLOBALFABRICOAM**](设置OAM全局配置（SET GLOBALFABRICOAM）_92520017.md) 的参数说明。
