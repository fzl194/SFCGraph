# 删除所有的PCF业务服务区的绑定关系（RMV PCFSSCOPEBINDALL）

- [命令功能](#ZH-CN_MMLREF_0000001438569369__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001438569369__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001438569369__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001438569369__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001438569369)

![](删除所有的PCF业务服务区的绑定关系（RMV PCFSSCOPEBINDALL）_38569369.assets/notice_3.0-zh-cn_2.png)

删除PCF业务服务区的绑定关系不当，可能导致基于业务服务区选择的PCF不符合预期，进而影响用户使用业务。

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除所有的PCF业务服务区的绑定关系。

## [注意事项](#ZH-CN_MMLREF_0000001438569369)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001438569369)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001438569369)

无

## [使用实例](#ZH-CN_MMLREF_0000001438569369)

删除PCFSSCOPEBIND的所有配置。

```
RMV PCFSSCOPEBINDALL:;
```
