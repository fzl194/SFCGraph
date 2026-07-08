# 删除NRF管理的ProxySMF（RMV NRFPROXYSMF）

- [命令功能](#ZH-CN_MMLREF_0000001823623002__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001823623002__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001823623002__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001823623002__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001823623002)

**适用NF：NRF**

该命令用于删除NRF管理的ProxySMF。

## [注意事项](#ZH-CN_MMLREF_0000001823623002)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001823623002)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001823623002)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示本NRF管理的ProxySMF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001823623002)

删除NF实例标识为Nfinstanceid01的NF的信息。

```
RMV NRFPROXYSMF: NFINSTANCEID="Nfinstanceid01";
```
