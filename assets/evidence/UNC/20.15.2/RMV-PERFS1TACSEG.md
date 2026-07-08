# 删除S1TAC段（RMV PERFS1TACSEG）

- [命令功能](#ZH-CN_MMLREF_0244530774__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0244530774__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0244530774__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0244530774__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0244530774)

**适用NF：SGW-C、PGW-C**

该命令用来删除某个S1TAC号段。

## [注意事项](#ZH-CN_MMLREF_0244530774)

- 该命令执行后立即生效。

- RMV PERFS1TACSEG时同时删除关联的PERFREGTAC配置。

#### [操作用户权限](#ZH-CN_MMLREF_0244530774)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0244530774)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACSEGNAME | TAC段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0244530774)

当运营商需要删除一个TAC号段，执行如下命令：

```
RMV PERFS1TACSEG: TACSEGNAME="changping";
```
