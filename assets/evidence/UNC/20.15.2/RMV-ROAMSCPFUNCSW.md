# 删除漫游跨PLMN场景间接路由配置（RMV ROAMSCPFUNCSW）

- [命令功能](#ZH-CN_MMLREF_0000001179735156__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001179735156__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001179735156__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001179735156__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001179735156)

**适用NF：AMF、SMF**

该命令用于删除漫游跨PLMN场景间接路由配置。

## [注意事项](#ZH-CN_MMLREF_0000001179735156)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001179735156)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001179735156)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNFTYPE | 本端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “AMF（AMF）”：NF类型为AMF<br>- “SMF（SMF）”：NF类型是SMF<br>默认值：无<br>配置原则：无 |
| PNFTYPE | 对端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “UDM（UDM）”：NF类型是UDM<br>- “AUSF（AUSF）”：NF类型为AUSF<br>- “AMF（AMF）”：NF类型为AMF<br>- “SMF（SMF）”：NF类型为SMF<br>- “EIR（5G-EIR）”：NF类型为5G-EIR<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001179735156)

运营商需要删除漫游跨PLMN场景下本端AMF与对端UDM之间的间接路由配置。

```
RMV ROAMSCPFUNCSW: LNFTYPE=AMF, PNFTYPE=UDM;
```
