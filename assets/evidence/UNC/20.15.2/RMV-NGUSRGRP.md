# 删除5G用户群（RMV NGUSRGRP）

- [命令功能](#ZH-CN_MMLREF_0244007669__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0244007669__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0244007669__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0244007669__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0244007669)

**适用NF：AMF**

该命令用于删除5G用户群记录。

删除用户群时必须首先删除该用户群下的全部成员记录。可执行LST NGUSRGRPMEM查看用户群下的成员记录。

删除用户群时必须保证已有配置命令中不存在该用户群标识的相关记录，可执行LST NITZPLCY、LST NGACCAREALST、LST LCSPERMITCFG、LST NGAREARESELPLCY、LST AMFRESELPLCY、LST NGGUTISELPLCY命令查看是否用到该用户群标识。

## [注意事项](#ZH-CN_MMLREF_0244007669)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0244007669)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0244007669)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRGRPID | 用户群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G用户群标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0244007669)

删除标识为20的5G用户群记录，执行如下命令：

```
RMV NGUSRGRP: USRGRPID=20;
```
