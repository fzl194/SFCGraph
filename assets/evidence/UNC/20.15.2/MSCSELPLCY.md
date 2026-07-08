# 设置MSC选择策略(SET MSCSELPLCY)

- [命令功能](#ZH-CN_MMLREF_0000001126305786__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305786__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305786__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305786__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305786__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305786__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305786)

**适用网元：MME**

该命令用于设置SRVCC流程中MSC域名解析策略。MME支持按RAI FQDN或LAI FQDN解析MSC。

#### [注意事项](#ZH-CN_MMLREF_0000001126305786)

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。
- 通过本命令修改Sv接口域名解析策略后，需要在本地或者DNS服务器上配置相应的FQDN记录。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305786)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305786)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305786)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNSPLCY | Sv接口域名解析策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在SRVCC流程中，MME采用RAI还是LAI解析MSC。<br>数据来源：全网规划<br>取值范围：<br>- “LAI（LAI）”<br>- “RAI（RAI）”<br>系统初始设置值：<br>“LAI（LAI）”<br>。<br>配置原则：<br>- 规划SRVCC的DNS解析数据时，建议采用LAI解析MSC，可节省配置工作量。<br>- 如果DNS上的数据已配置为按RAI解析MSC，MME割入网络时，为了保持一致性，本参数需要配置为按RAI解析MSC。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305786)

当DNS已经配置RAI解析MSC，MME割入网络时，为了保持一致性，本参数需要配置为按RAI解析MSC：

SET MSCSELPLCY: DNSPLCY = RAI;

除上述配置RAI场景外，建议在规划SRVCC的DNS解析数据时使用LAI解析MSC：

SET MSCSELPLCY: DNSPLCY = LAI;
