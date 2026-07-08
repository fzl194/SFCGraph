# 激活NF上线（ACT NFONLINE）

- [命令功能](#ZH-CN_MMLREF_0209652569__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652569__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652569__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652569__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652569)

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用来激活NF向NRF注册。在完成NF相关基础数据配置后，可以通过本命令手动触发NF到NRF的注册。也可以在NF注册、或者配置数据更新异常的情况下，通过本命令重新手动触发NF到NRF的重新上线注册。

## [注意事项](#ZH-CN_MMLREF_0209652569)

- 该命令执行后立即生效。

- 执行该命令无法切换注册的NRF，请使用DWORD2 BIT8切换到主用NRF注册。

#### [操作用户权限](#ZH-CN_MMLREF_0209652569)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652569)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFPROFILE命令中的NFINSTANCENAME值保持一致。NFINSTANCENAME值可通过LST NFPROFILE获得。 |

## [使用实例](#ZH-CN_MMLREF_0209652569)

激活AMF_Instance_0向NRF的注册。

```
ACT NFONLINE: NFINSTANCENAME="AMF_Instance_0";
```
