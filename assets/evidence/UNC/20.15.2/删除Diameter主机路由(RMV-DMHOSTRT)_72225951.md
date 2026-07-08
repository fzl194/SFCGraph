# 删除Diameter主机路由(RMV DMHOSTRT)

- [命令功能](#ZH-CN_MMLREF_0000001172225951__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225951__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225951__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225951__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225951__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225951__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225951)

![](删除Diameter主机路由(RMV DMHOSTRT)_72225951.assets/notice_3.0-zh-cn_2.png)

删除Diameter主机路由，将导致通过该主机路由连接的对端的Diameter链路发生中断。

**适用网元：SGSN、MME**

该命令用于删除一条Diameter主机路由。主机路由是指通过主机名来选择对端。在 UNC 和Diameter对端直连时使用此命令。相同选路模式的主机路由可以通过命令 [**ADD DMRTGRP**](../Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md) 配到同一个Diameter路由组中，业务通过引用路由组配置进行选路。

#### [注意事项](#ZH-CN_MMLREF_0000001172225951)

- 该命令执行后立即生效。
- 删除该主机路由，将导致通过该主机路由连接的对端的Diameter链路发生中断。
- 当Diameter路由组引用该路由索引时，不允许删除，可以在UNCMML窗口上执行命令[**LST DMRTGRP**](../Diameter路由组/查询Diameter路由组(LST DMRTGRP)_26306104.md)查看路由索引是否被引用。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225951)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225951)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225951)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEIDX | 路由索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter主机路由索引。<br>取值范围：0~1023<br>默认值：无<br>说明：可以通过<br>[**LST DMHOSTRT**](查询Diameter主机路由(LST DMHOSTRT)_72345873.md)<br>命令查看已有配置，确认所要删除的Diameter主机路由的索引。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225951)

删除索引号为0的Diameter主机路由：

RMV DMHOSTRT: ROUTEIDX=0;
