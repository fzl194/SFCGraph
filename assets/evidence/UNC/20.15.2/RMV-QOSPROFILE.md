# 删除QoS描述配置（RMV QOSPROFILE）

- [命令功能](#ZH-CN_MMLREF_0209653062__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653062__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653062__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653062__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653062)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除QosProfile的配置信息。

## [注意事项](#ZH-CN_MMLREF_0209653062)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209653062)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653062)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoSProfile名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数不能和命令SET QOSGLOBAL的QosProfileName重复。 |

## [使用实例](#ZH-CN_MMLREF_0209653062)

删除QosProfile名字为test的配置信息：

```
RMV QOSPROFILE:QOSPROFILENAME="test";
```
