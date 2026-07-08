# 查询PDN自动探测开关状态（LST PDNAUTOTSTSW）

- [命令功能](#ZH-CN_CONCEPT_0000206312872232__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206312872232__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206312872232__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206312872232__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206312872232__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000206312872232__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206312872232)

**适用NF：PGW-U、UPF**

查询PDN自动探测开关状态。

#### [注意事项](#ZH-CN_CONCEPT_0000206312872232)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206312872232)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206312872232)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000206312872232)

查询PDN自动探测开关状态：

```
LST PDNAUTOTSTSW:;
```

```

RETCODE = 0  Operation succeeded

PDN自动探测开关状态
------------------------
PDN Route Auto Test Switch  =  ENABLE
Dns Kpi Fault Test Switch = ENABLE
Path Fault Tracert Test Switch = ENABLE
(结果个数 = 1)
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000206312872232)

| 输出项名称 | 输出项解释 |
| --- | --- |
| PDN Route Auto Test Switch | PDN路由自动测试开关。 |
| Dns Kpi Fault Test Switch | DNS KPI故障自动探测开关。 |
| Path Fault Tracert Test Switch | 路径故障Tracert开关。 |
