# 删除CP GTP-U地址（RMV CPGTPUADDR）

- [命令功能](#ZH-CN_MMLREF_0296805498__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296805498__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296805498__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296805498__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0296805498)

![](删除CP GTP-U地址（RMV CPGTPUADDR）_96805498.assets/notice_3.0-zh-cn_2.png)

删除CPGTPUADDR会导致用户激活失败，请确认要删除的CPGTPUADDR不会被使用。

与UPF对接启用GTP-U时，删除CPGTPUADDR会导致已经激活的用户无法和UPF传递信息（比如RS/RA）。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除与UPF对接的本端用户面地址。

## [注意事项](#ZH-CN_MMLREF_0296805498)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0296805498)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0296805498)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定与UPF对接的本端GTP-U IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0296805498)

删除一个与UPF对接的本端GTP-U IPv4地址：

```
RMV CPGTPUADDR:IPVERSION=IPV4;
```
