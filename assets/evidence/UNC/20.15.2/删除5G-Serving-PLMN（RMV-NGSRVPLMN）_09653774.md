# 删除5G Serving PLMN（RMV NGSRVPLMN）

- [命令功能](#ZH-CN_MMLREF_0209653774__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653774__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653774__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653774__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653774)

![](删除5G Serving PLMN（RMV NGSRVPLMN）_09653774.assets/notice_3.0-zh-cn_2.png)

删除Serving PLMN可能影响AMF给无线侧广播的PLMN信息。

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF**

该命令用于删除指定的Serving PLMN。

## [注意事项](#ZH-CN_MMLREF_0209653774)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209653774)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653774)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNIDX | PLMN索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统内唯一标识一个PLMN。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653774)

为运营商A删除Serving PLMN信息（索引为0），执行如下命令：

```
RMV NGSRVPLMN: PLMNIDX=0;
```
