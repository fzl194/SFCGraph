# 删除GTP-C接口信息（RMV GTPCINTF）

- [命令功能](#ZH-CN_MMLREF_0209654360__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209654360__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209654360__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209654360__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209654360)

![](删除GTP-C接口信息（RMV GTPCINTF）_09654360.assets/notice_3.0-zh-cn_2.png)

该命令用于删除GTP-C接口，该命令执行后删除指定GTP-C的接口配置，导致该接口与外部通讯异常，可能影响对应业务，请谨慎操作！。

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于删除GTP-C接口信息。

## [注意事项](#ZH-CN_MMLREF_0209654360)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209654360)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209654360)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C接口类型。<br>数据来源：全网规划<br>取值范围：<br>- E_GTPCINTF_ITFS11（S11接口）<br>- E_GTPCINTF_ITFN26（N26接口）<br>- E_GTPCINTF_ITFS5_S（S5-S接口）<br>- E_GTPCINTF_ITFS8_S（S8-S接口）<br>- S5_P_OR_GN（S5-P/GN接口）<br>- S8_P_OR_GP（S8-P/GP接口）<br>- PROXY_SGSN_GP（Proxy SGSN GP接口）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209654360)

删除S11 GTP-C接口:

```
RMV GTPCINTF:INTFTYPE=E_GTPCINTF_ITFS11;
```
