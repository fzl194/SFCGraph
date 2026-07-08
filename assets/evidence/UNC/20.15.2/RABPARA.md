# 设置RAB参数协商配置(SET RABPARA)

- [命令功能](#ZH-CN_MMLREF_0000001172345827__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345827__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345827__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345827__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345827__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345827__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345827)

**适用网元：SGSN**

此命令用于设置RAB参数协商配置涉及到的参数。在进行RAB指派时，RNC可能会返回因QoS不支持导致的失败的RAB Assignment Response，SGSN需要进行降速率处理，对QoS进行重协商，可协商的Qos参数，分为最大速率、保证速率与最大和保证速率。

#### [注意事项](#ZH-CN_MMLREF_0000001172345827)

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345827)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345827)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345827)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RABPARA | 可协商RAB参数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RAB指配可协商的参数，即SGSN向RNC发送的RAB Assignment Request消息中携带的Alternative RAB Parameter Values信元里包含的可协商速率种类。<br>数据来源：本端规划<br>取值范围：<br>- “MAX_GUARANTEE_BITRATE(最大和保证速率)”<br>- “MAX_BITRATE(最大速率)”<br>- “GUARANTEE_BITRATE(保证速率)”<br>系统初始设置值：MAX_GUARANTEE_BITRATE(最大和保证速率)<br>配置原则：<br>说明：GUARANTEE_BITRATE(保证速率)只在Conversational和Streaming业务中发挥作用。MAX_BITRATE(最大速率)、MAX_GUARANTEE_BITRATE(最大和保证速率)在Conversational、Streaming、Interactive和Background业务中都能发挥作用。 |
| BP | 可选RAB的带宽与初始RAB的带宽的百分比（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定可选RAB的带宽与RAB Assignment Request消息中第一个RAB的带宽的百分比。<br>数据来源：本端规划<br>取值范围：1～99(%)<br>系统初始设置值：50% |
| MUPRABLIST | 上行最大速率协商列表 | 可选必选说明：可选参数<br>参数含义：该参数用于指定降QoS重指配时选择的上行最大速率列表。<br>数据来源：本端规划<br>取值范围：<br>- “BR84M(BR84M)”<br>- “BR48M(BR48M)”<br>- “BR32M(BR32M)”<br>- “BR16M(BR16M)”<br>- “BR12M(BR12M)”<br>- “BR8M(BR8M)”<br>- “BR4M(BR4M)”<br>- “BR2M(BR2M)”<br>- “BR1M(BR1M)”<br>- “BR384K(BR384K)”<br>- “BR256K(BR256K)”<br>- “BR144K(BR144K)”<br>- “BR128K(BR128K)”<br>- “BR64K(BR64K)”<br>- “BR32K(BR32K)”<br>- “BR16K(BR16K)”<br>- “BR8K(BR8K)”<br>系统初始设置值：全部清空<br>配置原则：当<br>[**ADD RNC**](../../../../Iu接口管理/Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md)<br>命令的参数Negotiate RAB QoS值为“support（支持）”及参数Alternative Bitrate Type值为“Value Range”时，建议全部勾选。 |
| MDNRABLIST | 下行最大速率协商列表 | 可选必选说明：可选参数<br>参数含义：该参数用于指定降QoS重指配时选择的下行最大速率协商列表。<br>数据来源：本端规划<br>取值范围：<br>- “BR84M(BR84M)”<br>- “BR48M(BR48M)”<br>- “BR32M(BR32M)”<br>- “BR16M(BR16M)”<br>- “BR12M(BR12M)”<br>- “BR8M(BR8M)”<br>- “BR4M(BR4M)”<br>- “BR2M(BR2M)”<br>- “BR1M(BR1M)”<br>- “BR384K(BR384K)”<br>- “BR256K(BR256K)”<br>- “BR144K(BR144K)”<br>- “BR128K(BR128K)”<br>- “BR64K(BR64K)”<br>- “BR32K(BR32K)”<br>- “BR16K(BR16K)”<br>- “BR8K(BR8K)”<br>系统初始设置值：全部清空<br>配置原则：当<br>[**ADD RNC**](../../../../Iu接口管理/Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md)<br>命令的参数Negotiate RAB QoS值为“support（支持）”及参数Alternative Bitrate Type值为“Value Range”时，建议全部勾选。 |
| GUPRABLIST | 上行保证速率协商列表 | 可选必选说明：可选参数<br>参数含义：该参数用于指定降QoS重指配时选择的上行保证速率协商列表。<br>数据来源：本端规划<br>取值范围：<br>- “BR84M(BR84M)”<br>- “BR48M(BR48M)”<br>- “BR32M(BR32M)”<br>- “BR16M(BR16M)”<br>- “BR12M(BR12M)”<br>- “BR8M(BR8M)”<br>- “BR4M(BR4M)”<br>- “BR2M(BR2M)”<br>- “BR1M(BR1M)”<br>- “BR384K(BR384K)”<br>- “BR256K(BR256K)”<br>- “BR144K(BR144K)”<br>- “BR128K(BR128K)”<br>- “BR64K(BR64K)”<br>- “BR32K(BR32K)”<br>- “BR16K(BR16K)”<br>- “BR8K(BR8K)”<br>系统初始设置值：全部清空<br>配置原则：当<br>[**ADD RNC**](../../../../Iu接口管理/Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md)<br>命令的参数Negotiate RAB QoS值为“support（支持）”及参数Alternative Bitrate Type值为“Value Range”时，建议全部勾选。 |
| GDNRABLIST | 下行保证速率协商列表 | 可选必选说明：可选参数<br>参数含义：该参数用于指定降QoS重指配时选择的下行保证协商速率。<br>数据来源：本端规划<br>取值范围：<br>- “BR84M(BR84M)”<br>- “BR48M(BR48M)”<br>- “BR32M(BR32M)”<br>- “BR16M(BR16M)”<br>- “BR12M(BR12M)”<br>- “BR8M(BR8M)”<br>- “BR4M(BR4M)”<br>- “BR2M(BR2M)”<br>- “BR1M(BR1M)”<br>- “BR384K(BR384K)”<br>- “BR256K(BR256K)”<br>- “BR144K(BR144K)”<br>- “BR128K(BR128K)”<br>- “BR64K(BR64K)”<br>- “BR32K(BR32K)”<br>- “BR16K(BR16K)”<br>- “BR8K(BR8K)”<br>系统初始设置值：全部清空<br>配置原则：当<br>[**ADD RNC**](../../../../Iu接口管理/Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md)<br>命令的参数Negotiate RAB QoS值为“support（支持）”及参数Alternative Bitrate Type值为“Value Range”时，建议全部勾选。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345827)

配置一条RAB参数协商配置记录，可协商RAB参数为Max Guarantee BitRate，可选RAB的带宽与初始RAB的带宽的百分比为50，上行最大速率协商列表为BR32M，下行最大速率协商列表为BR32M，上行保证速率协商列表为BR16M，下行保证速率协商列表为BR16M：

SET RABPARA: RABPARA=MAX_GUARANTEE_BITRATE, BP=50, MUPRABLIST=BR84M-0&BR48M-0&BR32M-1&BR16M-0&BR12M-0&BR8M-0&BR4M-0&BR2M-0&BR1M-0&BR384K-0&BR256K-0&BR144K-0&BR128K-0&BR64K-0&BR32K-0&BR16K-0&BR8K-0, MDNRABLIST=BR84M-0&BR48M-0&BR32M-1&BR16M-0&BR12M-0&BR8M-0&BR4M-0&BR2M-0&BR1M-0&BR384K-0&BR256K-0&BR144K-0&BR128K-0&BR64K-0&BR32K-0&BR16K-0&BR8K-0, GUPRABLIST=BR84M-0&BR48M-0&BR32M-0&BR16M-1&BR12M-0&BR8M-0&BR4M-0&BR2M-0&BR1M-0&BR384K-0&BR256K-0&BR144K-0&BR128K-0&BR64K-0&BR32K-0&BR16K-0&BR8K-0, GDNRABLIST=BR84M-0&BR48M-0&BR32M-0&BR16M-1&BR12M-0&BR8M-0&BR4M-0&BR2M-0&BR1M-0&BR384K-0&BR256K-0&BR144K-0&BR128K-0&BR64K-0&BR32K-0&BR16K-0&BR8K-0;
