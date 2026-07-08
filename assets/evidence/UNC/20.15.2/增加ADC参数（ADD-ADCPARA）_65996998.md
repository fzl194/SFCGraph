# 增加ADC参数（ADD ADCPARA）

- [命令功能](#ZH-CN_CONCEPT_0265996998__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0265996998__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0265996998__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0265996998__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0265996998__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0265996998)

**适用NF：PGW-C、SMF**

该命令用于配置应用的流信息上报开关信息。

流信息的上报功能是指对于需要进行检测上报的应用，在上报应用开始/结束上报时，同时上报当前业务的流信息，便于PCRF/PCF能够获取到应用与流的对应关系，从而可以下发更精确地策略对业务进行控制。

#### [注意事项](#ZH-CN_CONCEPT_0265996998)

- 该命令执行后立即生效。
- 该命令最大记录数为8000。

#### [操作用户权限](#ZH-CN_CONCEPT_0265996998)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0265996998)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置应用对应的流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD FLOWFILTER命令配置生成。 |
| FLOWINFORPT | 流信息上报标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置流信息上报标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不上报流信息。<br>- ENABLE：上报流信息。<br>默认值：DISABLE<br>配置原则：<br>- DISABLE：在向PCRF上报应用开始/结束时，不上报流信息。<br>- ENABLE：在向PCRF上报应用开始/结束时，上报流信息。 |

#### [使用实例](#ZH-CN_CONCEPT_0265996998)

- 假设运营商需要为ADC应用添加流过滤器来匹配和检测出运营商需要的应用但不开启流信息上报功能时，指定流过滤器名称为testflowfiltername：
  ```
  ADD ADCPARA:FLOWFILTERNAME="testflowfiltername";
  ```
- 假设运营商需要为ADC应用添加流过滤器并且开启流信息上报功能时，指定应用对应的流过滤器名称为testflowfiltername：
  ```
  ADD ADCPARA:FLOWFILTERNAME="testflowfiltername",FLOWINFORPT=ENABLE;
  ```
