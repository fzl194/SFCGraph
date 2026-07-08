# 添加NRF功能实例信息（ADD NRFFUNCTION）

- [命令功能](#ZH-CN_MMLREF_0209652375__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652375__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652375__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652375__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652375)

**适用NF：NRF**

该命令用于添加NRF功能实例信息。

## [注意事项](#ZH-CN_MMLREF_0209652375)

- 该命令执行后立即生效。

- 该命令当前版本仅支持配置1条记录，否则会影响北向功能。

- 最多可输入100条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0209652375)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652375)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NRF功能实体号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示特定NRF功能实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| NAME | NRF功能实体描述 | 可选必选说明：可选参数<br>参数含义：该参数用于表示特定NRF功能实体描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |
| ADMINSTATE | 管理状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示特定NRF功能实体管理状态。<br>数据来源：本端规划<br>取值范围：<br>- Locked（锁定）<br>- Unlocked（未锁定）<br>- ShuttingDown（关机）<br>默认值：Unlocked<br>配置原则：无 |
| OPERATIONSTATE | 运行状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示特定NRF功能实体运行状态。<br>数据来源：本端规划<br>取值范围：<br>- Enabled（运行）<br>- Disabled（不运行）<br>默认值：Enabled<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：可选参数<br>参数含义：该参数用于表示特定NRF功能实体FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652375)

运营商想新增一条NRF功能实体号为Instanceid01,NRF功能实体描述为nfdescription01,管理状态为Locked,运行状态为Enabled,FQDN为fqdn01的NRF功能实例信息：

```
ADD NRFFUNCTION:INSTANCEID="Instanceid01",NAME="nfdescription01",ADMINSTATE=Locked,OPERATIONSTATE=Enabled,FQDN="fqdn01";
```
