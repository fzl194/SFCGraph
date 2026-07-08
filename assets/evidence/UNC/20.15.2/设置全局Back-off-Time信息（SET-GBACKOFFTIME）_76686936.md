# 设置全局Back-off Time信息（SET GBACKOFFTIME）

- [命令功能](#ZH-CN_MMLREF_0276686936__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0276686936__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0276686936__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0276686936__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0276686936)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置全局的Back-off Time信息。

## [注意事项](#ZH-CN_MMLREF_0276686936)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| BACKOFFTIMER |
| --- |
| 600 |

#### [操作用户权限](#ZH-CN_MMLREF_0276686936)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0276686936)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BACKOFFTIMER | 全局Back-off时长(秒) | 可选必选说明：必选参数<br>参数含义：该参数用于指定全局Back-off时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~3600，单位是秒。<br>默认值：无。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0276686936)

当运营商需要设置全局Back-off Time信息时，配置如下：

```
SET GBACKOFFTIME: BACKOFFTIMER = 600;
```
