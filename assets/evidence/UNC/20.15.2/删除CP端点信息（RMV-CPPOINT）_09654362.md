# 删除CP端点信息（RMV CPPOINT）

- [命令功能](#ZH-CN_MMLREF_0209654362__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209654362__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209654362__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209654362__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209654362)

![](删除CP端点信息（RMV CPPOINT）_09654362.assets/notice_3.0-zh-cn_2.png)

删除CPPOINT会影响N4建链，请确认要删除的CPPOINT不会被使用。

删除CPPOINT会影响UPF节点的添加和修改，请确认要删除的CPPOINT中的VPNNAME不会被UPNODE使用。

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于删除CP端点信息，删除方式为根据CP端点的索引进行删除。

## [注意事项](#ZH-CN_MMLREF_0209654362)

- 该命令执行后立即生效。

- 执行本命令会导致在待删除CP端点上建立的会话中断。

#### [操作用户权限](#ZH-CN_MMLREF_0209654362)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209654362)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPPOINTINDEX | CP端点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定这个CP端点的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209654362)

删除CP端点索引为0的CP端点：

```
RMV CPPOINT: CPPOINTINDEX=0;
```
