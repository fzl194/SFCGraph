# 显示当前NRF实例信息（DSP CURNRFINFO）

- [命令功能](#ZH-CN_MMLREF_0212701646__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0212701646__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0212701646__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0212701646__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0212701646__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0212701646)

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF、CBCF**

显示当前NF对接的NRF实例信息。

## [注意事项](#ZH-CN_MMLREF_0212701646)

无

#### [操作用户权限](#ZH-CN_MMLREF_0212701646)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0212701646)

无

## [使用实例](#ZH-CN_MMLREF_0212701646)

显示当前NF对接的NRF实例信息：

```
%%DSP CURNRFINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
      NRF实例ID  =  NRF_Instance_0
NRF绑定的NF类型  =  non-NRF
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0212701646)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NRF实例ID | 该参数用于指定NRF的实例ID。 |
| NRF绑定的NF类型 | 该参数用于指定NRF的绑定类型。本端为NRF对接的NRF绑定类型为NRF，本端为非NRF对接的NRF绑定类型为NON_NRF。<br>取值说明：<br>- “NRF（NRF）”：NRF类型<br>- “NON_NRF（non-NRF）”：非NRF类型 |
