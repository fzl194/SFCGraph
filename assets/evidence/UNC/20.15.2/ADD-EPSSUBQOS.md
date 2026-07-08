# 增加EPS签约QoS配置（ADD EPSSUBQOS）

- [命令功能](#ZH-CN_MMLREF_0209653648__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653648__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653648__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653648__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653648)

**适用NF：SGW-C、PGW-C**

该命令用来配置用户的签约QoS属性。当APN下使能COA功能时，RADIUS鉴权服务器会下发subscriber-qos index，UNC根据index匹配到subscriber-qos配置，用来进行用户QoS的协商控制，主动调整带宽等。

如果RADIUS鉴权服务器没有下发subscriber-qos index，则根据APN下绑定的qos-profile下的subscriber-qos index进行用户QoS的协商控制、调整带宽等。

## [注意事项](#ZH-CN_MMLREF_0209653648)

- 该命令执行后只对新激活用户生效。

- 该配置必须和网络规划一致，否则会导致用户的带宽和业务级别等控制出现问题。

- 最多可输入100条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0209653648)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653648)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBQOSINDEX | 用户QoS索引 | 可选必选说明：必选参数<br>参数含义：该参数表示用户QoS索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| QCI | 标准QCI | 可选必选说明：必选参数<br>参数含义：该参数表示QoS业务类型参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~9，69~70。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP的优先级别 | 可选必选说明：必选参数<br>参数含义：该参数表示分配优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| AMBRDL | 下行APN AMBRR(千比特/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于设置下行APN-AMBR比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2000000。<br>默认值：无<br>配置原则：无 |
| AMBRUL | 上行APN AMBRR(千比特/秒) | 可选必选说明：必选参数<br>参数含义：该参数用于设置上行APN-AMBR比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2000000。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653648)

增加EPSSUBQOS，“SUBQOSINDEX”为“123”，“AMBRDL”为“564110”，“AMBRUL”为“300000”，“ARPPL”为“10”，“QCI”为“5”：

```
ADD EPSSUBQOS: SUBQOSINDEX=123, QCI=5, ARPPL=10, AMBRDL=564110, AMBRUL=300000;
```
