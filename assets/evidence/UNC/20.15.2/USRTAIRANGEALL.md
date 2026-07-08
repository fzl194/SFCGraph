# 删除所有的用户TAI区域（RMV USRTAIRANGEALL）

- [命令功能](#ZH-CN_MMLREF_0000001438729357__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001438729357__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001438729357__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001438729357__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001438729357)

![](删除所有的用户TAI区域（RMV USRTAIRANGEALL）_38729357.assets/notice_3.0-zh-cn_2.png)

删除用户TAI区域不当可能导致动态PCC用户无法基于用户TAI区域绑定的业务服务区选择PCF，进而影响用户使用业务。

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除所有的用户TAI区域。

## [注意事项](#ZH-CN_MMLREF_0000001438729357)

- 该命令执行后立即生效。

- 如果用户TAI区域已经与PCF业务服务区绑定，则不允许删除，需要执行命令RMV PCFSSCOPEBIND解除绑定关系后再删除。

#### [操作用户权限](#ZH-CN_MMLREF_0000001438729357)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001438729357)

无

## [使用实例](#ZH-CN_MMLREF_0000001438729357)

删除系统内所有与PCFSSCOPEBIND不存在绑定关系的用户TAI区域。

```
RMV USRTAIRANGEALL:;
```
