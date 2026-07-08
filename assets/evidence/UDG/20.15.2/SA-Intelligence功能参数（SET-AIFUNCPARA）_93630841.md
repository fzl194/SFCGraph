# SA Intelligence功能参数（SET AIFUNCPARA）

- [命令功能](#ZH-CN_CONCEPT_0000201793630841__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201793630841__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201793630841__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201793630841__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201793630841__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201793630841)

**适用NF：PGW-U、UPF**

该命令用于设置SA intelligence功能参数。

#### [注意事项](#ZH-CN_CONCEPT_0000201793630841)

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 欺诈、物联网、重定向、百万级规则流量不支持intelligence能耗优化功能。
- SA协议解析加速功能只恢复域名。所有需要解析URL或其他七层字段的内容或位置的流程，不使能SA协议解析加速功能。
- 使用前提：基于IP+Port+L34 Protocol的端点识别技术，也就是在特定时间段内，基于服务器三元组或服务器地址可以唯一确定该业务流所提供的服务，也就是代表intelligence加速的三元组基于intelligence学习到的唯一确定的识别和解析结果（host）进行处理。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SAAIENABLER | AICHKSAMPLERAT | AICHKFLOWNUM | AICHKVALIDRAT | PARSERACCSW |
| --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | 0 | 2000 | 9900 | ENABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000201793630841)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201793630841)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SAAIENABLER | SA Intelligence功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否开启SA intelligence功能。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| AICHKSAMPLERAT | Intelligence验证流的抽样率 | 可选必选说明：可选参数<br>参数含义：该参数用于配置SA性能优化库校验功能的流抽样率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～10000，单位是万分之一。<br>默认值：无<br>配置原则：该校验功能是可选功能。该值如果配置过大会降低intelligence能耗优化流量比例，影响优化效果。如果配置过小，会影响SA性能优化库校验功能准确性。建议配置为100～300。 |
| AICHKFLOWNUM | Intelligence验证流数 | 可选必选说明：可选参数<br>参数含义：该参数用于配置SA性能优化库校验功能的有效流数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为500～20000，单位是个。<br>默认值：无<br>配置原则：无 |
| AICHKVALIDRAT | Intelligence验证流的有效率 | 可选必选说明：可选参数<br>参数含义：该参数用于配置SA性能优化库校验功能的有效比率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5000～10000，单位是万分之一。<br>默认值：无<br>配置原则：无 |
| PARSERACCSW | SA协议解析加速开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否开启SA协议解析intelligence能耗优化功能。当intelligence训练开关开启时，该字段生效。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000201793630841)

如设置支持SA intelligence功能，命令如下：

```
SET AIFUNCPARA: SAAIENABLER=ENABLE, AICHKSAMPLERAT=100, AICHKFLOWNUM=500, AICHKVALIDRAT=9800;
```
