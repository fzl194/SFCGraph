# 显示NETCONF代理操作失败信息（DSP NCSPROXYFAILOPER）

- [命令功能](#ZH-CN_CONCEPT_0259036129__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0259036129__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0259036129__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0259036129__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0259036129__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0259036129__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0259036129)

该命令用于NETCONF代理操作失败信息。

#### [注意事项](#ZH-CN_CONCEPT_0259036129)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0259036129)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0259036129)

无。

#### [使用实例](#ZH-CN_CONCEPT_0259036129)

NETCONF代理操作失败信息：

```
DSP NCSPROXYFAILOPER:;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
NETCONF会话ID  =  316
       时间戳  =  2017-10-11, 00:31:09:737
    NLS通道ID  =  5
      NLS名称  =  kk
     错误信息  =  系统正忙，请稍后重试。;MessageId=82
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0259036129)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NETCONF会话ID | NETCONF会话ID。 |
| 时间戳 | 时间戳。 |
| NLS通道ID | NLS通道ID。 |
| NLS名称 | NLS名称。 |
| 错误信息 | 错误信息。 |
