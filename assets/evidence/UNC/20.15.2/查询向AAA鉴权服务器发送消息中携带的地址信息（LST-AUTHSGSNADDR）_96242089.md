# 查询向AAA鉴权服务器发送消息中携带的地址信息（LST AUTHSGSNADDR）

- [命令功能](#ZH-CN_MMLREF_0296242089__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296242089__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296242089__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296242089__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0296242089__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0296242089)

**适用NF：PGW-C、SGW-C**

该命令用来查询SPW-C和PGW-C合一形态向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元的配置。

## [注意事项](#ZH-CN_MMLREF_0296242089)

无

#### [操作用户权限](#ZH-CN_MMLREF_0296242089)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0296242089)

无

## [使用实例](#ZH-CN_MMLREF_0296242089)

查询SPW-C和PGW-C向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元的配置 ：

```
%%LST AUTHSGSNADDR:;%%
RETCODE = 0  操作成功

结果如下
--------
3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元中携带的地址信息  =  Pa接口
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0296242089)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元中携带的地址信息 | SPW-C和PGW-C合一形态向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6–Address信元携带的地址信息。 |
