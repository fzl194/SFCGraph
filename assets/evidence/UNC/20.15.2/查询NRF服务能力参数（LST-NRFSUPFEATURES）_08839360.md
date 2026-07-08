# 查询NRF服务能力参数（LST NRFSUPFEATURES）

- [命令功能](#ZH-CN_MMLREF_0000001108839360__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001108839360__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001108839360__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001108839360__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001108839360__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001108839360)

**适用NF：NRF**

该命令用于查询NRF网元特定服务是否携带能力参数。

## [注意事项](#ZH-CN_MMLREF_0000001108839360)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001108839360)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001108839360)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：可选参数<br>参数含义：该参数表示NRF服务类型。选择NFM表示设置NF管理类服务中的订阅功能支持的能力，选择DISC表示设置NF服务发现功能支持的能力。<br>数据来源：本端规划<br>取值范围：<br>- DISC（DISC）<br>- NFM（NFM）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001108839360)

查询NRF服务是否携带能力参数。

```
LST NRFSUPFEATURES:;
%%LST NRFSUPFEATURES:;%%
RETCODE = 0  操作成功

结果如下
------------------------
服务类型    能力参数携带开关                                

NFM         打开                                
DISC        关闭                            
(结果个数 = 2)
```

## [输出结果说明](#ZH-CN_MMLREF_0000001108839360)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 服务类型 | 该参数表示NRF服务类型。选择NFM表示设置NF管理类服务中的订阅功能支持的能力，选择DISC表示设置NF服务发现功能支持的能力。 |
| 能力参数携带开关 | 该参数用于表示NRF向NF的订阅响应、发现响应中是否携带NRF支持的能力参数。该参数设置为“FUNC_OFF”时表示不携带，设置为“FUNC_ON”时表示携带。当SERVICETYPE选择NFM时此开关控制订阅响应，当选择DISC时此开关控制服务发现响应。<br>订阅能力参数包括订阅通知时支持携带service的map格式的参数，详细可参考3GPP 29510协议中的“Features supported by the NFManagement service”；<br>服务发现能力参数包括服务发现结果支持携带service的map格式的参数等，详细可参考3GPP 29510协议中的“Features supported by the NFDiscovery service”。 |
