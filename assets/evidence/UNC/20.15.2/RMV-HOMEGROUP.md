# 删除Home Group（RMV HOMEGROUP）

- [命令功能](#ZH-CN_MMLREF_0000001188733227__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001188733227__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001188733227__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001188733227__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001188733227)

![](删除Home Group（RMV HOMEGROUP）_88733227.assets/notice_3.0-zh-cn_2.png)

执行不当会导致系统异常。

**适用NF：PGW-C、GGSN**

该命令用于删除Home Group配置。

## [注意事项](#ZH-CN_MMLREF_0000001188733227)

- 该命令执行后立即生效。

- HOEMNGROUPINDX不输入时表示删除所有的记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001188733227)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001188733227)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOMEGROUPINDX | Home Group编号 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Home Group的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001188733227)

删除“Home Group编号”为“2”的Home Group配置：

```
RMV HOMEGROUP: HOMEGROUPINDX=2, CONFIRM=Y;
```
