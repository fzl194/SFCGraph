# 设置NRF服务能力参数（SET NRFSUPFEATURES）

- [命令功能](#ZH-CN_MMLREF_0000001109279254__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001109279254__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001109279254__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001109279254__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001109279254)

**适用NF：NRF**

该命令用于设置NRF网元特定服务是否携带能力参数。

## [注意事项](#ZH-CN_MMLREF_0000001109279254)

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SERVICETYPE | SUPFEATURESSW |
| --- | --- |
| DISC | FUNC_OFF |
| NFM | FUNC_OFF |

#### [操作用户权限](#ZH-CN_MMLREF_0000001109279254)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001109279254)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：该参数表示NRF服务类型。选择NFM表示设置NF管理类服务中的订阅功能支持的能力，选择DISC表示设置NF服务发现功能支持的能力。<br>数据来源：本端规划<br>取值范围：<br>- DISC（DISC）<br>- NFM（NFM）<br>默认值：无。<br>配置原则：无 |
| SUPFEATURESSW | 能力参数携带开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NRF向NF的订阅响应、发现响应中是否携带NRF支持的能力参数。该参数设置为“FUNC_OFF”时表示不携带，设置为“FUNC_ON”时表示携带。当SERVICETYPE选择NFM时此开关控制订阅响应，当选择DISC时此开关控制服务发现响应。<br>订阅能力参数包括订阅通知时支持携带service的map格式的参数，详细可参考3GPP 29510协议中的“Features supported by the NFManagement service”；<br>服务发现能力参数包括服务发现结果支持携带service的map格式的参数等，详细可参考3GPP 29510协议中的“Features supported by the NFDiscovery service”。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001109279254)

设置NRF订阅响应中携带NRF支持的服务能力。

```
SET NRFSUPFEATURES: SERVICETYPE=NFM, SUPFEATURESSW=FUNC_ON;
```
