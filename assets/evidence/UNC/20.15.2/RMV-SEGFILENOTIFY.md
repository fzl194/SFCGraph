# 删除号段文件通知记录（RMV SEGFILENOTIFY）

- [命令功能](#ZH-CN_MMLREF_0250738961__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0250738961__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0250738961__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0250738961__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0250738961)

![](删除号段文件通知记录（RMV SEGFILENOTIFY）_50738961.assets/notice_3.0-zh-cn_2.png)

该操作会触发订阅通知，导致后续号段导入通知记录与预期不符。

**适用NF：NRF**

该命令用于在NRF上通过手动删除NF对应的IMSI/MSISDN号段信息达到NF号段更新，触发订阅通知。

## [注意事项](#ZH-CN_MMLREF_0250738961)

- 该命令执行后立即生效。

- 主备或双活两个NRF上均需执行此命令，配置参数值参考实际规划。

#### [操作用户权限](#ZH-CN_MMLREF_0250738961)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0250738961)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持IMSI/MSISDN号段支持的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>默认值：无<br>配置原则：<br>支持IMSI号段配置的NF类型仅包含AUSF、PCF、UDM、 UDR、CHF、CUSTOM_OCS。支持MSISDN号段配置的NF类型仅包含PCF、UDM、 UDR、CHF、CUSTOM_OCS。 |
| SEGTYPE | 号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>默认值：无<br>配置原则：无 |
| NFGROUPID | NF组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示待配置IMSI/MSISDN号段的NF组标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0250738961)

在NRF上手动触发删除CHF类型的NF组标识为nfgroup001的IMSI号段信息的订阅通知。

```
RMV SEGFILENOTIFY: SEGTYPE=IMSI, NFTYPE=CHF, NFGROUPID="nfgroup001";
```
