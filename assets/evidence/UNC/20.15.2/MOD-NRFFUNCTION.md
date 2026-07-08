# 修改NRF功能实例信息（MOD NRFFUNCTION）

- [命令功能](#ZH-CN_MMLREF_0209654376__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209654376__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209654376__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209654376__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209654376)

**适用NF：NRF**

该命令用于修改NRF功能实例基本信息。

## [注意事项](#ZH-CN_MMLREF_0209654376)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209654376)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209654376)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NRF功能实体号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示特定NRF功能实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| NAME | NRF功能实体描述 | 可选必选说明：可选参数<br>参数含义：该参数用于表示特定NRF功能实体描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |
| ADMINSTATE | 管理状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示特定NRF功能实体管理状态。<br>数据来源：本端规划<br>取值范围：<br>- Locked（锁定）<br>- Unlocked（未锁定）<br>- ShuttingDown（关机）<br>默认值：无<br>配置原则：无 |
| OPERATIONSTATE | 运行状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示特定NRF功能实体运行状态。<br>数据来源：本端规划<br>取值范围：<br>- Enabled（运行）<br>- Disabled（不运行）<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：可选参数<br>参数含义：该参数用于表示特定NRF功能实体FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209654376)

运营商想修改一条NRF功能实体号为Instanceid01的NRF功能实例信息。将其NRF功能实体描述修改为nfdescription02,管理状态修改为Locked,运行状态修改为Enabled,FQDN修改为fqdn02:

```
MOD NRFFUNCTION:INSTANCEID="Instanceid01",NAME="nfdescription02",ADMINSTATE=Locked,OPERATIONSTATE=Enabled,FQDN="fqdn02":
```
