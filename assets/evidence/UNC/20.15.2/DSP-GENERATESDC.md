# 查询强制产生业务数据容器结果（DSP GENERATESDC）

- [命令功能](#ZH-CN_CONCEPT_0209897026__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897026__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897026__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897026__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897026__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897026__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897026)

**适用NF：SGW-C、PGW-C、SMF**

查询FOC GENERATESDC命令的执行结果。

#### [注意事项](#ZH-CN_CONCEPT_0209897026)

- 该命令执行后立即生效。
- 当前版本不支持此命令。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897026)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897026)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209897026)

查询强制产生业务数据容器结果：

```
DSP GENERATESDC:;
```

```
 
 
Previously Focibly SDC Generation Result 
---------------------------------------- 
                                Time  =  2018-07-16 14:00:00 
 Porcess Online Charging User Number  =  50 
Porcess Offline Charging User Number  =  100 
                              Result  =  success 
(Number of results = 1) 
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897026)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 时间 | 上次强制产生业务数据容器的时间。 |
| 处理的在线计费用户数 | 处理的在线计费用户数。 |
| 处理的离线计费用户数 | 处理的离线计费用户数。 |
| 结果 | 上次强制产生业务数据容器的结果。 |
