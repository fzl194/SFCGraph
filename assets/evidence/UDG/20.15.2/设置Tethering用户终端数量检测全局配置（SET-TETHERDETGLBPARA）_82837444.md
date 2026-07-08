# 设置Tethering用户终端数量检测全局配置（SET TETHERDETGLBPARA）

- [命令功能](#ZH-CN_CONCEPT_0182837444__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837444__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837444__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837444__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837444__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837444)

**适用NF：PGW-U、UPF**

该命令用来设置Tethering用户终端数量检测全局配置。

#### [注意事项](#ZH-CN_CONCEPT_0182837444)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 此命令的生效范围为整机。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | AGETIME | HOTSPOTAGETIMEPARA | HOTSPOTAGETIME | TTLANTIFRAUD | PCCMAXNUMCHOICE | BWMSUBSCRCTRL | STATISTICMETHOD | UDPFLOWCTRL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 300 | INHERIT | 300 | ENABLE | COMMON_POLICY | ALL_BWM_CONTROL | CONFIG | TETHERING_FLOW |

#### [操作用户权限](#ZH-CN_CONCEPT_0182837444)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837444)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGETIME | Tethering用户终端数量检测缓存节点的老化时间(秒) | 可选必选说明：可选参数<br>参数含义：该参数用来显示Tethering用户终端检测时存储的缓存节点的老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～3600，单位是秒。<br>默认值：无<br>配置原则：取值范围60~3600秒。 |
| HOTSPOTAGETIMEPARA | Tethering用户终端数量检测热点终端缓存节点老化时间配置参数 | 可选必选说明：可选参数<br>参数含义：该参数用来设置Tethering用户终端数量检测时热点终端缓存节点老化时间的配置参数。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：表示Tethering用户热点终端缓存节点的老化时间继承AgeTime的配置值。<br>- USER_DEFINED：表示Tethering用户热点终端缓存节点的老化时间自行配置。<br>默认值：无<br>配置原则：无 |
| HOTSPOTAGETIME | Tethering用户终端数量检测热点终端缓存节点的老化时间(秒) | 可选必选说明：条件必选参数<br>前提条件：该参数在“HOTSPOTAGETIMEPARA”配置为“USER_DEFINED”时为必选参数。<br>参数含义：该参数用来设置Tethering终端数量检测时存储的热点终端节点的老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～3600，单位是秒。<br>默认值：无<br>配置原则：无 |
| TTLANTIFRAUD | TTL防欺诈开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否使能Tethering终端数量检测TTL防欺诈功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）Tethering终端数量检测TTL防欺诈功能。<br>- ENABLE：使能（开启）Tethering终端数量检测TTL防欺诈功能。<br>默认值：无<br>配置原则：无 |
| PCCMAXNUMCHOICE | PCC用户Tethering终端数量检测最大Tethering个数的选择方式 | 可选必选说明：可选参数<br>参数含义：该参数用来设置PCC用户Tethering终端数量检测最大Tethering个数的选择方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- COMMON_POLICY：表示PCC用户进行Tethering检测时最多可检测的终端个数是SMF下发的common-policy对应的UserProfile下配置的TETHERINGMAXNUM参数值。<br>- MAX_VALUE：表示PCC用户进行Tethering检测时最多可检测的终端个数是SMF下发的所有UserProfile下配置的TETHERINGMAXNUM参数的有效最大值，取值范围是0到20。如果没有有效值，则不做Tethering终端个数检测。<br>默认值：无<br>配置原则：无 |
| BWMSUBSCRCTRL | 用户级业务带宽控制选项 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Tethering用户终端数量检测时用户级业务带宽控制器是否使用PCC rule。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL_BWM_CONTROL：表示对于Tethering用户，所有流量都不使用PCC rule中的QoS参数做用户级业务带宽控制，使用BWM Rule中的带宽管理参数做用户带宽控制。<br>- TETHERING_BWM_CONTROL：表示对于Tethering用户，热点流量依据SET BANDWIDTHMNG命令的BWMSUBSCRCTRL参数进行用户级带宽控制，tethering流量不使用PCC rule中的QoS参数做用户级业务带宽控制。<br>- CONFIG：表示对于Tethering用户，所有流量都依据SET BANDWIDTHMNG命令的BWMSUBSCRCTRL参数进行用户级带宽控制。<br>默认值：无<br>配置原则：无 |
| STATISTICMETHOD | Tethering节点统计方式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Tethering用户终端数量检测时每个用户Tethering节点的申请个数控制方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CONFIG：表示每个用户下Tethering节点的最大个数，按照UserProfile下TetheringMaxNum参数配置值加1申请。<br>- ACTUAL_NUM：表示每个用户下Tethering节点的最大个数，按照实际接入的Tethering终端个数申请。<br>默认值：无<br>配置原则：无 |
| UDPFLOWCTRL | UDP流的控制方式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Tethering用户终端数量检测时UDP流的控制方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TETHERING_FLOW：表示识别出的Tethering个数大于USERPROFILE命令的TETHERINGMAXNUM参数时对UDP的Tethering流，统一按照未超规格Tethering策略处理，该策略通过ADD GLBEXTENDPOLICY命令配置。<br>- EXCEED_TETHERING_FLOW：表示识别出的Tethering个数大于USERPROFILE命令的TETHERINGMAXNUM参数时对UDP的Tethering流，统一按照超规格Tethering策略处理，该策略通过ADD GLBEXTENDPOLICY命令配置。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837444)

设置Tethering用户终端数量缓存节点老化时间为100s：

```
SET TETHERDETGLBPARA: AGETIME=100;
```
