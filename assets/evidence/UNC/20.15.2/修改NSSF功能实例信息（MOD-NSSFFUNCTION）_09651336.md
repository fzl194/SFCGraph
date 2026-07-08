# 修改NSSF功能实例信息（MOD NSSFFUNCTION）

- [命令功能](#ZH-CN_MMLREF_0209651336__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651336__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651336__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651336__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651336)

**适用NF：NSSF**

本命令用于修改NSSF功能实例信息。

## [注意事项](#ZH-CN_MMLREF_0209651336)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209651336)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651336)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NSSF功能实例号 | 可选必选说明：必选参数<br>参数含义：NSSF功能实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| NAME | NSSF功能实例描述 | 可选必选说明：可选参数<br>参数含义：NSSF功能实例描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |
| ADMINSTATE | 管理状态 | 可选必选说明：可选参数<br>参数含义：NSSF功能实例的管理状态。<br>数据来源：本端规划<br>取值范围：<br>- Locked（锁定）<br>- Unlocked（未锁定）<br>- ShuttingDown（关机）<br>默认值：无<br>配置原则：无 |
| OPERATIONSTATE | 运行状态 | 可选必选说明：可选参数<br>参数含义：NSSF功能实例的运行状态。<br>数据来源：本端规划<br>取值范围：<br>- Enabled（运行）<br>- Disabled（不运行）<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：可选参数<br>参数含义：NSSF功能实例的FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209651336)

修改NSSF功能实体号为Instanceid01的NSSF功能实例信息，将NSSF功能实体描述改为nfdescription02，管理状态改为Locked，运行状态改为Enabled，FQDN改为fqdn02，最大切片选择次数修改为101。

```
MOD NSSFFUNCTION:INSTANCEID="Instanceid01",NAME="nfdescription02",ADMINSTATE=Locked,OPERATIONSTATE=Enabled,FQDN="fqdn02";
```
