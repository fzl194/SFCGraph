# 修改QoS属性（MOD QOSPROP）

- [命令功能](#ZH-CN_CONCEPT_0209897164__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897164__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897164__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897164__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897164__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897164)

**适用NF：PGW-C、SMF**

该命令是用来修改PCC预定义规则的QoS参数。

#### [注意事项](#ZH-CN_CONCEPT_0209897164)

- 该命令执行后立即生效。
- 修改QoS属性，执行MOD QOSPROP命令前，需要确定修改记录是否存在，存在才能修改记录，否则修改失败。
- 若QosType参数值为QOS_L2_PARA的记录已被ADD L2RULE命令引用，则不允许将QosType参数值修改为QOS_BEARER_PARA和QOS_FLOW_PARA，否则修改失败。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897164)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897164)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROPNAME | QoS属性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| QCIVALUE | QoS等级标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QOSTYPE”配置为“QOS_BEARER_PARA”时为可选参数。<br>参数含义：配置QCI，不同的QCI的业务流需使用不同的承载。QCI带宽保障类型通过配置ADD STDQOSID和ADD EXTENDQCIMAP判断，对于NonGBR类型的QCI如果配置了GBR值，GBR值在业务处理中不生效。该参数4/5G时有效，3G时可配置但不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：无 |
| ARPVALUE | 分配保留优先级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QOSTYPE”配置为“QOS_FLOW_PARA”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“QOSTYPE”配置为“QOS_BEARER_PARA” 或 “QOS_L2_PARA”时为可选参数。<br>参数含义：数值越高优先级越低。当资源限制时根据这个参数决定是否允许用户的二次激活。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～15。<br>默认值：无<br>配置原则：无 |
| EMPCAP | QoS抢占能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个业务是否可以抢占已经分配给其他低优先级业务流的资源的能力。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：<br>- ENABLE：表示可以被高优先级业务抢占资源。<br>- DISABLE：表示不能被高优先级业务抢占资源。 |
| EMPVUL | QoS被抢占设置 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个业务流是否可以被高优先级业务抢占。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：<br>- ENABLE：表示可以被高优先级业务抢占资源。<br>- DISABLE：表示不能被高优先级业务抢占资源。 |
| GBRUPLKVALUE | 保证的上行比特率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定上行保证带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| GBRDNLKVALUE | 保证的下行比特率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下行保证带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| MBRUPLKVALUE | 最大上行比特率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定上行最大带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| MBRDNLKVALUE | 最大下行比特率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下行最大带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| QOSTYPE | QoS属性类型 | 可选必选说明：可选参数<br>参数含义：5G/4G下分别配置5QI和QCI。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- QOS_BEARER_PARA：承载级别的QoS参数。<br>- QOS_FLOW_PARA：流级QoS参数。<br>- QOS_L2_PARA：层二QoS参数。<br>默认值：无<br>配置原则：无 |
| FQI | 5G QoS标识 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QOSTYPE”配置为“QOS_FLOW_PARA”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“QOSTYPE”配置为“QOS_L2_PARA”时为可选参数。<br>参数含义：配置5QI，不同的5QI的业务流需使用不同的承载。5QI带宽保障类型通过配置ADD STDQOSID和ADD EXTENDQCIMAP判断，对于NonGBR类型的5QI如果配置了GBR值，GBR值在业务处理中不生效。该参数4/5G时有效，3G时可配置但不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：无 |
| RQI | 反射QoS指示 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QOSTYPE”配置为“QOS_FLOW_PARA”时为可选参数。<br>参数含义：配置反射QoS标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| QOSURRNAME | QoS使用量上报规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QOSTYPE”配置为“QOS_BEARER_PARA” 或 “QOS_FLOW_PARA”时为可选参数。<br>参数含义：该参数用于设置QoS URR名称，如果不设置此参数，业务触发承载创建则无法感知。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD URR命令配置生成。<br>- 输入单空格将删除该参数已有配置项。<br>- 设置的QOSURRNAME必须是系统已经存在的QoS URR名称。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897164)

修改名称为“test”的QoS属性，QoS等级标识为4，分配保留优先级为1，QoS抢占能力为ENABLE，QoS被抢占设置为ENABLE，保证的上行比特率为10，保证的下行比特率为1000，最大上行比特率为20，最大下行比特率为2000命令为：

```
MOD QOSPROP: QOSPROPNAME="test", EMPCAP=ENABLE, EMPVUL=ENABLE, GBRUPLKVALUE=10, GBRDNLKVALUE=1000, MBRUPLKVALUE=20, MBRDNLKVALUE=2000, QOSTYPE=QOS_BEARER_PARA, QCIVALUE=4, ARPVALUE=1;
```
