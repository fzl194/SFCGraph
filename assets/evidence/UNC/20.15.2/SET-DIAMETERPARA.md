# 设置Diameter参数（SET DIAMETERPARA）

- [命令功能](#ZH-CN_CONCEPT_0209897315__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897315__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897315__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897315__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897315__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897315)

**适用NF：PGW-C、SMF**

该命令用于设置是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送。

如果希望UNC在发送携带Destination-Host AVP的消息时，如果直连路径不存在或直连路径故障，尝试通过Destination-Realm来查找路由发送，则可将该参数使能。

#### [注意事项](#ZH-CN_CONCEPT_0209897315)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | REALMBASEROUTE |
| --- | --- |
| 初始值 | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0209897315)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897315)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMBASEROUTE | 基于域名的路由功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897315)

UNC在发送携带Destination-Host AVP的消息时，如果不存在到Destination-Host的直连路径，希望按照Destination-Realm来查找路由发送，则需要使能该功能：

```
SET DIAMETERPARA:REALMBASEROUTE=ENABLE;
```
