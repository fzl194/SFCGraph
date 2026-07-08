# 查看NRF功能实体服务列表（LST NRFSERVICENAME）

- [命令功能](#ZH-CN_MMLREF_0209653039__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653039__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653039__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653039__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653039__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653039)

**适用NF：NRF**

该命令用于查看NRF功能实体服务列表。

## [注意事项](#ZH-CN_MMLREF_0209653039)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653039)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653039)

无

## [使用实例](#ZH-CN_MMLREF_0209653039)

查询NRF功能实体服务列表：

```
LST NRFSERVICENAME:;
%%LST NRFSERVICENAME:;%%
RETCODE = 0  执行成功

操作结果如下:
-------------------------
NRF服务名称      

nrf-servcename001  
nrf-servcename002
nrf-servcename003
(结果个数 = 3)
```

## [输出结果说明](#ZH-CN_MMLREF_0209653039)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NRF服务名称 | 该参数用于表示特定NRF功能实例的服务名称。 |
