# 查询SMF和UPF时间一致性检测（LST CUSTATECHK）

- [命令功能](#ZH-CN_CONCEPT_0279440357__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0279440357__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0279440357__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0279440357__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0279440357__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0279440357__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0279440357)

**适用NF：UPF**

查询SMF和UPF时间一致性检测参数。

#### [注意事项](#ZH-CN_CONCEPT_0279440357)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0279440357)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0279440357)

无。

#### [使用实例](#ZH-CN_CONCEPT_0279440357)

查询SMF和UPF时间一致性检测参数：

```
%%LST CUSTATECHK:;
```

```
%%
RETCODE = 0  Operation succeeded

Time Inconsistency Between SMF and UPF
--------------------------------------
UTC Time Consistency Check Switch  =  ENABLE
        Detection error threshold  =  1000
           Alarm Report Threshold  =  10
            Alarm Clear Threshold  =  5
(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0279440357)

参见SET CUSTATECHK的参数说明。
