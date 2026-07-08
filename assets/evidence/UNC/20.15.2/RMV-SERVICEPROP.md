# 删除业务属性（RMV SERVICEPROP）

- [命令功能](#ZH-CN_CONCEPT_0209897170__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897170__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897170__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897170__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897170__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897170)

**适用NF：PGW-C、SMF**

该命令用于删除业务属性。

#### [注意事项](#ZH-CN_CONCEPT_0209897170)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897170)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897170)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTYPE | 操作类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务属性的操作类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SRV_PROP_NAME：删除SRVPROPNAME。<br>- SERVICE_ID：删除SERVICEID。<br>默认值：无<br>配置原则：无 |
| SRVPROPNAME | 业务属性名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OPTYPE”配置为“SRV_PROP_NAME”时为必选参数。<br>参数含义：该参数用于指定业务属性名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SERVICEID | 业务标识 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OPTYPE”配置为“SERVICE_ID”时为必选参数。<br>参数含义：该参数用于指定业务标识。全局唯一。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897170)

删除业务属性配置：OPTYPE为SRV_PROP_NAME，SRVPROPNAME为test：

```
RMV SERVICEPROP:OPTYPE=SRV_PROP_NAME,SRVPROPNAME="test";
```
