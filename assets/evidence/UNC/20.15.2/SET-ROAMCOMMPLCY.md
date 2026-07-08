# 设置漫游通信策略（SET ROAMCOMMPLCY）

- [命令功能](#ZH-CN_MMLREF_0000001224207973__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001224207973__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001224207973__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001224207973__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001224207973)

**适用NF：AMF、SMF**

该命令用于设置漫游场景下跨PLMN的网元之间的通信策略。

## [注意事项](#ZH-CN_MMLREF_0000001224207973)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ROUTEMODE | SEPPMODE |
| --- | --- |
| SEPP | HTTPPROXY |

#### [操作用户权限](#ZH-CN_MMLREF_0000001224207973)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001224207973)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEMODE | 漫游路由模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定漫游路由模式。<br>数据来源：全网规划<br>取值范围：<br>- “SEPP（通过SEPP通信）”：漫游跨PLMN的网元之间通过SEPP通信<br>- “SCP（优选SCP通信）”：漫游跨PLMN的网元之间优选SCP通信，如果根据本端NfType与对端NfType能找到ROAMSCPFUNCSW配置记录则通过SCP对接SEPP通信（如果没有配置SCP则无法通信）；如果根据本端NfType与对端NfType不能找到ROAMSCPFUNCSW配置记录则通过SEPP通信。<br>- “DIRECT（直连通信）”：漫游跨PLMN的网元之间通过直连通信（该枚举值仅用于测试场景）<br>默认值：无。<br>配置原则：无 |
| SEPPMODE | 信令汇聚模式 | 可选必选说明：该参数在"ROUTEMODE"配置为"SEPP"、"SCP"时为条件必选参数。<br>参数含义：该参数用于指定漫游信令汇聚模式。仅在ROUTEMODE设置为SEPP或SCP时生效。<br>数据来源：全网规划<br>取值范围：<br>- “HTTPPROXY（Http Proxy）”：在服务请求消息的authority中填写目标NF的地址信息<br>- “TARGETAPIROOT（3gpp-Sbi-Target-apiroot）”：在服务请求消息的3gpp-Sbi-Target-apiroot中填写目标NF的地址信息<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ROAMCOMMPLCY查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001224207973)

运营商希望漫游跨PLMN的网元之间通过SEPP通信，且在服务请求消息的authority中填写目标NF的地址信息，需要设置漫游通信策略；

```
SET ROAMCOMMPLCY: ROUTEMODE=SEPP, SEPPMODE=HTTPPROXY;
```
