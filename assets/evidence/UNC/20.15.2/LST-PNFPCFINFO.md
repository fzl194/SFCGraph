# 查询对端PCF信息（LST PNFPCFINFO）

- [命令功能](#ZH-CN_MMLREF_0209653010__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653010__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653010__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653010__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653010__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653010)

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询本地配置的对端PCF实例信息。

## [注意事项](#ZH-CN_MMLREF_0209653010)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653010)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653010)

无

## [使用实例](#ZH-CN_MMLREF_0209653010)

查询对端PCF信息。

```
%%LST PNFPCFINFO:;%%
RETCODE = 0 操作成功

结果如下
--------
          NF实例标识 = pcf_instance_0
Rx接口Diameter主机名 = huawei.com
  Rx接口Diameter域名 = huawei.com
（结果个数 = 1）

----    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209653010)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF实例标识 | 该参数用于指定NF实例标识。 |
| Rx接口Diameter主机名 | 该参数用于指定Rx接口Diameter主机名。 |
| Rx接口Diameter域名 | 该参数用于指定Rx接口Diameter域名。 |
