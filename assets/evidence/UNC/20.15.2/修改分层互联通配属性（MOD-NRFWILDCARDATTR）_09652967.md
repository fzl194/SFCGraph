# 修改分层互联通配属性（MOD NRFWILDCARDATTR）

- [命令功能](#ZH-CN_MMLREF_0209652967__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652967__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652967__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652967__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652967)

**适用NF：NRF**

该命令用于在NRF修改分层互联通配属性。

## [注意事项](#ZH-CN_MMLREF_0209652967)

- 该命令执行后立即生效。

- 当分层互联属性类型为TAC时，通配的起始位置加通配的长度小于等于6，即MATCHSTART+MATCHLEN<=6。
- 当分层互联属性类型为NFGROUP或SERVINGSCOPE时，通配的起始位置加通配的长度小于等于128，即MATCHSTART+MATCHLEN<=128。
- 当分层互联属性类型为REGIONIDSETID时，通配的起始位置加通配的长度小于等于18，即MATCHSTART+MATCHLEN<=18。
- 当分层互联属性类型为ROUTINGINDICATOR时，通配的起始位置加通配的长度小于等于4，即MATCHSTART+MATCHLEN<=4。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### [操作用户权限](#ZH-CN_MMLREF_0209652967)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652967)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ATTRIBUTE | 属性 | 可选必选说明：必选参数<br>参数含义：该参数用于表示分层互联属性类型。<br>数据来源：全网规划<br>取值范围：<br>- TAC（TAC）<br>- NRFNFGROUP（NFGROUP）<br>- SERVINGSCOPE（SERVINGSCOPE）<br>- REGIONIDSETID（区域标识和集合标识）<br>- ROUTINGINDICATOR（选路指示器）<br>默认值：无<br>配置原则：<br>每种属性最多只能配置一条分层互联通配属性。 |
| MATCHSTART | 起始位置 | 可选必选说明：必选参数<br>参数含义：该参数用于表示通配的起始位置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| MATCHLEN | 通配长度 | 可选必选说明：必选参数<br>参数含义：该参数用于表示通配的长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652967)

运营商修改分层互联通配属性信息，达到快速修改NRF路由的效果：针对的通配信息为：NRFNFGROUP中起始位置为0，通配长度为3位的省份通配信息，执行此命令。

```
MOD NRFWILDCARDATTR: ATTRIBUTE=NRFNFGROUP, MATCHSTART=0, MATCHLEN=3;
```
