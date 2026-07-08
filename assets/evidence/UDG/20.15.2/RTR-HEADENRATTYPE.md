# 恢复头增强RAT类型定义（RTR HEADENRATTYPE）

- [命令功能](#ZH-CN_CONCEPT_0186527135__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186527135__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186527135__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186527135__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186527135__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0186527135)

**适用NF：PGW-U、UPF**

该命令用于恢复头增强全局参数默认值，初始化RAT类型设置。

#### [注意事项](#ZH-CN_CONCEPT_0186527135)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0186527135)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186527135)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPEVALUE | RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个RAT类型，查询其相应字符串的值。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- RESERVED：预留RAT类型。<br>- UTRAN：无线接入类型为UMTS陆地无线接入网。<br>- GERAN：无线接入类型为GSM/EDGE无线接入网。<br>- WLAN：无线接入类型为无线局域网。<br>- GAN：无线接入类型为通用接入网络。<br>- HSPAE：无线接入类型为增强型高速分组接入。<br>- EUTRAN：无线接入类型为演进UMTS陆地无线接入网。<br>- VIRTUAL：无线接入类型为Virtual。<br>- EUTRANNBIOT：无线接入类型为EUTRAN-NB-IoT。<br>- LTEM：无线接入类型为LTE-M。<br>- NR：无线接入类型为NR。<br>- REDCAPNR：无线接入类型为RedCap-NR。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186527135)

假如运营商希望恢复无线接入类型为WLAN的头增强参数默认值WLANSTR，可以通过该命令恢复该无线接入类型的头增强参数默认值：

```
RTR HEADENRATTYPE:RATTYPEVALUE=WLAN;
```
