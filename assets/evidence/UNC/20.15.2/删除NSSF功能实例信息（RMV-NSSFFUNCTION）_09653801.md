# 删除NSSF功能实例信息（RMV NSSFFUNCTION）

- [命令功能](#ZH-CN_MMLREF_0209653801__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653801__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653801__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653801__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653801)

**适用NF：NSSF**

该命令用于删除NSSF功能实例信息。

## [注意事项](#ZH-CN_MMLREF_0209653801)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209653801)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653801)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NSSF功能实例号 | 可选必选说明：必选参数<br>参数含义：NSSF功能实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653801)

删除NSSF功能实体号为Instanceid01的NSSF功能实例信息。

```
RMV NSSFFUNCTION:INSTANCEID="Instanceid01";
```
