# 删除NRF协议参数（RMV NRFPARA）

- [命令功能](#ZH-CN_MMLREF_0209651539__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651539__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651539__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651539__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651539)

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF**

该命令用于删除NRF协议相关的配置信息。

## [注意事项](#ZH-CN_MMLREF_0209651539)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209651539)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651539)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFINSTANCENAME | NRF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：<br>本参数取值与ADD NRF命令中的“NRF实例名称”参数取值保持一致时，关联关系生效。 |

## [使用实例](#ZH-CN_MMLREF_0209651539)

删除实例名为NRF_Instance_0的NRF的参数配置信息。

```
RMV NRFPARA: NRFINSTANCENAME="NRF_Instance_0";
```
