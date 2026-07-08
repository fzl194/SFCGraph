# 删除NRF信息（RMV NRF）

- [命令功能](#ZH-CN_MMLREF_0209651366__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651366__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651366__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651366__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651366)

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF**

该命令用于删除NRF实例的信息。

## [注意事项](#ZH-CN_MMLREF_0209651366)

- 该命令执行后立即生效。

- 如果NRF的信息被删除，NF与NRF之间的通信将中断。

#### [操作用户权限](#ZH-CN_MMLREF_0209651366)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651366)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFINSTANCENAME | NRF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：<br>- 本参数的构成字符只能是字母A～Z或a～z、数字0～9和下划线"_"和中划线"-"，例如，NRF_Instance_0。<br>- 不允许配置前18位字符与数据库中所有存储的非UUID格式的NRFINSTANCENAME的相同记录。 |

## [使用实例](#ZH-CN_MMLREF_0209651366)

需要删除名称为NRF_Instance_0的NRF的对应信息。

```
RMV NRF: NRFINSTANCENAME="NRF_Instance_0";
```
