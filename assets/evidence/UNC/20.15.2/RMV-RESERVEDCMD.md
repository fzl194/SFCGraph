# 删除补丁预留配置（RMV RESERVEDCMD）

- [命令功能](#ZH-CN_MMLREF_0250558747__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0250558747__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0250558747__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0250558747__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0250558747)

**适用NF：AMF、SMF、NRF、SGSN、MME、SGW-C、GGSN、PGW-C、SMSF、NCG、NSSF**

删除补丁预留配置。

## [注意事项](#ZH-CN_MMLREF_0250558747)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0250558747)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0250558747)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMDNAME | 功能名称 | 可选必选说明：必选参数<br>参数含义：功能名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0250558747)

删除补丁预留配置，其中功能名称为BALCKLIST，请运行以下命令：

```
RMV RESERVEDCMD: CMDNAME="BALCKLIST";
```
