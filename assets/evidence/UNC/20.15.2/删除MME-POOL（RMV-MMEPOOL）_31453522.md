# 删除MME POOL（RMV MMEPOOL）

- [命令功能](#ZH-CN_MMLREF_0231453522__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0231453522__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0231453522__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0231453522__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0231453522)

**适用NF：SGW-C、PGW-C**

该命令用于删除MME POOL。假设运营商不再使用MME POOL时，使用该命令。

## [注意事项](#ZH-CN_MMLREF_0231453522)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0231453522)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0231453522)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEPOOLNAME | MME POOL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME POOL名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0231453522)

假设要删除一个名为“mmepool1”的MME POOL：

```
RMV MMEPOOL:MMEPOOLNAME="mmepool1";
```
