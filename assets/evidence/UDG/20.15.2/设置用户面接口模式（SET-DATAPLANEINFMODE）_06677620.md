# 设置用户面接口模式（SET DATAPLANEINFMODE）

- [命令功能](#ZH-CN_CONCEPT_0000203206677620__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203206677620__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203206677620__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203206677620__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203206677620__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203206677620)

**适用NF：SGW-U、PGW-U、UPF**

![](设置用户面接口模式（SET DATAPLANEINFMODE）_06677620.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置此命令时需要检查当前的POD Type是否是ISU/APU POD，如果不是，不能开启入不转板功能。

设置数据面接口模式，包含的接口类型有：s5-sif，s1-uif，saif，paif，n3if，n9cif，scif，n6。

#### [注意事项](#ZH-CN_CONCEPT_0000203206677620)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 修改此命令前需要删除所有用户。
- 配置此命令时需要检查SET CPTEIDUALLOC配置SWITCH是否是DISABLE，如果不是，不能开启入不转板功能。
- 当有逻辑接口绑定切片时，不能开启入不转板功能。
- 当设置数据面接口模式为Instance后，需要通过DSP IPSUIT命令查询每个IP Suit的逻辑接口配置情况。保证每个IP Suit的逻辑接口配置齐全，否则可能会导致用户激活失败。
- 外部地址分配的后路由用户不支持入不转板。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MODE | ROUTEENHANCEDSW |
| --- | --- | --- |
| 初始值 | Group | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000203206677620)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203206677620)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODE | 模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户面IP模式。<br>数据来源：全网规划<br>取值范围：<br>- Group：组级用户面IP模式。<br>- Instance：ISU POD级用户面IP模式。<br>默认值：无<br>配置原则：无 |
| ROUTEENHANCEDSW | 路由增强功能开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MODE”配置为“Instance”时为可选参数。<br>参数含义：该参数用于指定用户面IP下行路由发布时是否开启增强功能。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：参数取值ENABLE：开启用户面IP下行路由发布的增强功能。参数取值DISABLE：不开启用户面IP下行路由发布的增强功能。 |

#### [使用实例](#ZH-CN_CONCEPT_0000203206677620)

设置数据面接口为ISU POD级用户面IP模式，可以使用该命令设置：

```
SET DATAPLANEINFMODE: MODE=Instance;
```
