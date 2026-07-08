# 删除Pre-R8 QoS控制动作配置（RMV PRER8QOSACTION）

- [命令功能](#ZH-CN_MMLREF_0209654419__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209654419__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209654419__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209654419__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209654419)

**适用NF：GGSN**

该命令用于删除QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

## [注意事项](#ZH-CN_MMLREF_0209654419)

该命令执行后只对新激活用户生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209654419)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209654419)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>QOSPROFILENAME字段值必须先在QOSPROFILE或QOSGLOBAL对象中添加成功。 |
| TRAFFICCLASS | 业务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务类型。<br>数据来源：本端规划<br>取值范围：<br>- “CONVERSATIONAL（会话类）”：表示用户签约信息中业务类型的级别为会话层面，优先级高。<br>- “STREAMING（流媒体类）”：表示用户签约信息中业务类型的级别为流媒体层面。<br>- “INTERACTIVE（交互类）”：表示用户签约信息中业务类型的级别为交互层面。<br>- “BACKGROUND（后台类）”：表示用户签约信息中业务类型的级别为后台层面。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209654419)

删除“QOSPROFILENAME”为“test”的上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作：

```
RMV PRER8QOSACTION:QOSPROFILENAME="test",TRAFFICCLASS=CONVERSATIONAL;
```
