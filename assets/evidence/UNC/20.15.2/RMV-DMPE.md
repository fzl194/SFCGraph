# 删除Diameter对端实体(RMV DMPE)

- [命令功能](#ZH-CN_MMLREF_0000001126306096__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126306096__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126306096__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126306096__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126306096__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126306096__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126306096)

**适用网元：SGSN、MME**

该命令用于删除Diameter对端实体配置。

#### [注意事项](#ZH-CN_MMLREF_0000001126306096)

- 该命令执行后立即生效。
- 当DMHOSTRT，DMRT和DMLKS引用该对端实体索引时，不允许删除，在“MML命令行-UNC”窗口上执行命令[**LST DMHOSTRT**](../Diameter主机路由/查询Diameter主机路由(LST DMHOSTRT)_72345873.md)，[**LST DMRT**](../Diameter路由/查询Diameter域路由配置(LST DMRT)_72225969.md)，[**LST DMLKS**](../Diameter链路集/查询Diameter链路集配置(LST DMLKS)_26146280.md)查看对端实体索引是否被引用。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126306096)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126306096)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126306096)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERIDX | 对端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter对端实体索引。<br>取值范围：0～639<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126306096)

删除索引为2的Diameter对端实体配置：

RMV DMPE: PEERIDX=2;
