# 删除BSF信息（RMV BSFINFO）

- [命令功能](#ZH-CN_MMLREF_0209652302__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652302__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652302__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652302__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652302)

**适用NF：SMF**

该命令用于删除BSF实例信息。删除BSF后，AF无法选到正确的PCF，导致语音业务受影响。

## [注意事项](#ZH-CN_MMLREF_0209652302)

- 该命令执行后立即生效。

- 当前版本不支持此命令。

#### [操作用户权限](#ZH-CN_MMLREF_0209652302)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652302)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINSTANCENAME | BSF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BSF的实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：<br>该参数需要在ADD NFUUID中事先配置，可执行LST NFUUID进行查看。 |

## [使用实例](#ZH-CN_MMLREF_0209652302)

删除当前配置的某BSF，其实例名称是BSF_Instance_0：

```
RMV BSFINFO: BSFINSTANCENAME="BSF_Instance_0";
```
