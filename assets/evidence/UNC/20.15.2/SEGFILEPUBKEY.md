# 查询号段配置文件的签名验证公钥（LST SEGFILEPUBKEY）

- [命令功能](#ZH-CN_MMLREF_0209653001__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653001__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653001__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653001__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653001__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653001)

**适用NF：NRF**

该命令用于查询号段配置文件的签名验证公钥。

## [注意事项](#ZH-CN_MMLREF_0209653001)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653001)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653001)

无

## [使用实例](#ZH-CN_MMLREF_0209653001)

查询号段配置文件签名验证公钥信息：

```
LST SEGFILEPUBKEY:;
%%LST SEGFILEPUBKEY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
公钥名称  =  keyname001
公钥信息  =  -----BEGIN PUBLIC KEY-----#MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsog/61GMt1h6iePkMilD#L7PUuZ41aI8swe/aJAUMlDORsGkoOvkUxRZitBccUr/5yThXb1el5TSUpibGCbEj#YWJmpPSbTQzOQUKTYHwB3Ex23Qo5C3ByeN9HgzUKZMghNeHw5IUIKU/9PKp34bVX#/If2u4q+bPrGqFZ7Uqf/HM2eD8LR2POVSgyngNDCKt5MI5DVx4Kj5JmdaZHmJppD#/72qzxLXdJGH79z3M/Z2MtJ7jp4ZEi+MtOnyqx7Tvrm3A/9bWRghDCLUjxKzHvbi#NTVrf8QDpO2J1FkMmsTBsLJAHyA+rCB11J9OFCObF5HaS6ZqKrOz/FD/mAsLZZi7#gwIDAQAB#-----END PUBLIC KEY-----#
(结果个数 = 1)
```

## [输出结果说明](#ZH-CN_MMLREF_0209653001)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 公钥名称 | 该参数用于表示在NRF上配置的号段配置文件的签名验证公钥名称。 |
| 公钥信息 | 该参数用于表示在NRF上配置的公钥内容。 |
