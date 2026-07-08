# 删除NSSF功能实例服务（RMV NSSFSERVICELIST）

- [命令功能](#ZH-CN_MMLREF_0209653059__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653059__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653059__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653059__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653059)

**适用NF：NSSF**

本命令用于删除NSSF功能实体服务列表。

## [注意事项](#ZH-CN_MMLREF_0209653059)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209653059)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653059)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：NSSF服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~65。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653059)

删除NSSF实例服务名称：

```
RMV NSSFSERVICELIST:SERVICENAME="NSSF-SERVICENAME001";
```
