# 设置仲裁服务配置（SET ELECTSERVICE）

- [命令功能](#ZH-CN_CONCEPT_0000001095628124__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001095628124__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001095628124__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001095628124__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001095628124__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001095628124)

![](设置仲裁服务配置（SET ELECTSERVICE）_95628124.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致系统有发生脑裂的风险，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置ETCD仲裁服务的客户端相关配置，包括ETCD仲裁的开关和ETCD灯塔特性的开关。

#### [注意事项](#ZH-CN_CONCEPT_0000001095628124)

- 该命令执行后立即生效。
- 该操作可能使得仲裁服务承载的业务受影响。
- 该命令可以关闭仲裁服务，当仲裁服务关闭时，系统有发生脑裂的风险。
- ETCD灯塔开关使能之后，也需要ETCD服务仲裁开关使能才能实现灯塔功能。
- 开启ETCD灯塔功能，会导致ETCD服务的CPU使用率升高。

- 该命令存在系统初始记录，VNFP的参数的初始设置值如下表：
  | SERVICESWITCH | LIGHTHOUSESWITCH |
  | --- | --- |
  | ENABLE | DISNABLE |

- 该命令存在系统初始记录，LST VNFC命令查询到的VNFC的参数的初始设置值如下表：
  | SERVICESWITCH | LIGHTHOUSESWITCH |
  | --- | --- |
  | ENABLE | ENABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000001095628124)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001095628124)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICESWITCH | 仲裁服务开关配置 | 可选必选说明：可选参数<br>参数含义：该参数用于表示仲裁服务的开关配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：服务去使能。<br>- ENABLE：服务使能。<br>默认值：无<br>配置原则：该参数和可选参数LIGHTHOUSESWITCH需要至少选择一个。 |
| LIGHTHOUSESWITCH | ETCD灯塔开关配置 | 可选必选说明：可选参数<br>参数含义：该参数用于表示ETCD灯塔的开关配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：服务去使能。<br>- ENABLE：服务使能。<br>默认值：无<br>配置原则：该参数和可选参数SERVICESWITCH需要至少选择一个。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001095628124)

打开仲裁服务和ETCD灯塔开关：

```
SET ELECTSERVICE:SERVICESWITCH=ENABLE,LIGHTHOUSESWITCH=ENABLE
,SERVICEINSTANCE="vnfc"
;
```
