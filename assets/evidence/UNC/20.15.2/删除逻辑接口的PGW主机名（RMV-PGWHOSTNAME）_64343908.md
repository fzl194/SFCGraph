# 删除逻辑接口的PGW主机名（RMV PGWHOSTNAME）

- [命令功能](#ZH-CN_MMLREF_0264343908__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0264343908__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0264343908__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0264343908__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0264343908)

**适用NF：PGW-C**

此命令用于删除PGW-C逻辑接口主机名。根据网络规划，当需要修改逻辑接口主机名时，需要先执行该命令，再执行ADD PGWHOSTNAME命令。

## [注意事项](#ZH-CN_MMLREF_0264343908)

- 该命令执行后立即生效。

- 如果没有该配置，且配置需要向Diameter AAA上报hostname，可能导致Diameter AAA授权失败。

#### [操作用户权限](#ZH-CN_MMLREF_0264343908)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0264343908)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C接口类型。<br>数据来源：本端规划<br>取值范围：<br>- S5_P_OR_GN_OR_S2B（S5-P/Gn/S2b/S2a接口）<br>- S8_P_OR_GP_OR_S2B（S8-P/Gp/S2b/S2a接口）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0264343908)

根据网络规划，需要删除PGW-C接口类型为S5_P_OR_GN_OR_S2B的配置：

```
RMV PGWHOSTNAME: INTFTYPE=S5_P_OR_GN_OR_S2B;
```
