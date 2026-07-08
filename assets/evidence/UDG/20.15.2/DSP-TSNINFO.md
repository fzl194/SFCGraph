# 显示TSN信息（DSP TSNINFO）

- [命令功能](#ZH-CN_CONCEPT_0000202968723519__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202968723519__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202968723519__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202968723519__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202968723519__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000202968723519__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202968723519)

**适用NF：SGW-U、PGW-U**

用来查看TSN信息。

#### [注意事项](#ZH-CN_CONCEPT_0000202968723519)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202968723519)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202968723519)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000202968723519)

运行该命令，显示当前TSN信息：

```
DSP TSNINFO:;
```

```

RETCODE = 0 操作成功

TSN 信息:
---------------
TSN info  =  
Master TSN      
          NE ID Code Len = 1
              NE ID Code = 16
              NE ID Name = TSN1
               NE Status = Activity
              IP Address = 10.0.0.0
                Recovery = 1
             Create Time = 17:45:58 07/15/2022(MM/DD/YYYY)
             Active Time = 17:45:58 07/15/2022(MM/DD/YYYY)
        Last Update Time = 17:45:58 07/15/2022(MM/DD/YYYY)
(结果个数 = 1)

--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000202968723519)

| 输出项名称 | 输出项解释 |
| --- | --- |
| TSN信息 | 显示TSN的相关信息。 |
