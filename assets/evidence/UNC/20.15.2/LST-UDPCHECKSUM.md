# 查询UNC发送的UDP报文是否携带checksum（LST UDPCHECKSUM）

- [命令功能](#ZH-CN_MMLREF_0000001194059550__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001194059550__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001194059550__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001194059550__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001194059550__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001194059550)

**适用NF：PGW-C、GGSN、SMF**

该命令用来查询UNC发送的UDP报文是否携带checksum。

## [注意事项](#ZH-CN_MMLREF_0000001194059550)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001194059550)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001194059550)

无

## [使用实例](#ZH-CN_MMLREF_0000001194059550)

查询UNC发送的UDP报文是否携带checksum：

```
%%LST UDPCHECKSUM:;%%
RETCODE = 0  操作成功

结果如下
--------
    UDP Type = DHCP
Checksum开关 = 不使能   
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001194059550)

| 输出项名称 | 输出项解释 |
| --- | --- |
| UDP Type | 指定是何种类型的报文。 |
| Checksum开关 | 指定UNC发送的UDP报文中是否携带checksum。 |
