# 删除自动扩缩容监测的虚机资源（RMV SCALELOADMON）

- [命令功能](#ZH-CN_MMLREF_0000001924015948__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001924015948__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001924015948__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001924015948__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001924015948)

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于自动扩缩容场景下，关闭指定虚机资源的负载监测。

## [注意事项](#ZH-CN_MMLREF_0000001924015948)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001924015948)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001924015948)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOADCATEGORY | 自动扩缩容上报资源种类 | 可选必选说明：必选参数<br>参数含义：该参数用于指定自动扩缩容上报资源种类。<br>数据来源：本端规划<br>取值范围：<br>- SMSESSIONLOAD（sm-pod的会话资源）<br>- AMUSERLOAD（usn-pod的5G用户资源）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001924015948)

删除一种会话类型的自动扩缩容检测项，执行如下命令：

```
%%RMV SCALELOADMON: LOADCATEGORY=SMSESSIONLOAD;%%
RETCODE = 0  Operation succeeded
```
