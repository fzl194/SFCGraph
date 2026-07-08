# 激活一次链路迁移操作（ACT LINKMIGRATION）

- [命令功能](#ZH-CN_MMLREF_0000001663466285__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001663466285__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001663466285__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001663466285__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001663466285)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于在链路分布不均的场景下激活一次链路迁移，涉及的链路接口类型为Ga/Gx/Gy/S6b。链路迁移策略可以通过调试命令OPR DBGDATA的子命令calseqmigpolicy进行查询。

## [注意事项](#ZH-CN_MMLREF_0000001663466285)

- 该命令执行后立即生效。

- 链路迁移时的绑定方式由集中点部署模式决定(SET CONCENPOINT)。
- 对于Ga接口链路，仅在Ga集中点部署模式为SINGLE_CONNECT时生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001663466285)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001663466285)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKINFTYPE | 链路接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于用户指定链路迁移的接口类型。<br>数据来源：全网规划<br>取值范围：<br>- GX（Gx链路接口类型）<br>- GY（Gy链路接口类型）<br>- S6B（S6b链路接口类型）<br>- GA（Ga链路接口类型）<br>默认值：无<br>配置原则：无 |
| MIGRATIONTYPE | 迁移类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路迁移的迁移类型。<br>数据来源：本端规划<br>取值范围：<br>- “LOADBALANCE（负载均衡）”：负载均衡<br>- “ANTIAFFINITY（反亲和）”：反亲和<br>默认值：LOADBALANCE<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001663466285)

激活一次Ga接口链路迁移，迁移类型为反亲和：

```
ACT LINKMIGRATION:LINKINFTYPE=GA,MIGRATIONTYPE=ANTIAFFINITY;
```
