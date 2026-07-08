# 设置对Gy接口的cea消息中的Origin-Host检查开关（SET CEAORIGHOSTCHK）

- [命令功能](#ZH-CN_CONCEPT_0209897240__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897240__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897240__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897240__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897240__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897240)

**适用NF：PGW-C、SMF**

为了实现某运营商的特定需求。该命令用于配置Diameter对Gy接口的cea消息中的Origin-Host检查开关。

#### [注意事项](#ZH-CN_CONCEPT_0209897240)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CEAORIGHOSTCHK |
| --- | --- |
| 初始值 | ENABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0209897240)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897240)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CEAORIGHOSTCHK | 检查Gy的CEA消息中的Origin-Host | 可选必选说明：可选参数<br>参数含义：该参数用于配置UNC是否检查Gy接口CEA消息中的Origin-Host。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：是。<br>- DISABLE：否。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897240)

配置Diameter对Gy接口的cea消息中的Origin-Host检查开关，则可按如下配置：

```
SET CEAORIGHOSTCHK:CEAORIGHOSTCHK=DISABLE;
```
