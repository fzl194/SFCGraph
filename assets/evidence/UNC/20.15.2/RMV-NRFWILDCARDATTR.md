# 删除分层互联通配属性（RMV NRFWILDCARDATTR）

- [命令功能](#ZH-CN_MMLREF_0209652345__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652345__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652345__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652345__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652345)

**适用NF：NRF**

该命令用于在NRF删除分层互联通配属性，以减少分层互联路由信息的配置量。

## [注意事项](#ZH-CN_MMLREF_0209652345)

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### [操作用户权限](#ZH-CN_MMLREF_0209652345)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652345)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ATTRIBUTE | 属性 | 可选必选说明：必选参数<br>参数含义：该参数用于表示分层互联属性类型。<br>数据来源：全网规划<br>取值范围：<br>- TAC（TAC）<br>- NRFNFGROUP（NFGROUP）<br>- SERVINGSCOPE（SERVINGSCOPE）<br>- REGIONIDSETID（区域标识和集合标识）<br>- ROUTINGINDICATOR（选路指示器）<br>默认值：无<br>配置原则：<br>每种属性最多只能配置一条分层互联通配属性。 |

## [使用实例](#ZH-CN_MMLREF_0209652345)

运营商完成分层互联路由配置后，不需要通配属性，想删除属性为NRFNFGROUP的分层互联通配属性信息时，执行此命令。

```
RMV NRFWILDCARDATTR: ATTRIBUTE=NRFNFGROUP;
```
